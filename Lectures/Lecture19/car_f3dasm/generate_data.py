"""Generate the car braking-distance dataset with f3dasm.

Model: y = z * x + 0.1 * x**2
  x : speed (m/s), sampled in [3, 82] with the Sobol sampler (seed 0)
  z : reaction time (s), one per driver, z ~ N(1.5, 0.5**2)
  y : stopping distance (m)

Each row is one driver (one experiment). The result is stored as an
f3dasm ExperimentData in the folder ``data/``.
"""

from pathlib import Path

import numpy as np
import pandas as pd

from f3dasm import ExperimentData, create_sampler
from f3dasm.design import Domain

HERE = Path(__file__).parent
DATA_DIR = HERE / "data"
N_SAMPLES = 30
SEED = 0


def main() -> None:
    # 1) Sample speeds with the Sobol sampler on a 1-D domain.
    x_domain = Domain()
    x_domain.add_float("x", low=3.0, high=82.0)
    x_domain.add_output("y")
    empty = ExperimentData(domain=x_domain)
    sampler = create_sampler("sobol_sampler", seed=SEED)
    sampler.arm(empty)
    x_data = sampler.call(empty, n_samples=N_SAMPLES)
    x = x_data.to_pandas()[0]["x"].to_numpy()

    # 2) One reaction time per driver, z ~ N(1.5, 0.5^2).
    rng = np.random.default_rng(SEED)
    z = rng.normal(loc=1.5, scale=0.5, size=N_SAMPLES)

    # 3) Stopping distance.
    y = z * x + 0.1 * x**2

    # 4) Store as an ExperimentData in data/.
    domain = Domain()
    domain.add_float("x", low=3.0, high=82.0)
    domain.add_float("z")  # per-driver reaction time (unbounded normal draw)
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
