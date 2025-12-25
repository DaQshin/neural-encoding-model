
import numpy as np

def nonlinear_function(r, spikes, num_bins=30):
    
    r_all = r
    r_spikes = r[spikes == 1]

    r_min = np.min(r_all)
    r_max = np.max(r_all)

    bins = np.linspace(r_min, r_max, num_bins + 1)
    bin_centers = (bins[:-1] + bins[1:]) / 2

    p_r, _ = np.histogram(r_all, bins=bins, density=True)
    p_r_given_spike, _ = np.histogram(r_spikes, bins=bins, density=True)

    eps = 1e-10
    p_r = p_r + eps
    
    f = p_r_given_spike / p_r

    return bin_centers, f