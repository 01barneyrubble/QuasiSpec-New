"""
QuasiSpec™ Q-Factor Module

Simulates quality factor and resonance stability for periodic vs quasiperiodic spacing.
"""

import numpy as np

__version__ = "1.0.0"


def q_factor_simulation(freqs, bandwidth, excitation_freq):
    """
    Simulate quality factor and resonance response at excitation frequency.
    
    Parameters
    ----------
    freqs : np.ndarray
        Array of resonant frequencies
    bandwidth : float
        Linewidth parameter (Hz)
    excitation_freq : float
        Driving frequency (Hz)
    
    Returns
    -------
    dict
        Dictionary with 'response', 'peak_q', and 'stability' keys
    """
    response = np.zeros_like(freqs, dtype=float)
    
    for i, f in enumerate(freqs):
        q = f / bandwidth
        detuning = abs(excitation_freq - f) / bandwidth
        response[i] = q / (1.0 + detuning**2)
    
    peak_q = np.max(response)
    stability = 1.0 / (np.std(response) + 1e-10)
    
    return {
        'response': response,
        'peak_q': peak_q,
        'stability': stability
    }


def q_stability(freqs, Q0):
    """
    Simulate effective Q degradation due to spectral crowding.
    
    Parameters
    ----------
    freqs : np.ndarray
        Array of resonant frequencies
    Q0 : float
        Baseline quality factor
    
    Returns
    -------
    float
        Effective Q factor accounting for spectral crowding
    """
    crowding = np.sum(1 / np.diff(np.sort(freqs)))
    return Q0 / (1 + 0.01 * crowding)
