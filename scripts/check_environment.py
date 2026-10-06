"""Small environment check; not a scientific experiment."""
from pathlib import Path
import os
import sys

root = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(root / ".mplconfig"))
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pytest

print("Python:", sys.version.split()[0])
print("NumPy:", np.__version__)
print("Matplotlib:", matplotlib.__version__)
print("pytest:", pytest.__version__)
rng = np.random.default_rng(20261005)
samples = rng.standard_normal(10000)
assert np.isfinite(samples).all()
fig, ax = plt.subplots(figsize=(6, 4))
ax.hist(samples, bins=50, density=True)
ax.set(title="Environment check: standard normal samples", xlabel="z", ylabel="Density")
output = root / "results" / "environment-check.png"
output.parent.mkdir(parents=True, exist_ok=True)
fig.tight_layout()
fig.savefig(output, dpi=150)
plt.close(fig)
print("Environment OK. Plot:", output)
