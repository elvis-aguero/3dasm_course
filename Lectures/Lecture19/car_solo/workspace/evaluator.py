from pathlib import Path
import numpy as np

rng = np.random.default_rng()

def evaluate(x: float) -> float:
    """One new driver at speed x (m/s): the stopping distance in m."""
    y = rng.normal(1.5, 0.5) * x + 0.1 * x ** 2
    with open(Path(__file__).parent / "calls.csv", "a") as f: # keep a record of every call
        f.write(f"{x},{y}\n")
    return float(y)
