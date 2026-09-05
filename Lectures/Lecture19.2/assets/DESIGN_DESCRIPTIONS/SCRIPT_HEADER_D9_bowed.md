# D9 · Radially bowed longerons - generator header

Verbatim module docstring. Source file is 422 lines.

```
SupercompressibleBowedLongeronsDataGenerator
================================================
D011 additive design-family extension of SupercompressibleDataGenerator
(workspace/data_generator.py, this run's registered baseline oracle):
RADIALLY PRE-CURVED ("bowed") longerons. Instead of a straight (or
twist-helical) longeron running from the bottom ring to the top ring,
each longeron's radial distance from the mast's central axis now varies
smoothly with height z:

    r(z) = r_taper(z) * (1 - bow_amplitude * shape(z))

where r_taper(z) is the EXISTING linear taper (interpolating bottom
radius D1/2 to top radius D1*(1-ratio_top_diameter)/2, unchanged), and
shape(z) = sin(pi * z_local/pitch) is a symmetric function that is ZERO
at both the bottom and top ring of a storey and reaches its extremum
(peak=+1.0) at mid-height. bow_amplitude is a NEW free parameter;
bow_amplitude > 0 bows the longeron INWARD (r(z) < r_taper(z) at
mid-height) -- see the SIGN CONVENTION note below, this is a deliberate,
explicit deviation from the "+" sign in the task's illustrative formula,
chosen specifically so that "positive = inward" (the task's own stated
primary-hypothesis requirement) holds. Negative bow_amplitude bows
OUTWARD; trivially supported (same formula, no extra code), though the
primary/validated direction here is inward (bow_amplitude in [0, 0.20]).

THIS IS A SEPARATE FILE/CLASS FROM THE BASELINE ORACLE. It does not
modify workspace/data_generator.py or scripts/*.py in place (those remain
the live, currently-registered baseline evaluator that other concurrent
delegations may be using) -- instead it points at two NEW pre-processing
scripts (copies of the baseline's with an additive radial-bow geometry
patch) that live alongside this file's own scripts/ subfolder:

    scripts/supercompressible_lin_buckle_pretwist_bowed.py
    scripts/supercompressible_riks_pretwist_bowed.py

The post-processors are UNCHANGED and reused verbatim from the study's
scripts/ dir (they only parse results.pkl / U-field / strain data, never
reference longeron-path geometry).

Geometry patch (see the two pretwist scripts' own comment blocks for the
full derivation)
-----------------------------------------------------------------------
The baseline's joint-generation loop only ever samples EACH LONGERON at
the n_storeys+1 storey-boundary heights (for n_storeys=1: 2 points, the
bottom and top ring -- the longeron between them is geometrically a
single straight WirePolyLine edge, only mesh-refined into many B31
elements, not many geometrically distinct points). This is too coarse a
polyline to trace a smooth mid-height bow, so this extension replaces
that per-storey sampling with a FINE per-level sampling
(n_bow_subdiv levels per storey, default 40) while reusing the EXACT SAME
per-node (x, y) taper + twist_offset(z) formula as before, with one
additional multiplicative factor:

    aux3          = 2*pi*i/n_longerons + twist_offset(z)      [UNCHANGED]
    taper_factor  = 1 - min(z, transition_length_ratio*mast_height)
                        / mast_height * cone_slope             [UNCHANGED]
    bow_shape(z)  = sin(pi * z_local/pitch)   (z_local = height within
                    the CURRENT storey; 0 at each storey's bottom/top)
    radial_factor = taper_factor * (1 - bow_amplitude * bow_shape(z))
    (x, y)        = radial_factor * mast_radius * (cos(aux3), sin(aux3))

The named JOINT-<i_storey>-<i_vertex> sets used for boundary conditions
and inter-part couplings are assigned ONLY at the coarse storey-boundary
levels (bow_shape==0 there by construction) -- i.e. EXACTLY the same
physical points as the un-bowed baseline. Only the intermediate polyline
vertices (which the baseline never had) carry the bow.

SIGN CONVENTION (explicit deviation from the task's illustrative "+")
-----------------------------------------------------------------------
The task's illustrative formula r(z) = r_taper(z)*(1 + bow_amplitude*
shape(z)) uses shape(z) peaking at +1.0 and a "+" sign, but ALSO states
"positive bow_amplitude = bow INWARD (r(z) < r_taper(z) at mid-height)"
as the primary, required behavior. With a positive-peaked shape(z) these
two statements are mutually exclusive under a literal "+": +1 * positive
bow_amplitude can only INCREASE r(z), not decrease it. This generator
resolves the conflict in favor of the explicitly stated REQUIRED
behavior (positive=inward) by using "-" instead of "+":
    radial_factor = taper_factor * (1 - bow_amplitude * bow_shape(z))
bow_shape(z) itself is still exactly as specified (peak=+1.0 at
mid-height, zero at both ends) -- only the combining sign changed. This
is flagged explicitly here and in the delivery report's Retrospective.

Design variables (ADDITIVE on top of the baseline's -- see
workspace/data_generator.py's own docstring for all inherited ones)
-----------------------------------------------------------------------
bow_amplitude  : dimensionless, [0.0, 0.20] recommended domain (negative
                 values are also supported -- outward bow -- but are not
                 the validated/primary direction here).
n_bow_subdiv   : (advanced/internal, NOT part of the recommended search
                 domain) integer >= 2, number of fine polyline
                 subdivisions per storey used to approximate the smooth
                 bow curve; default 40, forwarded with a default so a
                 caller who never sets it still gets a fine polyline.

All other inputs (circular/cross-section mode, n_longerons, n_storeys,
twist_angle, ratio_pitch, ratio_top_diameter, ratio_shear_modulus, and the
per-mode cross-section ratios) are inherited unchanged from the baseline
and validated here fixed at the winning rectangular-profile family
(circular=2, ratio_a=0.009204, ratio_b=0.018754, ratio_pitch=0.601567,
ratio_top_diameter=0.037945, ratio_shear_modulus=0.3677, n_longerons=3,
n_storeys=1, twist_angle=0.0) -- twist_angle=0.0 for ALL validation runs
in this delegation. The bow patch is written to compose additively with a
nonzero twist_angle (both terms feed the SAME aux2/aux3/radial_factor
chain, independently), but THIS WAS NOT EMPIRICALLY VERIFIED here (no
nonzero-twist_angle + nonzero-bow_amplitude combination was run) due to
time budget -- flagged explicitly in the delivery report.

Outputs (identical names/semantics to the baseline)
-----------------------------------------------------------------------
sigma_crit, coilable, max_compressive_strain, max_local_strain -- see
workspace/data_generator.py's docstring; formula/semantics unchanged.
```
