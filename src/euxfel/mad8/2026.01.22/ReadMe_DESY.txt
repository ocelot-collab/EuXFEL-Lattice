
**** Mad 8.51.18 **** 
**** Mar-31-2009 **** 

This package provides mad8 i386 executables for windows and linux.

To run this under windows it is necessary to set the DICT environment variable to 
your mad8.dict file. For more information visit the mad 8 for windows homepage (1).

**** files **** 

ReadMe_DESY.txt                     - this file
dict                                - necessary dictionary (copy)
mad8.dict                           - necessary dictionary
mad8.exe                            - mad 8 executable for windows
mad8s                               - mad 8 executable for linux (cosmos)

**** versions **** 
Mar-31-2009:
  New package released
  
Jan-19-2009, W.Decking(DESY), Mad 8.51.18:
  Changed subroutine flseq to support longer sequence names
  
03-APR-2008, M. Vogt (DESY), Mad 8.51.17:
  Modified OPTICS command (twopsv,twoptc) to use LACAV properly;
  Modifed tmlcav routine;

Feb-21-2007:
  this is the first version
  package build by S. Meykopff (DESY)
  This mad version includes a patch from W. Decking (DESY). It implements an exact Rosenzweig-Serrafin 
  Matrix to be consistent with elegant at low energies.  
  
**** more information **** 
  
(1) Mad 8 for windows homepage:
http://project-madwindows.web.cern.ch/project-madwindows/MAD-8/default.htm


**** local notes (EuXFEL-Lattice repository) ****

2026-07-31, TWISS_T5D re-run:
  The original TWISS_T5D was generated with `couple` on its twiss command
  (Run_South_2025.txm:260).  That is the only one of the seven twiss calls that
  had it, and it scaled T5D's dispersion by E/E_ref -- leaving DX a factor 26
  below every other path over the 6526 elements they share with T5D, and
  suppressing DY through the SASE2 extraction to ~0 despite 1.08 mrad of
  vertical bending there.

  W. Decking re-ran the south branch with that flag removed.  Run_South_2025.txm
  and tapes/TWISS_T5D.gz are the corrected versions; SURVEY_T5D is byte-identical
  to the original, as expected -- `couple` affects optics only, never geometry --
  and Run_North_2025.txm is unchanged, so no other target is affected.

  After the correction T5D's DX agrees with T4D's to 1e-17 and its DY with TLD's
  to 1e-16 across the shared injector and linac.  tests/test_mad8_convert.py
  checks Dy across every module boundary as a result; before it could not.
