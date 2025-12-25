import numpy as np
from src.nonlinear_func import nonlinear_function
from src.sta import compute_sta

def compute_filtered_response(stim, sta): 
    T = len(sta)
    g = np.zeros((len(stim), ))

    for t in range(T, len(stim)):
        g[t] = np.dot(sta, stim[t - T: t])

    return g


def ln_model(stim, spikes, num_bins=30):
    sta = compute_sta(stim, spikes)
    g = compute_filtered_response(stim, sta)

    bin_centers, f = nonlinear_function(g, spikes, num_bins)

    return bin_centers, f

