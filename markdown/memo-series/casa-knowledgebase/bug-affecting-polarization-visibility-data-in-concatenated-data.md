

# Bug affecting polarization visibility data in concatenated data 

Knowledgebase Article: characterization of a bug that affected polarization visibility data in concatenated data in CASA versions up to 5.6.

**George Moellenbrock****Original 17 Apr 2020, latest edited version 12 May 2020**

 

CASA 5.7/6.1 fixed a bug in **concat** and **importfitsidi** that affected polarization visibility data in concatenated MSs. The problem that occurs in CASA versions earlier than 5.7/6.1 is that the cross-hands may be spuriously mis-ordered on a subset of baselines in the concatenated MS.This Knowledgebase Article describes the main effects that this bug has on concat\'d data in general, and in particular on the processing of ALMA and VLA data with CASA up to and including version 5.6.A careful analysis has revealed the following effects in concat\'d MSs in CASA versions prior to 5.7/6.1:1). *In general,* visibility data cross-hands may be spuriously swapped on some baselines in concat\'d data when the antenna lists in the input MSs are *partially* different.  The concat task adopts the first (in time order) MS\'s antenna list for the output MS, and appends unique antennas from later MS(s), typically with larger indices than in their original MSs.  Depending on the original antenna indexing, baselines between these additional antennas and antennas that did occur in the first MS may sometimes require conjugation (reversal of the order of antennas in the baseline) to maintain internal indexing consistency within the output MS (for all baselines in an MS, the first antenna must have an index which is lower than (or same as) the index of the second antenna).   When baselines are conjugated in this way, the sign of the phase of each correlation and the UVWs must be reversed, and the cross-hands swapped (RL or XY will become LR or YX, respectively, and vice-versa).  Prior to CASA 5.7/6.1, the sign reversals were correct, but the cross-hand swap was spuriously omitted.  For successfully calibrated data (i.e., calibrated *prior* to running concat), this means that the sign of the imaginary part of the cross-hand visibilities will be incorrect, and thus the sign Stokes U (for circular feeds) or Stokes V (for linear feeds) will be incorrect on the affected baselines in concat\'d data. Since the pathology affects only the cross-hands, polarimetry calibration of concat\'d data may be adversely affected. 

For reconfigurable arrays, note that an antenna\'s particular position (pad) makes it unique, i.e., a specific physical antenna that has moved is a new unique antenna in this context.  Concatenation of *entirely* disjoint antenna lists are unaffected, since all additional antennas in the concatenation will have uniformly incremented indices, and no baseline conjugation will be required.   Certain unique cases of different antenna lists are immune to this problem, e.g., new unique antennas with already-higher indices than all other common antennas, etc.2). The concat task initially sorts the MSs into time order (only at whole-MS granularity), so the effect cannot be controlled merely by adjusting the order in which the input MSs are specified in the concat call (i.e., there is no easy user-directed fix).

3). An implicit concat happens in importfitsidi (i.e., VLBI, typically) when specifying multiple FITS-IDI files. Here the antenna re-indexing occurs upon fill, and thus most-likely *before* calibration.  Since ordinary gain calibration uses only the parallel-hands, it will not be affected by the underlying cross-hand swap error.  However, polarimetry calibration will be affected to the extent that there are spuriously swapped cross-hands within the filled MS.  EVN observations consisting of multiple FITS-IDI will have the same antenna table in each file and are therefore unaffected by this bug.4). Since the pathology affects only the cross-hands, purely Stokes I (total intensity) observations of any kind should not be affected (even if the cross-hand are present and some are affected, and thus technically incorrect).

5). For ALMA and VLA data, calibration typically occurs prior to any potentially pathological use of concat, and the impact will be as follows:

5a). ALMA:  Total intensity observations of any kind are not affected.  For successfully calibrated (per session) ALMA polarization data not subject to this pathology in the concat of multiple contiguous execblocks within each session\*, the pathology affects only Stokes V (circular polarization) when concat-ing multiple sessions subject to the baseline conjugation conditions described in item 1 above.  This is because the spurious cross-hand swap effectively sabotages only the sign of the imaginary part of the cross-hands in some baselines, i.e., the apparent Stokes V signal sampled by linear feeds.  The net effect will be to suppress the net Stokes V signal in imaging.   This presumably affects only a very tiny minority of existing ALMA observations.

<div class="alert alert-info">
\* **Note:** In the course of standard scripted ALMA polarimetry calibration, the split task does not remove antennas from the ANTENNA subtable, even when they are fully flagged and keepflags=False.  The data rows are not retained in this case, but the ANTENNA subtable seen by concat remains complete.  Therefore, as long as the execblocks within the contiguous polarization session are uniform as regards to antenna population (as is intended), the polarization calibration within an individual session should not be subject to this this pathology.
</div>

5b). VLA: Total intensity observations of any kind are not affected.  For successfully calibrated VLA polarization observations (which typically do not require a prior concat), the pathology affects only Stokes U when concat-ing multiple observations subject to the baseline conjugation conditions described in item 1 above.  By the same logic as for ALMA, the Stokes U (cross-hand imaginary part for circular feeds) will be suppressed.  Since this affects part of the linearly polarized net response, a larger fraction of VLA cases (cf ALMA) may be affected.  The pathological condition arises when antennas are variously removed from the array (typically up to 2 or 3 at any given time) for incidental maintenance, so as to generate datasets with fewer than the full complement of 27 antennas, or when antennas move in and out of the barn (even when there are 27 antennas present in each observation), and when such disparate observations are concat\'d.    For concats of different VLA configurations, some baselines to antennas that did *not* move (typically \~12 out of 27 antennas) between the configurations will be affected, even if the total antenna lists (by name/number) have not changed.  This is because antennas that did move (only) are unique new antennas in the concat by virtue of their new positions, and some baselines between them and the stationary antennas must be conjugated in the concat. 

6). If observations are combined implicitly in imaging by specifying a list of MSs to tclean, there should be no problem, since the bug is an artifact of the mechanical combination of MSs into a single MS on disk.

 
