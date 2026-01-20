"""
QuasiSpec™ Core Module

Provides spectral generation, metrics, optimization, and Q-factor analysis.
"""

from .spectrum import periodic_spectrum, quasiperiodic_spectrum
from .metrics import spectral_overlap, coherence_metric
from .optimizer import optimize_ratio
from .qfactor import q_factor_simulation

__version__ = "1.0.0"

__all__ = [
    'periodic_spectrum',
    'quasiperiodic_spectrum',
    'spectral_overlap',
    'coherence_metric',
    'optimize_ratio',
    'q_factor_simulation',
]
