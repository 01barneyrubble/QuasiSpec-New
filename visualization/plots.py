"""
QuasiSpec™ Visualization Module

Generates publication-quality comparison plots for periodic vs quasiperiodic spectra.
"""

import numpy as np
import matplotlib.pyplot as plt

__version__ = "1.0.0"


def plot_spectrum_comparison(periodic_freqs, quasiperiodic_freqs, title="Spectrum Comparison"):
    """
    Generate side-by-side comparison plot of periodic vs quasiperiodic spectra.
    
    Parameters
    ----------
    periodic_freqs : np.ndarray
        Periodic spectrum frequencies
    quasiperiodic_freqs : np.ndarray
        Quasiperiodic spectrum frequencies
    title : str
        Plot title
    
    Returns
    -------
    fig, ax
        Matplotlib figure and axes objects
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    
    ax1.stem(range(len(periodic_freqs)), periodic_freqs, basefmt=' ')
    ax1.set_title('Periodic Spacing')
    ax1.set_xlabel('Mode Index')
    ax1.set_ylabel('Frequency (Hz)')
    ax1.grid(True, alpha=0.3)
    
    ax2.stem(range(len(quasiperiodic_freqs)), quasiperiodic_freqs, basefmt=' ')
    ax2.set_title('Quasiperiodic Spacing')
    ax2.set_xlabel('Mode Index')
    ax2.set_ylabel('Frequency (Hz)')
    ax2.grid(True, alpha=0.3)
    
    fig.suptitle(title, fontsize=14, fontweight='bold')
    plt.tight_layout()
    
    return fig, (ax1, ax2)


def plot_coherence_scan(ratio_range, coherence_values):
    """
    Plot coherence metric as function of spacing ratio.
    
    Parameters
    ----------
    ratio_range : np.ndarray
        Array of ratio values
    coherence_values : np.ndarray
        Corresponding coherence metrics
    
    Returns
    -------
    fig, ax
        Matplotlib figure and axes objects
    """
    fig, ax = plt.subplots(figsize=(10, 5))
    
    ax.plot(ratio_range, coherence_values, 'b-', linewidth=2)
    ax.set_xlabel('Spacing Ratio')
    ax.set_ylabel('Coherence Metric')
    ax.set_title('Coherence vs Spacing Ratio')
    ax.grid(True, alpha=0.3)
    
    return fig, ax
