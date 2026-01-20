# QuasiSpec™ Overview

## Problem Statement

Resonator-based systems with uniform (periodic) frequency spacing suffer from coherent resonance buildup. When multiple resonators are driven at or near their resonant frequencies, the uniform spacing causes harmonic alignment, leading to:

- **Spectral instability** – Coherent peaks at integer multiples
- **Broadband coupling** – Resonances reinforce each other
- **Difficult suppression** – Filtering becomes inefficient

## Solution: Quasiperiodic Spacing

By replacing uniform spacing with irrational (quasiperiodic) ratios, we break harmonic alignment:

- **Spectrum decorrelation** – No integer harmonic relationships
- **Distributed response** – Energy spreads across modes
- **Improved stability** – Reduced coherent buildup

## Mathematical Foundation

### Periodic Spectrum
```
f_n = f₀ × n,  n = 1, 2, 3, ...
```
Uniform spacing creates integer ratios: f₂/f₁ = 2, f₃/f₁ = 3, etc.

### Quasiperiodic Spectrum
```
f_n = f₀ × φⁿ,  n = 0, 1, 2, ...
```
Where φ (golden ratio ≈ 1.618) is irrational: no integer ratios exist.

## Key Metrics

### Spectral Overlap
Measures how closely resonances approach each other (assuming Lorentzian linewidths):
```
Overlap = Σ exp(-Δf / BW)
```
Lower values indicate better spectral separation.

### Coherence Metric
Quantifies commensurability via frequency ratios:
```
Coherence = StdDev(f_i / f_j)
```
Lower values indicate more irrational (less harmonic) spacing.

## Applications

| Domain | Benefit |
|--------|---------|
| RF Filters | Suppress spurious resonances |
| Power Electronics | Reduce harmonic coupling in LC tanks |
| Sensors | Improve stability in resonant arrays |
| Metamaterials | Design broadband absorbers |

---

For implementation details, see **[Quickstart](quickstart.md)**.
