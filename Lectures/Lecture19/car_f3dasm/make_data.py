"""Generate the car stopping-distance experiment (30 drivers) into data/.

x : speed (m/s), Sobol design on [3, 82], seed 0
z : reaction time (s), one draw per driver, z ~ N(1.5, 0.5^2), seed 0
y : stopping distance (m) = z*x + 0.1*x**2
"""
import numpy as np
import pandas as pd
from f3dasm import ExperimentData
from f3dasm.design import Domain, sobol

N = 30
SEED = 0

# Sobol design over speed (seed 0)
design = Domain()
design.add_float("x", low=3.0, high=82.0)
x_df, _ = sobol(seed=SEED).call(ExperimentData(domain=design), n_samples=N).to_pandas()
x = x_df["x"].to_numpy()

# One reaction time per driver
rng = np.random.default_rng(SEED)
z = rng.normal(loc=1.5, scale=0.5, size=N)

y = z * x + 0.1 * x**2

domain = Domain()
domain.add_float("x", low=3.0, high=82.0)
domain.add_float("z", low=-np.inf, high=np.inf)
domain.add_float("y", low=-np.inf, high=np.inf)  # output, moved to output below

data = ExperimentData(
    domain=domain,
    input_data=pd.DataFrame({"x": x, "z": z}),
    output_data=pd.DataFrame({"y": y}),
    project_dir="data",
)
data.store(project_dir="data")
print(data)
