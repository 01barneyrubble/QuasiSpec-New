# QuasiSpec™ Quickstart

## Installation

```bash
pip install -r requirements.txt
```

## Basic Usage

### 1. Generate Periodic Spectrum

```python
from core.spectrum import periodic_spectrum
import numpy as np

f0 = 1e9  # 1 GHz
N = 10    # 10 modes

periodic = periodic_spectrum(f0, N)
print(periodic)
# Output: [1.e+09 2.e+09 3.e+09 ... 1.e+10]
```

### 2. Generate Quasiperiodic Spectrum

```python
from core.spectrum import quasiperiodic_spectrum

phi = 1.618  # Golden ratio
quasi = quasiperiodic_spectrum(f0, N, phi)
print(quasi)
# Output: [1.618e+09 2.618e+09 4.236e+09 ...]
```

### 3. Measure Coherence

```python
from core.metrics import coherence_metric

coh_periodic = coherence_metric(periodic)
coh_quasi = coherence_metric(quasi)

print(f"Periodic: {coh_periodic:.4f}")
print(f"Quasiperiodic: {coh_quasi:.4f}")
```

Lower coherence = better quasiperiodic spacing.

### 4. Optimize Ratio

```python
from core.optimizer import optimize_ratio

result = optimize_ratio(f0, N, ratio_range=(1.5, 2.0), steps=50)

print(f"Best ratio: {result['ratio']:.4f}")
print(f"Coherence: {result['coherence']:.4f}")
```

### 5. Visualize Results

```python
from visualization.plots import plot_spectrum_comparison

fig, axes = plot_spectrum_comparison(periodic, result['spectrum'])
fig.show()
```

## Next Steps

- See **[Theory Agnostic](theory_agnostic.md)** for practical design rules
- Check **[examples/](../examples/)** for real-world applications

---

**QuasiSpec™** – Pure engineering optimization.
