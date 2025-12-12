import numpy as np
from matplotlib import pyplot as plt



def plot_data(
        timestamps: np.ndarray,
        data: np.ndarray,
        time_units: str = "a.u.",
) -> None:
    """
    Plots the given data against timestamps.

    :param timestamps: A numpy array of timestamps.
    :param data: A numpy array of data values corresponding to the timestamps.
    :param time_units: A string representing the units of time for the x-axis.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, data, marker='o', linestyle='-')
    plt.xlabel(f'Time ({time_units})')
    plt.ylabel('Data Values')
    plt.title('Data vs Time')
    plt.grid(True)
    plt.show()


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

    timestamps = np.arange(0, duration, 1/frame_rate)
    spikes = np.random.poisson(1e-2, (len(timestamps), num_neurons))
    calcium_data = _spikes_to_traces(spikes, tau, 1/frame_rate)
    return np.hstack([timestamps.reshape(-1, 1), calcium_data])


# def simulate_raw_calcium(
#     X: int,
#     T: int,
#     dt: float = 1/30,                 # seconds per frame
#     rate_hz: tuple[float, float] = (0.02, 1.0),
#     tau_rise: float = 0.06,           # s
#     tau_decay: float = 0.7,           # s
#     amp: tuple[float, float] = (0.6, 2.0),
#     shared_event_rate_hz: float = 0.15,
#     shared_event_gain: tuple[float, float] = (0.0, 2.0),
#     seed: int = 0,
# ) -> tuple[np.ndarray, np.ndarray]:
#     """
#     Returns:
#       time_s: (T,) timestamps in seconds
#       calcium: (X, T) raw (latent) calcium traces (a.u.)
#     """
#     rng = np.random.default_rng(seed)
#     time_s = np.arange(T, dtype=np.float32) * np.float32(dt)
#
#     # baseline firing rates and shared event gains
#     rates = rng.uniform(*rate_hz, size=X).astype(np.float32)
#     gains = rng.uniform(*shared_event_gain, size=X).astype(np.float32)
#
#     # shared population events
#     shared_events = (rng.random(T) < (shared_event_rate_hz * dt)).astype(np.float32)  # (T,)
#     shared_hazard = gains[:, None] * shared_events[None, :]                            # (X,T)
#
#     # spikes per frame (Bernoulli approx to Poisson)
#     base_spikes = rng.random((X, T)) < (rates[:, None] * dt)
#     shared_spikes = rng.random((X, T)) < np.clip(shared_hazard * dt, 0.0, 0.95)
#     spikes = (base_spikes | shared_spikes).astype(np.float32)
#
#     # calcium dynamics: difference-of-exponentials via two IIR filters
#     alpha_r = float(np.exp(-dt / max(tau_rise, 1e-6)))
#     alpha_d = float(np.exp(-dt / max(tau_decay, 1e-6)))
#
#     r = np.zeros((X, T), dtype=np.float32)
#     c = np.zeros((X, T), dtype=np.float32)
#
#     for t in range(1, T):
#         r[:, t] = alpha_r * r[:, t - 1] + spikes[:, t]
#         c[:, t] = alpha_d * c[:, t - 1] + (1 - alpha_r) * r[:, t]
#
#     # per-neuron amplitude scaling
#     a = rng.uniform(*amp, size=X).astype(np.float32)
#     calcium = (a[:, None] * c).astype(np.float32)
#
#     return time_s, calcium
#
#
# # Example
# if __name__ == "__main__":
#     time_s, calcium = simulate_raw_calcium(X=100, T=3000, dt=1/30, seed=1)
#     print(time_s.shape, calcium.shape)
