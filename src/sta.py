import numpy as np

def compute_sta(stim, rho, num_timesteps):
    sta = np.zeros((num_timesteps, 1))
    spike_times = np.where(rho == 1)[0]
    spike_times = spike_times[spike_times >= num_timesteps]
    num_spikes = len(spike_times)
    print(f'Number of spikes considered for STA: {num_spikes}')

    for t in spike_times:
        sta += stim[t - num_timesteps: t]

    sta /= num_spikes

    return sta