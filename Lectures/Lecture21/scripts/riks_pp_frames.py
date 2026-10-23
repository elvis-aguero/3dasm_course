"""Riks post-processing for the no-contact runs: the history of the top reference point (as riks_pp_diag.py), and
per frame the load proportionality factor, U3 of the top reference point and the largest |E11| in the longerons, so
that the strain check can be restricted to the frames up to full compression."""

import pickle

import numpy as np
from abaqus import session  # NOQA


def main(odb):
    riks_results = {}
    step = odb.steps["RIKS_STEP"]
    nodes = odb.rootAssembly.nodeSets["ZTOP_REF_POINT"].nodes[0]
    node = nodes[0]
    instance_name = node.instanceName if node.instanceName else "ASSEMBLY"
    historyOutputs = step.historyRegions["Node " + instance_name + "." + str(node.label)].historyOutputs
    for variable in ["U", "UR", "RF", "RM"]:
        riks_results[variable] = np.array(
            [[d[1] for d in historyOutputs["%s%i" % (variable, k)].data] for k in (1, 2, 3)
             if "%s%i" % (variable, k) in historyOutputs.keys()])

    ref = odb.rootAssembly.nodeSets["ZTOP_REF_POINT"]
    longerons = odb.rootAssembly.instances["LONGERONS"].elementSets["ALL_LONGERONS"]
    lpf, u3, peak = [], [], []
    for frame in step.frames:
        lpf.append(frame.frameValue)
        try:
            u3.append(frame.fieldOutputs["U"].getSubset(region=ref).values[0].data[2])
        except Exception:
            u3.append(np.nan)
        p = np.nan
        try:
            p = max(abs(v.data[0]) for v in frame.fieldOutputs["E"].getSubset(region=longerons).values)
        except Exception:
            pass
        peak.append(p)
    riks_results["frame_lpf"] = np.array(lpf, float)
    riks_results["frame_u3"] = np.array(u3, float)
    riks_results["frame_strain"] = np.array(peak, float)
    finite = [p for p in peak if p == p]
    riks_results["max_local_strain"] = float(max(finite)) if finite else None

    for key in ("ALLSD", "ALLSE"):  # stabilized static step only
        riks_results[key] = None
        for region_name in step.historyRegions.keys():
            h = step.historyRegions[region_name].historyOutputs
            if key in h.keys():
                riks_results[key] = np.array([d[1] for d in h[key].data], float)
                break

    with open("results.pkl", "wb") as file:
        pickle.dump(riks_results, file)
