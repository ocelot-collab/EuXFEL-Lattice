"""Main module."""

from math import copysign

import matplotlib as mpl
import matplotlib.patches as patches
import numpy as np

MAGNET_WIDTH = 0.1

DEFAULT_COLOUR_MAP = {
    "Quadrupole": "red",
    "SBend": "blue",
    "RBend": "blue",
    "RFCavity": "orange",
    "Cavity": "orange",
    "Marker": None,
    "Drift": None,
    "Monitor": None,
    "HKicker": "purple",
    "VKicker": "purple",
    "Kicker": "purple",
    "Collimator": "black",
    "GenericMap": "rosybrown",
    "Solenoid": "olive",
    "Sextupole": "lawngreen",
    "Octupole": "green",
    "TransverseDeflectingCavity": "magenta",
    "Undulator": "cyan",
}


# dict_plot = {Quadrupole: {"scale": 0.7, "color": "r", "edgecolor": "r", "label": "quad"},
#              Sextupole: {"scale": 0.5, "color": "g", "edgecolor": "g", "label": "sext"},
#              Octupole: {"scale": 0.5, "color": "g", "edgecolor": "g", "label": "oct"},
#              Cavity: {"scale": 0.7, "color": "orange", "edgecolor": "lightgreen", "label": "cav"},
#              TWCavity: {"scale": 0.7, "color": "orange", "edgecolor": "lightgreen", "label": "twcav"},
#              Bend: {"scale": 0.7, "color": "lightskyblue", "edgecolor": "k", "label": "bend"},
#              RBend: {"scale": 0.7, "color": "lightskyblue", "edgecolor": "k", "label": "bend"},
#              SBend: {"scale": 0.7, "color": "lightskyblue", "edgecolor": "k", "label": "bend"},
#              Matrix: {"scale": 0.7, "color": "pink", "edgecolor": "k", "label": "mat"},
#              Multipole: {"scale": 0.7, "color": "g", "edgecolor": "k", "label": "mult"},
#              Undulator: {"scale": 0.7, "color": "pink", "edgecolor": "k", "label": "und"},
#              Monitor: {"scale": 0.5, "color": "orange", "edgecolor": "orange", "label": "mon"},
#              Hcor: {"scale": 0.7, "color": "c", "edgecolor": "c", "label": "cor"},
#              Vcor: {"scale": 0.7, "color": "c", "edgecolor": "c", "label": "cor"},
#              Drift: {"scale": 0., "color": "k", "edgecolor": "k", "label": ""},
#              Marker: {"scale": 0., "color": "k", "edgecolor": "k", "label": "mark"},
#              Solenoid: {"scale": 0.7, "color": "g", "edgecolor": "g", "label": "sol"},
#              TDCavity: {"scale": 0.7, "color": "magenta", "edgecolor": "g", "label": "tds"},
#              UnknownElement: {"scale": 0.7, "color": "g", "edgecolor": "g", "label": "unk"},
#              XYQuadrupole: {"scale": 0.7, "color": "r", "edgecolor": "r", "label": "xyquad"},
#              Aperture: {"scale": 0.7, "color": "g", "edgecolor": "g", "label": "ap"},
#              }


def draw_survey(
    fig,
    axes,
    sequence,
    colour_map=None,
    annotate=True,
    dimension="x",
    magnet_width=MAGNET_WIDTH,
    **drawlinekw,
):
    try:
        survey = sequence.survey()
    except AttributeError:
        survey = sequence

    draw_survey_line(axes, survey["z"], survey[dimension], **drawlinekw)

    if colour_map is None:
        colour_map = DEFAULT_COLOUR_MAP

    patch_ids_to_annotations = {}
    patch_ids_to_elements = {}

    for row in survey.iter_rows(named=True):
        colour = DEFAULT_COLOUR_MAP[row["keyword"]]
        alpha = 1

        if not row["active"]:
            alpha = 0.25

        if colour is None:
            alpha = 0.0

        x, y, z = row["x"], row["y"], row["z"]
        # This is the end basically.
        if dimension == "y":
            x = y
        elif dimension != "x":
            raise ValueError(f"Unrecognised dimension type {dimension}.")

        length = row["length"]
        patch_start_x = z - length
        patch_width = length
        patch_start_y = x - 2 * magnet_width
        patch_height = 4 * magnet_width

        # Quadrupoles are drawn at half height, above or below the beamline
        # according to their polarity.  Upstream reached for `element` here,
        # which is never bound in this function -- the survey DataFrame
        # already carries both the type and k1, so use those instead.
        # copysign(h, 0.0) is positive, so a zero-strength quadrupole draws
        # upwards, matching draw()'s use of np.sign(k1).
        if row["keyword"] == "Quadrupole":
            patch_height = copysign(patch_height * 0.5, row["k1"])
            patch_start_y = x

        rectx = patches.Rectangle(
            (patch_start_x, patch_start_y),
            patch_width,
            patch_height,
            linewidth=0.1,
            # label=label,
            edgecolor="white",
            facecolor=colour,
            alpha=alpha,
        )
        xcentre = patch_start_x + 0.5 * patch_width
        ycentre = patch_start_y + 0.5 * patch_height
        t2 = (
            mpl.transforms.Affine2D().rotate_around(xcentre, ycentre, -row["theta"])
            + axes.transData
        )
        rectx.set_transform(t2)
        axes.add_patch(rectx)

        if annotate:
            element_type = row["keyword"]
            name = row["name"]
            annotation = axes.annotate(
                f"{element_type}: {name}",
                xy=(z, x),  # xycoords='data',
                xytext=(z, x),
                textcoords="data",
                horizontalalignment="left",
                arrowprops=dict(arrowstyle="simple", connectionstyle="arc3,rad=+0.2"),
                bbox=dict(boxstyle="round", facecolor="w", edgecolor="0.5", alpha=0.9),
                fontsize=18,
            )
            # by default, disable the annotation visibility
            annotation.set_visible(False)
            patch_ids_to_annotations[id(rectx)] = annotation
            patch_ids_to_elements[id(rectx)] = row
            rectx.set_picker(True)

    def on_pick(event):
        annotation = patch_ids_to_annotations[id(event.artist)]
        annotation.set_visible(not annotation.get_visible())
        fig.canvas.draw_idle()  # text_from_points=False
        element = patch_ids_to_elements[id(event.artist)]
        print(repr(element))

    def on_press(event):
        if event.key == "c":  # press c to clear the annotations.
            for annotation in patch_ids_to_annotations.values():
                annotation.set_visible(False)
        fig.canvas.draw_idle()

    fig.canvas.mpl_connect("pick_event", on_pick)
    fig.canvas.mpl_connect("key_press_event", on_press)


