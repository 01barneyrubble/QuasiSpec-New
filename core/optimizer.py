"""
QuasiSpec™ Optimizer Module

Optimizes spacing ratios for spectral stability and resonance suppression.
"""

import numpy as np
from .metrics import coherence_metric

__version__ = "1.0.0"


def optimize_ratio(f0, N, ratio_range=(1.5, 2.0), steps=100):
    """
    Search for optimal irrational ratio within a given range.
    
    Parameters
    ----------
    f0 : float
        Base frequency (Hz)
    N : int
        Number of resonant modes
    ratio_range : tuple
        (min_ratio, max_ratio) search bounds
    steps : int
        Number of ratio values to evaluate
    
    Returns
    -------
    dict
        Dictionary with 'ratio', 'coherence', and 'spectrum' keys
    """
    ratios = np.linspace(ratio_range[0], ratio_range[1], steps)
    best_ratio = None
    best_coherence = float('inf')
    best_spectrum = None
    
    for ratio in ratios:
        spectrum = np.array([f0 * ratio**n for n in range(N)])
        coh = coherence_metric(spectrum)
        
        if coh < best_coherence:
            best_coherence = coh
            best_ratio = ratio
            best_spectrum = spectrum
    
    return {
        'ratio': best_ratio,
        'coherence': best_coherence,
        'spectrum': best_spectrum
    }
