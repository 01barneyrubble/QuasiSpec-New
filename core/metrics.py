"""
QuasiSpec™ Metrics Module

Quantifies spectral properties: overlap, coherence, and stability measures.
"""

import numpy as np

__version__ = "1.0.0"


def spectral_overlap(freqs, bandwidth):
    """
    Quantify spectral overlap assuming Lorentzian linewidths.
    
    Parameters
    ----------
    freqs : np.ndarray
        Array of resonant frequencies
    bandwidth : float
        Linewidth parameter (Hz)
    
    Returns
    -------
    float
        Total spectral overlap (dimensionless)
    """
    overlap = 0.0
    for i in range(len(freqs)):
        for j in range(i + 1, len(freqs)):
            df = abs(freqs[i] - freqs[j])
            overlap += np.exp(-df / bandwidth)
    return overlap


def coherence_metric(freqs):
    """
    Measures commensurability via normalized frequency ratios.
    Lower values indicate better quasiperiodic spacing.
    
    Parameters
    ----------
    freqs : np.ndarray
        Array of resonant frequencies
    
    Returns
    -------
    float
        Coherence metric (standard deviation of frequency ratios)
    """
    ratios = []
    for i in range(len(freqs)):
        for j in range(i + 1, len(freqs)):
            ratios.append(freqs[i] / freqs[j])
    ratios = np.array(ratios)
    return np.std(ratios)
