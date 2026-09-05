# D42 · Serpentine longeron - Stage-1 script header

Verbatim module docstring. Source file is 458 lines.

```
SERPENTINE LONGERON FAMILY (namespace='serpentine', added 2026-08-26, D003), Stage 1
(linear eigenvalue buckling) pre-processor.

GROUNDING. Shi, Huang, Yu & Li (2024), "Double-eigenvalue bifurcation and multistability
in serpentine strips" (see corpus). Their result: a serpentine (in-plane wavy) strip whose
cross-section is strongly ANISOTROPIC -- in-plane bending stiffness >> out-of-plane
bending/twisting stiffness -- does not simply deepen its own in-plane waviness under axial
load. Instead it buckles OUT OF its own planform plane via a coupled bend-twist mode (a
double-eigenvalue bifurcation of the two lowest-lying buckling loads), and remains stable
through large displacement. This is a genuinely different post-buckling energy channel from
a straight member's simple planar (in-plane) coiling curvature -- the mechanism this whole
study's incumbent families (circular, "elliptical"/RectangularProfile, every taper/pre-twist/
pre-coil variant) all share.

WHY THIS IS NOT A RE-TEST OF THE PRIOR "in-plane meander" IDEA (run 20260718T031519, H2,
namespace n/a, `scripts/supercompressible_lin_buckle_meander_fractal.py`'s single-order
ancestor): that family offset the centerline SINUSOIDALLY IN THE RADIAL DIRECTION -- i.e.
its wave lay IN the plane that ALSO contains the coiling bending direction (a straight
longeron's own natural in-plane bow is radial-tangential... no: Bessa's own weak-axis
convention bows TANGENTIALLY, and that meander family offset RADIALLY, i.e. transverse to
the natural coiling-bow direction but still coplanar with the mast axis and the chord). It
was found BARREN: local strain rose with amplitude and period count (opposite the
hypothesised direction), because a radial wave sits in the mast's own meridional
(axis-containing) plane and just adds extra curvature the coiling motion has to fight
through, with no cross-section anisotropy engineered to give it anywhere else to go.

THIS family is deliberately different in BOTH respects at once:
  1. GEOMETRY: the wave offsets in the TANGENTIAL direction (perpendicular to the mast's
     meridional plane), so the "wave plane" (spanned by the chord and the tangential
     direction) is NOT the plane containing the mast axis -- it is normal to the RADIAL
     direction, i.e. normal to the direction the mast's own coiling motion needs the
     longeron to bow INTO (a rocking mast coils by its longerons bowing inward/radially as
     the ring descends and rotates -- see PROBLEM_STATEMENT.md's "More background"). So the
     serpentine's own "in-plane" bending direction and the coiling motion's own preferred
     bending direction are DIFFERENT axes by construction, not coincident as in the prior
     meander family.
  2. CROSS-SECTION: a RectangularProfile (a=radial/local-1/OUT-of-plane, half-dim
     `ratio_a`; b=tangential/local-2/IN-plane, half-dim `ratio_b`) with `ratio_b > ratio_a`
     (wide-tangential, thin-radial) -- Shi et al.'s required anisotropy. In-plane bending
     (about the radial axis, curving the member within its own tangential-vertical wave
     plane) has I ~ a*b^3/12, LARGE when b>>a: the wave's own planform shape resists being
     bent flatter/sharper. Out-of-plane bending (about the tangential axis, i.e. RADIAL
     deflection -- exactly the direction ordinary coiling wants) has I ~ b*a^3/12, SMALL
     when a<<b, and torsion (open thin section, J ~ (1/3)*b*a^3) is smaller still. So the
     member is deliberately built to be COMPLIANT in exactly the direction (radial) that
     ordinary coiling already wants to bend it, and STIFF in the direction (tangential,
     its own planform) that a plain in-plane perturbation (the prior meander family) found
     unhelpful. Whether Shi et al.'s coupled bend-twist channel actually engages under this
     mast's own boundary conditions (kinematic ring coupling, contact) -- as opposed to the
     member simply coiling radially through its own soft axis exactly like an ordinary thin
     rectangular section would -- is the open question a campaign on this oracle answers; it
     is NOT assumed here.

GEOMETRY. Copied from supercompressible_lin_buckle_pretwist.py's "elliptical" cross-section
branch (RectangularProfile substitute for Abaqus's missing native ellipse -- see that file's
long NOTE for why) and from supercompressible_lin_buckle_meander_fractal.py's wave-insertion
technique (interior WirePolyLine points along a per-storey straight CHORD, offset
transversally by a sinusoid, N1_COSINES section orientation using a single reference vector
per longeron -- Abaqus parallel-transports it onto the plane normal to each element's own
local tangent, so this handles the curved path exactly as it already does for the meander/
helical families). The ONLY change from that technique: offset direction is TANGENTIAL
(`tangent_dir = z_hat x radial_dir`), not radial.

  offset(t) = amplitude_rel * D1 * sin(n_undulations * pi * t),   t in [0, 1]

`t=0`/`t=1` are the (unchanged) bottom/top ring-attachment joints -- offset(0)=offset(1)=0
for any integer `n_undulations`, so the ring attachment points and the kinematic ring
coupling are IDENTICAL to every other pretwist-family design, per the task brief.
`n_undulations` is a COUNT OF HALF-SINE LOBES (n_undulations=1: one hump; =2: two
opposite-sign humps; =3: three), matching the task's own "1-3 undulations" language and the
prior meander family's own `n_periods` convention (same formula, tangential instead of
radial offset).

FREE DESIGN PARAMETERS (this family), ALL REQUIRED:
    ratio_pitch, ratio_top_diameter   -- SAME meaning/bounds order as every other family.
    ratio_a       -- OUT-of-plane (radial) cross-section HALF-dimension / D1. Kept SMALL
                     (thin) to make radial bending/twisting compliant -- see module note.
    ratio_b       -- IN-plane (tangential) cross-section HALF-dimension / D1. Kept LARGE
                     (wide) relative to ratio_a to give the member its own strong in-plane
                     (planform) bending stiffness -- Shi et al.'s anisotropy requirement.
    amplitude_rel -- peak TANGENTIAL offset of the wave / D1.
    n_undulations -- integer 1-3, number of half-sine lobes along the chord.
Fixed for this family (see bo/D42_oracle_serpentine.py): n_longerons=3, n_storeys=1,
twist_angle=0.0, young_modulus=3500 MPa, bottom_diameter=100 mm, ratio_shear_modulus=0.3677.

A "SERPENTINE_APEX_0_PART" vertex Set is created on LONGERON-0's own first-wave-peak point
(t*=0.5/n_undulations, which by construction is EXACTLY grid index 8 of the 16-subdivisions-
per-half-lobe discretisation below, for every n_undulations) so the Riks pre-processor
(supercompressible_riks_serpentine.py) can request its displacement history -- the
out-of-plane/in-plane deflection-amplitude proxy for the Shi et al. mechanism (see that
file's own module docstring, and PROBLEM_STATEMENT.md's apples-to-apples clause). This file
(Stage 1, linear buckling) does not need the history request itself, but builds the SAME
Set so both stages' geometry (and this Set's node numbering) agree exactly.
```
