"""SupercompressibleDataGenerator -- the f3dasm side of the oracle.

TRIMMED FOR TEACHING. Real code from workspace/data_generator.py (3,966 lines), cut to
the f3dasm contract and one evaluation path. Elisions are marked; nothing is rewritten.

This is the file the agent WRITES. config.yaml only points at it:

    evaluator:
      entrypoint: "workspace/data_generator.py:SupercompressibleDataGenerator"

Everything f3dasm requires of an evaluator is here: subclass DataGenerator, declare
output_names, implement execute(sample) -> sample. The 3,900 lines it grew to are
18 cross-section families, admissibility guards, retries and partial-solve salvage.
"""
import os
from typing import Any, Optional
from f3dasm import DataGenerator, ExperimentSample

_YOUNG_MODULUS   = 3500.0    # MPa
_BOTTOM_DIAMETER = 100.0     # mm
_RATIO_SHEAR_MODULUS_GUARD = 0.0   # below this, nu >= 0.5 and Abaqus refuses the material


class SupercompressibleDataGenerator(DataGenerator):
    """f3dasm DataGenerator for the supercompressible-metamaterial benchmark.

    Two-stage Abaqus oracle: Stage 1 linear-eigenvalue buckling (always run)
    determines ``sigma_crit`` and ``coilable``; Stage 2 Riks arc-length
    post-buckling (only if ``coilable==1``) determines
    ``max_compressive_strain`` and ``max_local_strain``.
    """

    output_names = ["sigma_crit", "coilable",
                    "max_compressive_strain", "max_local_strain"]
    # ... elided: 20+ further outputs (energy_absorbed, riks_converged, timed_out,
    # slenderness, ring_passthrough, odb paths, note).

    def __init__(self, max_waiting_time_stage1: int = 600,
                 max_waiting_time_stage2: int = 5400,
                 n_retries: int = 3, n_retries_stage2: int = 2,
                 retry_backoff_s: float = 15.0,
                 scratch_base: Optional[str] = None):
        os.environ.setdefault("LANG", "en_US.UTF-8")
        # ... elided: stall detection, scratch resolution, and a long comment recording
        # why stage-2 waiting time went 900s -> 5400s (the solver was not diverging; the
        # gap between 188s CPU and 893s wallclock was shared-filesystem I/O).

    def execute(self, experiment_sample: ExperimentSample, **kwargs) -> ExperimentSample:
        d = experiment_sample.input_data

        # Admissibility guard: an inadmissible design is stored as NaN, never solved.
        ratio_shear_modulus = float(d.get("ratio_shear_modulus", 0.3677))
        if ratio_shear_modulus <= _RATIO_SHEAR_MODULUS_GUARD:
            return self._nan_sample(experiment_sample)

        cross_section = _CROSS_SECTION_BY_MODE[int(round(float(d.get("circular", 1.0))))]

        common: dict[str, Any] = dict(
            cross_section=cross_section,
            n_longerons=int(round(float(d.get("n_longerons", 3.0)))),
            n_storeys=int(round(float(d.get("n_storeys", 1.0)))),
            twist_angle=float(d.get("twist_angle", 0.0)),
            ratio_pitch=float(d["ratio_pitch"]),
            ratio_top_diameter=float(d["ratio_top_diameter"]),
            ratio_shear_modulus=ratio_shear_modulus,
            young_modulus=_YOUNG_MODULUS, bottom_diameter=_BOTTOM_DIAMETER,
        )
        if cross_section == "circular":
            common["ratio_d"] = float(d["ratio_d"])
        elif cross_section == "elliptical":
            common["ratio_a"], common["ratio_b"] = float(d["ratio_a"]), float(d["ratio_b"])
        # ... elided (~600 lines): 16 further cross-section families, each with its own
        # required parameters and its own geometric admissibility guard.

        # ... elided (~250 lines): Stage 1 dispatch, the coilability gate, Stage 2
        # dispatch, retry/backoff, and salvage of a partial Riks solve.

        # f3dasm's contract: put the outputs back on the sample and return it.
        # ... elided: experiment_sample.store(...) for each name in output_names.
        return experiment_sample