def draw(
    fig,
    axes,
    sequence,
    colour_map=None,
    annotate=True,
    magnet_width=MAGNET_WIDTH,
    coords="curvilinear",
    s_offset=0,
    **drawlinekw,
):
    draw_line(axes, sequence, s_offset=s_offset, **drawlinekw)
    if colour_map is None:
        colour_map = DEFAULT_COLOUR_MAP

    patch_ids_to_annotations = {}
    patch_ids_to_elements = {}

    for element, row in zip(sequence, sequence.survey().iter_rows(named=True)):
        colour = DEFAULT_COLOUR_MAP[row["keyword"]]
        alpha = 1

        if not element.is_active():
            alpha = 0.25

        if colour is None:
            alpha = 0.0

        # This is the end basically.
        length = element.length

        if coords == "curvilinear":
            element_x1 = row["s"] + s_offset
            element_x0 = element_x1 - length
        elif coords == "cartesian":
            element_x1 = row["z"] + s_offset
            element_x0 = element_x1 - row["zlocal"][2] * length

        length = element.length
        patch_start_x = element_x0
        patch_width = element_x1 - element_x0
        patch_start_y = -2 * magnet_width
        patch_height = 4 * magnet_width

        try:
            patch_height = copysign(patch_height * 0.5, element.polarity())
        except AttributeError:
            pass
        else:
            patch_start_y = 0  # patch_start_x

        rectx = patches.Rectangle(
            (patch_start_x, patch_start_y),
            patch_width,
            patch_height,
            linewidth=0.1,
            edgecolor="white",
            facecolor=colour,
            alpha=alpha,
        )
        axes.add_patch(rectx)

        if annotate:
            element_type = type(element).__name__

            annotation = axes.annotate(
                f"{element_type}: {element.name}",
                xy=(patch_start_x, 0),  # xycoords='data',
                xytext=(patch_start_x, 0),
                textcoords="data",
                horizontalalignment="left",
                arrowprops=dict(arrowstyle="simple", connectionstyle="arc3,rad=+0.2"),
                bbox=dict(boxstyle="round", facecolor="w", edgecolor="0.5", alpha=0.9),
                fontsize=18,
            )
            # by default, disable the annotation visibility
            annotation.set_visible(False)
            patch_ids_to_annotations[id(rectx)] = annotation
            patch_ids_to_elements[id(rectx)] = element
            rectx.set_picker(True)

    def on_pick(event):
        annotation = patch_ids_to_annotations[id(event.artist)]
        annotation.set_visible(not annotation.get_visible())
        fig.canvas.draw_idle()  # text_from_points=False
        element = patch_ids_to_elements[id(event.artist)]

        print(repr(element))

        # plt.draw()

    def on_press(event):
        if event.key == "c":  # press c to clear the annotations.
            for annotation in patch_ids_to_annotations.values():
                annotation.set_visible(False)
        fig.canvas.draw_idle()

    fig.canvas.mpl_connect("pick_event", on_pick)
    fig.canvas.mpl_connect("key_press_event", on_press)


def draw_line(axes, sequence, s_offset=0, **plotkw):
    survey = sequence.survey()

    s = np.concatenate(([0], survey["s"]))
    s += s_offset

    x = np.zeros_like(s)

    axes.plot(s, x, **plotkw)
    axes.set_ylim(-3, 3)


def draw_survey_line(axes, z, rcoord, **plotkw):
    axes.plot(z, rcoord, **plotkw)
