# How each family was parameterised

| file | what it is |
|---|---|
| `ALL_FAMILIES.md` | All 46 design families the campaign proposed: the idea, its grounding, the free design variables with bounds, what was held fixed, and the verdict. |
| `SCRIPT_HEADER_D9_bowed.md` | The bowed-longeron generator's own module docstring, verbatim. Gives the geometry: `r(z) = r_taper(z) * (1 - bow_amplitude * sin(pi z/pitch))`. |
| `SCRIPT_HEADER_D42_serpentine.md` | The serpentine Stage-1 script's docstring, verbatim. Gives the grounding, and why it is not a re-run of the earlier radial-meander family. |

Two notes on reading `ALL_FAMILIES.md`.

**"Fixed:" is doing as much work as the bounds.** Most families hold `n_longerons=3`,
`n_storeys=1`, `ratio_shear_modulus=0.3677`; what a family chose to free is the design decision.

**The families are not independent.** Many are follow-ups to a previous family's failure, and
the `Grounding` line says so when they are.
