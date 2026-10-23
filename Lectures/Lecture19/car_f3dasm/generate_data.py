"""Generate the braking-distance experiments and store them in data/.

Each experiment is one driver:
  x : speed (m/s), Sobol sequence (seed 0) over [3, 82]
  z : individual reaction time, z ~ N(1.5, 0.5^2), drawn with seed 0
  y : stopping distance (m), y = z * x + 0.1 * x**2
"""

from pathlib import Path

import numpy as np
import pandas as pd
from f3dasm import ExperimentData
from f3dasm.design import Domain, sobol

HERE = Path(__file__).resolve().parent
N_DRIVERS = 30
SEED = 0

# 1) Sobol design over speeds
speed_domain = Domain()
speed_domain.add_float("x", low=3.0, high=82.0)
design = sobol(seed=SEED).call(ExperimentData(domain=speed_domain), n_samples=N_DRIVERS)
x = design.to_pandas()[0]["x"].to_numpy()

# 2) One reaction time per driver
rng = np.random.default_rng(SEED)
z = rng.normal(loc=1.5, scale=0.5, size=N_DRIVERS)

# 3) Stopping distance
y = z * x + 0.1 * x**2

# 4) Store as ExperimentData in data/
domain = Domain()
domain.add_float("x", low=3.0, high=82.0)
domain.add_float("z")
domain.add_output("y")

inputs = pd.DataFrame({"x": x, "z": z})
outputs = pd.DataFrame({"y": y})
data = ExperimentData(domain=domain, input_data=inputs, output_data=outputs)
data.store(project_dir=HERE / "data")

if __name__ == "__main__":
    print(pd.concat([inputs, outputs], axis=1).round(3).to_string())
