"""
Section class for s2e tracking.
S.Tomin. XFEL/DESY. 2017

Vendored from ocelot.utils.section_track.  It is only ever used with the
EuXFEL, and this repository needs to change how it interacts with the lattice,
so it is maintained here rather than upstream.  Taken verbatim apart from the
imports, which were six `from ocelot.cpbd.* import *` lines and are now
explicit.
"""

import copy
import os

import numpy as np
from ocelot.cpbd.beam import Twiss
from ocelot.cpbd.csr import CSR
from ocelot.cpbd.elements import Cavity
from ocelot.cpbd.io import load_particle_array, save_particle_array
from ocelot.cpbd.magnetic_lattice import MagneticLattice
from ocelot.cpbd.navi import Navigator
from ocelot.cpbd.physics_proc import IBS, BeamTransform, SmoothBeam
from ocelot.cpbd.sc import LSC, SpaceCharge
from ocelot.cpbd.track import track, twiss
from ocelot.cpbd.transformations.second_order import SecondTM
from ocelot.cpbd.wake3D import Wake, WakeKick

__all__ = ["SectionLattice", "SectionTrack"]

#: Config keys that used to set magnets and RF from inside tracking.  They are
#: now owned by euxfel.volts.MachineSetpoints, which writes them onto the
#: lattice before a SectionLattice is built.
_MOVED_TO_SETPOINTS = {
    "rho": "a bunch compressor",
    "v": "cavity voltage",
    "phi": "cavity phase",
    "tds.v": "TDS voltage",
    "tds.phi": "TDS phase",
}


def _reject_setpoints(section, conf):
    """Refuse a config that still tries to set the machine during tracking.

    Silently ignoring these would be the worst outcome: a script would run to
    completion with its compression or RF quietly at the design values.
    """
    present = sorted(key for key in _MOVED_TO_SETPOINTS if key in conf)
    if not present:
        return
    raise ValueError(
        f"{type(section).__name__}: "
        f"{', '.join(repr(key) for key in present)} "
        f"({', '.join(_MOVED_TO_SETPOINTS[key] for key in present)}) "
        f"no longer belong in the section config -- the lattice is owned by "
        f"euxfel.volts.MachineSetpoints. Set them there and apply the "
        f"setpoints before building the SectionLattice:\n"
        f"    setpoints.bc2.r56 = ...       # or .l1.chirp, .tds_b2.voltage\n"
        f"    setpoints.apply_in_place(full_machine_cell())\n"
        f"The config dict now carries physics processes only "
        f"(SC, CSR, wake, smooth, match)."
    )


