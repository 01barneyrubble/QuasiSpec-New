# QuasiSpec™ Theory Agnostic Guide

## Practical Design Rules

You don't need to understand the math. Just follow these rules:

### Rule 1: Choose a Base Frequency
```python
f0 = 1e9  # Your lowest resonant frequency
```

### Rule 2: Pick an Irrational Ratio
Use one of these proven ratios:
- **Golden Ratio**: φ = 1.618 (most common)
- **Plastic Ratio**: ρ = 1.325
- **Silver Ratio**: δ = 2.414
- **Tribonacci**: τ ≈ 1.839

```python
ratio = 1.618  # Golden ratio
```

### Rule 3: Generate Frequencies
```python
from core.spectrum import quasiperiodic_spectrum

N = 10  # Number of resonators
freqs = quasiperiodic_spectrum(f0, N, ratio)
```

### Rule 4: Verify Stability
```python
from core.metrics import coherence_metric

coh = coherence_metric(freqs)
if coh < 0.3:  # Empirical threshold
    print("Good spacing!")
else:
    print("Try different ratio")
```

## Design Workflow

1. **Identify your resonator type** (LC tank, cavity, antenna, etc.)
2. **Measure or calculate resonant frequencies**
3. **Apply quasiperiodic spacing** using Rule 1-3
4. **Test in simulation or hardware**
5. **Iterate if needed**

## Common Mistakes

❌ **Using integer ratios** (e.g., 2.0, 3.0)
- These create harmonic alignment

✓ **Using irrational ratios** (e.g., 1.618, 1.325)
- These break harmonic alignment

❌ **Spacing too close together**
- Causes overlap and coupling

✓ **Spacing with adequate separation**
- Minimum 10% frequency difference recommended

## Troubleshooting

| Problem | Solution |
|---------|----------|
| High coherence metric | Try different ratio |
| Resonances still coupled | Increase frequency separation |
| Fabrication tolerance issues | Add ±2% margin to frequencies |

---

**QuasiSpec™** – Pure engineering optimization.
