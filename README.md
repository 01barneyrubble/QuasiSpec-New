# QuasiSpec™

**Passive resonance suppression through quasiperiodic spectral spacing**

QuasiSpec™ is a design and analysis toolkit for engineers working with resonator-based systems. It enables the replacement of uniform frequency spacing with quasiperiodic (irrational) spacing to suppress coherent resonance buildup and spectral instability.

## Features

- **Generate periodic vs quasiperiodic spectra** – Compare uniform and irrational frequency distributions
- **Quantify spectral overlap and coherence** – Measure resonance coupling and commensurability
- **Optimize spacing ratios for stability** – Search for optimal irrational ratios
- **Export fabrication-ready frequency sets** – Generate production-grade specifications
- **Publication-quality plots** – Comparison graphs and coherence scans

## Applications

- **RF & microwave systems** – Suppress spurious resonances in filters and multiplexers
- **EMI / EMC mitigation** – Reduce coherent interference in multi-resonator designs
- **Sensors and instrumentation** – Improve stability in resonant sensor arrays
- **Power electronics** – Optimize LC tank networks for harmonic suppression
- **Metamaterials** – Design broadband absorbers with quasiperiodic resonance spacing

## Installation

```bash
pip install -r requirements.txt
```

## Quick Start

```python
import numpy as np
from core.spectrum import periodic_spectrum, quasiperiodic_spectrum
from core.metrics import coherence_metric

# Generate spectra
f0 = 1e9  # 1 GHz base frequency
N = 10    # 10 resonant modes

periodic = periodic_spectrum(f0, N)
quasiperiodic = quasiperiodic_spectrum(f0, N, ratio=1.618)  # Golden ratio

# Measure coherence
coh_periodic = coherence_metric(periodic)
coh_quasi = coherence_metric(quasiperiodic)

print(f"Periodic coherence: {coh_periodic:.4f}")
print(f"Quasiperiodic coherence: {coh_quasi:.4f}")
```

## Documentation

- **[Overview](docs/overview.md)** – Theory and design principles
- **[Quickstart](docs/quickstart.md)** – Step-by-step tutorial
- **[Theory Agnostic](docs/theory_agnostic.md)** – Practical implementation guide

## Examples

- **[LC Network Design](examples/lc_network.ipynb)** – Optimize LC tank spacing
- **[RF Resonators](examples/rf_resonators.ipynb)** – Multi-resonator filter design

## License

Copyright (c) 2026

Permission is hereby granted for personal and commercial use of this software as-is, without warranty of any kind.

---

**QuasiSpec™** – Pure engineering optimization.