class SectionLattice:
    """
    High level class to work with SectionTrack()
    """

    def __init__(
        self, sequence, tws0=None, data_dir=".", main_config=None, *args, **kwargs
    ):  # Added main_config
        """
        :param sequence: list of SectionTrack()
        :param main_config: The main configuration dictionary from the script
        """
        self.sec_seq = sequence
        self.elem_seq = None
        self.tws = None
        self.tws0 = tws0
        self.tws_current = None
        self.data_dir = data_dir
        self.main_config = main_config  # Store the main config
        # Pass *args and **kwargs (like coupler_kick) to initialize
        self.initialize(*args, **kwargs)

    def initialize(self, *args, **kwargs):  # Accepts *args, **kwargs from __init__
        # Pass main_config and other args/kwargs to init_sections
        self.init_sections(self.main_config, *args, **kwargs)
        self.tws = self.calculate_twiss(self.tws0)

    def init_sections(
        self, main_config=None, *args, **kwargs_from_sl_init
    ):  # Accepts main_config and *args,**kwargs
        """
        Method initiates section and return dictionary with initialized sections
        :param main_config: The main configuration dictionary
        :param args: additional args for section constructors
        :param kwargs_from_sl_init: additional kwargs (like coupler_kick) for section constructors
        :return: self.dict_sections - dictionary
        """
        self.dict_sections = {}
        self.elem_seq = []
        for sec_class in self.sec_seq:
            # Prepare specific initialization parameters for this section class
            sec_init_params = {}
            if main_config and sec_class in main_config:
                sec_init_params = main_config[sec_class].get("init_params", {})

            # Merge kwargs: kwargs_from_sl_init are general, sec_init_params are specific.
            # Specific params can override general ones if keys conflict.
            # The section constructor will receive data_dir, *args, and merged kwargs.
            current_sec_kwargs = {**kwargs_from_sl_init, **sec_init_params}
            s = sec_class(self.data_dir, *args, **current_sec_kwargs)

            # Existing coupler_kick logic (example, adapt if it was different)
            # This relies on 'coupler_kick' being in kwargs_from_sl_init
            if (
                "coupler_kick" in kwargs_from_sl_init
                and kwargs_from_sl_init["coupler_kick"] is False
            ):
                s.remove_coupler_kicks()

            self.dict_sections[sec_class] = s
            self.elem_seq.append(s.lattice.sequence)
        return self.dict_sections

    def calculate_twiss(self, tws0=None):
        """
        Method calculates twiss parameters for whole lattice [sequence of lattices]
        and assigns for each section initial Twiss() - section.tws0

        :param tws0: Twiss() - initial twiss parameters
        :return: return list of Twiss()
        """
        tws_whole = []
        for sec in self.sec_seq:
            s = self.dict_sections[sec]
            s.tws0 = tws0
            if s.tws0 is not None:
                tws = twiss(s.lattice, tws0)
                tws0 = tws[-1]
                tws_whole = np.append(tws_whole, tws)
        return tws_whole

    def update_sections(self, sections, config=None, coupler_kick=False):

        new_sections = []
        tws0 = self.dict_sections[sections[0]].tws0
        tws_whole = []
        seq_current = []
        for sec in sections:
            # np.random.seed(10)
            sec = self.dict_sections[sec]
            if not coupler_kick:
                sec.remove_coupler_kicks()

            if config is not None and sec.__class__ in config.keys():
                conf = config[sec.__class__]
                _reject_setpoints(sec, conf)
                if "match" in conf.keys() and conf["match"] is True:
                    bounds = [-5, 5]
                    remove_offsets = True
                    if "bounds" in conf.keys():
                        bounds = conf["bounds"]
                    if "remove_offsets" in conf.keys():
                        remove_offsets = conf["remove_offsets"]
                    sec.apply_matching(bounds=bounds, remove_offsets=remove_offsets)
                if "SC" in conf.keys():
                    sec.sc_flag = conf["SC"]
                if "CSR" in conf.keys():
                    sec.csr_flag = conf["CSR"]
                if "smooth" in conf.keys():
                    sec.smooth_flag = conf["smooth"]
                if "wake" in conf.keys():
                    sec.wake_flag = conf["wake"]
                if "IBS" in conf.keys():
                    sec.ibs_flag = conf["IBS"]

                if "save_output_files" in conf.keys():
                    sec.save_output_files = conf["save_output_files"]

            sec.lattice.update_transfer_maps()
            new_sections.append(sec)
            seq_current.append(sec.lattice.sequence)
            if tws0 is not None:
                tws = twiss(sec.lattice, tws0)
                tws0 = tws[-1]
                tws_whole = np.append(tws_whole, tws)
        self.tws_current = tws_whole
        self.lat_current = MagneticLattice(
            copy.deepcopy(seq_current), method={"global": SecondTM}
        )
        return new_sections

    def track_sections(
        self,
        sections,
        p_array,
        config=None,
        force_ext_p_array=False,
        coupler_kick=False,
        verbose=True,
        twiss_disp_correction=False,
    ):
        self.tws_track = []
        L = 0.0
        self.update_sections(sections, config=config, coupler_kick=coupler_kick)
        for i, sec in enumerate(sections):
            sec = self.dict_sections[sec]
            if i == 0 and sec.__class__ != self.sec_seq[0] and not force_ext_p_array:
                p_array = None
            sec.print_progress = verbose
            p_array = sec.tracking(
                particles=p_array, twiss_disp_correction=twiss_disp_correction
            )
            tws_track = copy.deepcopy(sec.tws_track)
            for tws in tws_track:
                tws.s += L
            L = tws_track[-1].s
            self.tws_track = np.append(self.tws_track, tws_track)
        return p_array

    def load_twiss_track(self, sections):
        s = []
        bx = []
        by = []
        s0 = 0
        for i, sec in enumerate(sections):
            sec = self.dict_sections[sec]
            tws = sec.load_twiss_file()
            s_tws = np.array(tws["s"])
            s_tws = s_tws - s_tws[0] + s0
            s0 = s_tws[-1]
            s = np.append(s, s_tws)
            bx = np.append(bx, tws["beta_x"])
            by = np.append(by, tws["beta_y"])
        return s, bx, by


