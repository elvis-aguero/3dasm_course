"""Generate the car stopping-distance experiments with f3dasm.

Model: y = z * x + 0.1 * x**2 (metres), x = speed (m/s),
z = driver reaction time ~ N(1.5, 0.5**2), one z per driver (per experiment).
"""

from pathlib import Path

import numpy as np
import pandas as pd

from f3dasm import ExperimentData, create_sampler
from f3dasm.design import Domain

N_SAMPLES = 30
SEED = 0
PROJECT_DIR = Path(__file__).parent / "data"


def stopping_distance(x: np.ndarray, z: np.ndarray) -> np.ndarray:
    return z * x + 0.1 * x**2


def main() -> None:
    # Input domain: speed in [3, 82] m/s.
    domain = Domain()
    domain.add_float("x", low=3.0, high=82.0)

    # Sobol sampling of the speeds (seed 0).
    sampler = create_sampler("sobol_sampler", seed=SEED)
    sampled = sampler.call(
        data=ExperimentData(domain=domain), n_samples=N_SAMPLES
    )
    input_df, _ = sampled.to_pandas()
    x_values = input_df["x"].to_numpy(dtype=float)

    # One reaction time per driver, drawn from N(1.5, 0.5^2) with a fixed seed.
    rng = np.random.default_rng(SEED)
    z_values = rng.normal(loc=1.5, scale=0.5, size=N_SAMPLES)
    y_values = stopping_distance(x_values, z_values)

    # Store as an ExperimentData: x as input; z (per-driver) and y as outputs.
    data = ExperimentData(
        domain=domain,
        input_data=pd.DataFrame({"x": x_values}),
        output_data=pd.DataFrame({"z": z_values, "y": y_values}),
        project_dir=PROJECT_DIR,
    )
    data.store()
    print(f"Stored {N_SAMPLES} experiments in {PROJECT_DIR}")


if __name__ == "__main__":
    main()
