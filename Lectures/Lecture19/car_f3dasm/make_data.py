"""Generate the car stopping-distance experiment with f3dasm.

Speeds x (m/s) are drawn in [3, 82] with the Sobol sampler (seed 0).
Each of the 30 experiments is a different driver with their own reaction
time z ~ N(1.5, 0.5^2). The stopping distance is y = z * x + 0.1 * x**2 (m).
The result is stored as an ExperimentData project in data/.
"""

from pathlib import Path

import numpy as np
import pandas as pd
from f3dasm import ExperimentData
from f3dasm.design import Domain, sobol

HERE = Path(__file__).resolve().parent
DATA_DIR = HERE / "data"
N_DRIVERS = 30
SEED = 0


def main() -> None:
    # 1. Sobol-sample the speeds with f3dasm
    sampling_domain = Domain()
    sampling_domain.add_float("x", low=3.0, high=82.0)
    sampled = sobol(seed=SEED).call(
        ExperimentData(domain=sampling_domain), n_samples=N_DRIVERS
    )
    x = sampled.to_pandas()[0]["x"].to_numpy(dtype=float)

    # 2. One reaction time per driver
    rng = np.random.default_rng(SEED)
    z = rng.normal(loc=1.5, scale=0.5, size=N_DRIVERS)

    # 3. Stopping distance
    y = z * x + 0.1 * x**2

    # 4. Store as an ExperimentData in data/
    domain = Domain()
    domain.add_float("x", low=3.0, high=82.0)
    domain.add_float("z")  # per-driver reaction time (unbounded)
    domain.add_output("y")

    inputs = pd.DataFrame({"x": x, "z": z})
    outputs = pd.DataFrame({"y": y})
    data = ExperimentData(
        domain=domain,
        input_data=inputs,
        output_data=outputs,
        project_dir=DATA_DIR,
    )
    data.store()
    print(f"Stored {len(data)} experiments in {DATA_DIR}")


if __name__ == "__main__":
    main()