class SectionTrack:
    def __init__(self, data_dir, *args, **kwargs):
        # Store all kwargs passed during instantiation.
        # These will include both parameters from SectionLattice's direct pass-through
        # and specific init_params for this section.
        self.init_parameters = kwargs  # Store kwargs

        self.lattice_name = ""
        self.lattice = None
        self.tws0 = None

        self.unit_step = 1.0

        self.input_beam_file = None
        self.output_beam_file = None
        self.tws_file = None

        # self.data_dir = "."
        self.particle_dir = data_dir + "/particles/"
        self.tws_dir = data_dir + "/tws/"

        self.physics_processes_array = []  # list of physics process
        self.method = {"global": SecondTM}
        self.sc_flag = True
        self.csr_flag = True
        self.wake_flag = True
        self.bt_flag = True
        self.smooth_flag = True
        self.ibs_flag = True

        self.calc_tws = True
        self.kill_track = False
        self.save_output_files = True

    def remove_coupler_kicks(self):
        print("REMOVE Coupler kick")
        for e in self.lattice.sequence:
            if e.__class__ == Cavity:
                e.vx_up = 0
                e.vy_up = 0
                e.vxx_up = 0
                e.vxy_up = 0
                e.vx_down = 0
                e.vy_down = 0
                e.vxx_down = 0
                e.vxy_down = 0

    def apply_matching(self, bounds=None, remove_offsets=True):

        if bounds is None:
            bounds = [-5, 5]

        if self.tws0 is None:
            print("TWISS is not defined")
            return

        self.tws0.mux = 0
        self.tws0.muy = 0
        bt = BeamTransform(tws=self.tws0, remove_offsets=remove_offsets, bounds=bounds)
        self.add_physics_process(bt, self.lattice.sequence[0], self.lattice.sequence[0])

    def init_navigator(self):

        # init navigator
        self.navigator = Navigator(self.lattice)
        self.navigator.unit_step = self.unit_step

        # init physics processes
        for physics_process in self.physics_processes_array:
            if (
                physics_process[0].__class__ == SpaceCharge
                or physics_process[0].__class__ == LSC
            ) and self.sc_flag:
                self.navigator.add_physics_proc(
                    physics_process[0], physics_process[1], physics_process[2]
                )

            if physics_process[0].__class__ == CSR and self.csr_flag:
                self.navigator.add_physics_proc(
                    physics_process[0], physics_process[1], physics_process[2]
                )

            if physics_process[0].__class__ == IBS and self.ibs_flag:
                self.navigator.add_physics_proc(
                    physics_process[0], physics_process[1], physics_process[2]
                )

            if (
                physics_process[0].__class__ == Wake
                or physics_process[0].__class__ == WakeKick
            ) and self.wake_flag:
                self.navigator.add_physics_proc(
                    physics_process[0], physics_process[1], physics_process[2]
                )

            if physics_process[0].__class__ == BeamTransform and self.bt_flag:
                self.navigator.add_physics_proc(
                    physics_process[0], physics_process[1], physics_process[2]
                )

            if physics_process[0].__class__ == SmoothBeam and self.smooth_flag:
                self.navigator.add_physics_proc(
                    physics_process[0], physics_process[1], physics_process[2]
                )

            if physics_process[0].__class__ not in [
                SpaceCharge,
                CSR,
                Wake,
                WakeKick,
                BeamTransform,
                SmoothBeam,
                LSC,
                IBS,
            ]:
                self.navigator.add_physics_proc(
                    physics_process[0], physics_process[1], physics_process[2]
                )

    def add_physics_process(self, physics_process, start, stop):

        self.physics_processes_array.append([physics_process, start, stop])

    def read_beam_file(self):

        particles = None

        try:
            particles = load_particle_array(self.input_beam_file)

        except:  # noqa: E722  (inherited from upstream; narrow it separately)
            print(
                self.lattice_name
                + " - #### ERROR #### - NO START PARTICLES FILE: "
                + self.input_beam_file
            )

        return particles

    def folder_check_create(self, filename):
        # path to directory
        dir_path = os.path.dirname(os.path.abspath(filename))
        # check if exist
        if not os.path.exists(dir_path):
            # create
            os.makedirs(dir_path)

    def save_beam_file(self, particles):
        self.folder_check_create(self.output_beam_file)
        save_particle_array(self.output_beam_file, particles)

    def save_twiss_file(self, twiss_list):
        if self.tws_file is None:
            tws_file_name = self.output_beam_file.replace("particles", "tws")
        else:
            tws_file_name = self.tws_file

        self.folder_check_create(tws_file_name)

        bx = np.array([tw.beta_x for tw in twiss_list])
        by = np.array([tw.beta_y for tw in twiss_list])
        ax = np.array([tw.alpha_x for tw in twiss_list])
        ay = np.array([tw.alpha_x for tw in twiss_list])
        s = np.array([tw.s for tw in twiss_list])
        E = np.array([tw.E for tw in twiss_list])

        emit_x = np.array([tw.emit_x for tw in twiss_list])
        emit_y = np.array([tw.emit_y for tw in twiss_list])

        np.savez_compressed(
            tws_file_name,
            beta_x=bx,
            beta_y=by,
            alpha_x=ax,
            alpha_y=ay,
            E=E,
            s=s,
            emit_x=emit_x,
            emit_y=emit_y,
        )

    def load_twiss_file(self):
        return np.load(self.tws_file)

    def get_tws_list(self):
        tws_dict = {}
        n = 0
        with np.load(self.tws_file) as data:
            for key in data:
                tws_dict[key] = data[key]
                n = len(data[key])
        tws_list = []
        for i in range(n):
            tws = Twiss()
            for key in tws_dict:
                tws.__dict__[key] = tws_dict[key][i]

            tws_list.append(tws)

        return tws_list

    def tracking(self, particles=None, twiss_disp_correction=False):

        # read beam file
        if particles is None:
            particles = self.read_beam_file()
            if particles is None:
                return None

        # init navigator
        self.init_navigator()

        # tracking
        print()
        print(self.lattice_name + " TRACKING")
        # print("std1 = ", np.std(particles.tau()))
        tws_track, particles = track(
            self.lattice,
            particles,
            self.navigator,
            print_progress=self.print_progress,
            calc_tws=self.calc_tws,
            twiss_disp_correction=twiss_disp_correction,
        )
        self.tws_track = tws_track
        # save tracking results
        if (
            self.output_beam_file is not None
            and self.save_output_files
            and not self.kill_track
        ):
            self.save_beam_file(particles)
            self.save_twiss_file(tws_track)

        return particles
