import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from pathlib import Path

_RED = (197/255, 89/255, 94/255)
_BLUE = (72/255, 136/255, 170/255)

def plot_neuron(
        timestamps: np.ndarray,
        data: np.ndarray,
        neuron: str | int  = "0",
        time_units: str = "a.u.",
) -> None:
    """
    Plots the given data against timestamps.

    :param timestamps: A numpy array of timestamps.
    :param data: A numpy array of data values corresponding to the timestamps.
    :param time_units: A string representing the units of time for the x-axis.
    """
    fig, ax = plt.subplots(1, 1, figsize=(5, 3))
    ax.plot(timestamps, data, color=_BLUE, lw=1.5, label="Neuron 0")
    ax.set_xlabel(f'Time ({time_units})')
    ax.set_ylabel('Calcium Signal (a.u.)')
    ax.set_title(f'Neuron {neuron}')
    ax.xaxis.set_major_locator(plt.MultipleLocator(10))
    ax.xaxis.set_minor_locator(AutoMinorLocator(2))
    ax.yaxis.set_major_locator(plt.MultipleLocator(0.25))
    ax.yaxis.set_minor_locator(AutoMinorLocator(2))
    max_stamp =np.ceil(timestamps.max())
    x_bounds = (0, max_stamp)
    x_lim = (-0.025 * max_stamp, max_stamp)
    ax.set_xlim(*x_lim)
    ax.spines["bottom"].set_bounds(*x_bounds)
    step = 0.25
    rounded_peak = np.ceil(data.max()/step)*step
    y_bounds = (0, rounded_peak)
    y_lim = (-0.025 * rounded_peak, rounded_peak)
    ax.set_ylim(*y_lim)
    ax.spines["left"].set_bounds(*y_bounds)
    ax.grid(visible=False)
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)



def _spikes_to_traces(
        spikes: np.ndarray,
        tau: tuple[float, float],
        dt: float,
) -> np.ndarray:
    num_frames, num_neurons = spikes.shape
    traces = np.zeros((num_frames, num_neurons))

    tau_rise, tau_decay = tau

    alpha_rise = np.exp(-dt / tau_rise)
    alpha_decay = np.exp(-dt / tau_decay)

    for n in range(num_neurons):
        r = 0
        c = 0
        for t in range(num_frames):
            r = alpha_rise * r + spikes[t, n]
            c = alpha_decay * c + (1 - alpha_rise) * r
            traces[t, n] = c

    return traces


def simulate_calcium_data(
        num_neurons: int,
        duration: int = 30,
        frame_rate: int = 30,
        tau: tuple[float, float] = (0.06, 0.7),
) -> np.ndarray:

    """
    Simulates calcium imaging data for a given number of neurons over a specified duration.

    :param num_neurons: Number of neurons to simulate.
    :param duration: Duration of the simulation in seconds.
    :param frame_rate: Frame rate in Hz.
    :param tau: Tuple containing rise and decay time constants.

    :return: A numpy array of shape (num_neurons, num_frames) representing the simulated calcium data.
    """

    timestamps = np.arange(1/frame_rate, duration + 1/frame_rate, 1/frame_rate)
    spikes = np.random.poisson(1e-2, (len(timestamps), num_neurons))
    calcium_data = _spikes_to_traces(spikes, tau, 1/frame_rate)
    return np.hstack([timestamps.reshape(-1, 1), calcium_data])


if __name__ == "__main__":
    num_neurons = 10
    duration = 60  # seconds
    frame_rate = 30  # Hz

    simulated_data = simulate_calcium_data(num_neurons, duration, frame_rate)

    timestamps = simulated_data[:, 0]
    data = simulated_data[:, 1]

    np.save(Path("simulated_calcium_data.npy"), simulated_data)