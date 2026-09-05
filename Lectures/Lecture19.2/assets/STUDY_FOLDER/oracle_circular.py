"""GOLD reference oracle: the circular Bessa family.

TRIMMED FOR TEACHING. Real code from bo/oracle_circular.py (353 lines), cut to the
shape of one evaluation. Elisions are marked; nothing has been rewritten.

WHAT ONE evaluate() CALL DOES
  Stage 1  supercompressible_lin_buckle_pretwist.py -> _pp   : eigenvalue, mode shape
  gate     coilable? if not, stop -- no Riks
  Stage 2  supercompressible_riks_pretwist.py -> _pp          : the full response
  reduce   bo/response_metrics.windowed_metrics                : the reported quantities
"""
import math, uuid, numpy as np

N_LONGERONS      = 3
BOTTOM_DIAMETER  = 100.0     # mm, D1
YOUNG_MODULUS    = 3500.0    # MPa, PLA
SLENDERNESS_MIN  = 10.0      # beam-theory validity gate
IMPERFECTION     = 0.0698    # rad; median of Bessa's lognormal(4 deg, 1.2 deg)
MAX_SOLVE_SECONDS = 600

# ... elided: scratch paths, script locations, output-contract checker.


def _nominal(force_n):
    return force_n * 1000.0 / ((math.pi * BOTTOM_DIAMETER ** 2 / 4.0) * N_LONGERONS)


def _infeasible(note, **kw):
    """A design with no MEASURED objective.

    sigma_peak is returned as NaN, deliberately, NOT as 0.0. It comes from the Stage-2
    response, so if Stage 2 was skipped or failed it is UNMEASURED. Returning 0.0 instead
    is what broke the first template check: 42 of 120 evaluations failed their Riks solve,
    so the surrogate was fitted through 42 artificial zeros scattered across a surface that
    is smooth in truth. The constraint channels below stay populated with definite values:
    they are what tells the optimiser this region is infeasible, and that is real even when
    the objective is not.
    """
    out = dict(status="ok", feasible=False, note=note,
               sigma_peak=float("nan"), sigma_eig=kw.pop("sigma_eig", 0.0),
               lb_coilable=0, riks_strain=0.0, max_local_strain=1.0,
               converged=0, riks_converged=0, timed_out=0)
    out.update(kw)
    return out


def evaluate(x, imperfection=None):
    """x = (ratio_d, ratio_pitch, ratio_top_diameter). Never raises: a failed solve is a
    result (converged=0), because a raising oracle stalls an async optimisation pool.
    """
    from abaqus2py import AbaqusSimulator
    ratio_d, ratio_pitch, ratio_top_diameter = (float(v) for v in x)

    # Purely geometric gate -- no solve. Cheapest possible rejection.
    slenderness = ratio_pitch / ratio_d
    if slenderness < SLENDERNESS_MIN:
        return _infeasible("prefilter: slenderness %.2f < %.1f (no solve run)"
                           % (slenderness, SLENDERNESS_MIN), slenderness=slenderness)

    params = dict(cross_section="circular", n_longerons=N_LONGERONS, n_storeys=1,
                  twist_angle=0.0, ratio_shear_modulus=0.3677,
                  young_modulus=YOUNG_MODULUS, bottom_diameter=BOTTOM_DIAMETER,
                  ratio_d=ratio_d, ratio_pitch=ratio_pitch,
                  ratio_top_diameter=ratio_top_diameter)

    # -- Stage 1: linear eigenvalue buckling -----------------------------------
    s1 = "lin_%s" % uuid.uuid4().hex
    try:
        sim1 = AbaqusSimulator(num_cpus=1, working_directory=str(SCRATCH),
                               max_waiting_time=MAX_STAGE1_SECONDS)
        sim1.run(py_file=str(LIN_PRE), post_py_file=str(LIN_POST),
                 simulation_parameters=dict(params, name=s1))
        r1 = _load(SCRATCH / s1)
    except Exception as exc:
        return _infeasible("stage1 failed: %r" % (exc,), slenderness=slenderness)

    sigma_eig = _nominal(float(np.asarray(r1["loads"])[0]))

    # -- the gate: no coiling, no Stage 2 --------------------------------------
    if int(r1["coilable"]) != 1:
        return _infeasible("not coilable (Stage 2 not run)",
                           sigma_eig=sigma_eig, slenderness=slenderness)

    # -- Stage 2: Riks arc-length post-buckling --------------------------------
    s2 = "riks_%s" % uuid.uuid4().hex
    p2 = dict(params, name=s2)
    p2["max_disps"]      = [float(v) for v in np.asarray(r1["max_disps"]).tolist()]
    p2["lin_buckle_odb"] = str(SCRATCH / s1 / JOB_LIN)
    p2["imperfection"]   = IMPERFECTION if imperfection is None else float(imperfection)

    # ... elided (~90 lines): the Stage-2 solve, and its failure handling. A timeout is
    # reported distinctly from a solver failure -- they mean different things for whether
    # a family is worth searching (too expensive vs numerically unable), and conflating
    # them hides the one fact that decides it.

    # -- reduce: window the response, return the reported quantities -----------
    # ... elided (~40 lines): windowed_metrics() over Stage-2 increments up to the 2%
    # local-strain crossing; returns sigma_peak, energy_absorbed, mcs_at_peak, feasibility.
