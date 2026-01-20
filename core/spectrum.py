"""
QuasiSpec™ Spectrum Generation Module

Provides functions to generate periodic and quasiperiodic resonant frequency spectra.
"""

import numpy as np

__version__ = "1.0.0"


def periodic_spectrum(f0, N):
    """
    Generate N uniformly spaced resonant frequencies.
    
    Parameters
    ----------
    f0 : float
        Base frequency (Hz)
    N : int
        Number of resonant modes
    
    Returns
    -------
    np.ndarray
        Array of N uniformly spaced frequencies
    """
    return f0 * np.arange(1, N + 1)


def quasiperiodic_spectrum(f0, N, ratio):
    """
    Generate N quasiperiodically spaced resonant frequencies
    using an irrational ratio.
    
    Parameters
    ----------
    f0 : float
        Base frequency (Hz)
    N : int
        Number of resonant modes
    ratio : float
        Irrational spacing ratio (e.g., golden ratio ≈ 1.618)
    
    Returns
    -------
    np.ndarray
        Array of N quasiperiodically spaced frequencies
    """
    return np.array([f0 * ratio**n for n in range(N)])
