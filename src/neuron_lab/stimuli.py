"""Input-current generators.

All time values are in milliseconds and currents are in nanoamps.
"""

from __future__ import annotations

import numpy as np

from neuron_lab.simulation import FloatArray, SimulationConfig


def time_axis(config: SimulationConfig) -> FloatArray:
    """Create a stable time axis that uses the configured step size."""
    return np.arange(config.n_steps, dtype=np.float64) * config.dt_ms


def _validate_window(start_ms: float, stop_ms: float, duration_ms: float) -> None:
    if not np.isfinite(start_ms) or not np.isfinite(stop_ms):
        raise ValueError("stimulus times must be finite")
    if start_ms < 0:
        raise ValueError("start_ms must be non-negative")
    if stop_ms <= start_ms:
        raise ValueError("stop_ms must be greater than start_ms")
    if stop_ms > duration_ms:
        raise ValueError("stop_ms must not exceed the simulation duration")


def step_current(
    config: SimulationConfig,
    *,
    amplitude_na: float,
    start_ms: float,
    stop_ms: float,
) -> FloatArray:
    """Return a rectangular current step."""
    _validate_window(start_ms, stop_ms, config.duration_ms)
    if not np.isfinite(amplitude_na):
        raise ValueError("amplitude_na must be finite")

    t_ms = time_axis(config)
    current_na = np.zeros_like(t_ms)
    active = (t_ms >= start_ms) & (t_ms < stop_ms)
    current_na[active] = amplitude_na
    return current_na


def pulse_current(
    config: SimulationConfig,
    *,
    amplitude_na: float,
    pulse_starts_ms: list[float],
    pulse_width_ms: float,
) -> FloatArray:
    """Return one or more fixed-width current pulses."""
    if not np.isfinite(pulse_width_ms) or pulse_width_ms <= 0:
        raise ValueError("pulse_width_ms must be finite and positive")
    if not pulse_starts_ms:
        raise ValueError("pulse_starts_ms must contain at least one pulse")

    current_na = np.zeros(config.n_steps, dtype=np.float64)
    for start_ms in pulse_starts_ms:
        current_na += step_current(
            config,
            amplitude_na=amplitude_na,
            start_ms=start_ms,
            stop_ms=start_ms + pulse_width_ms,
        )
    return current_na


def sinusoidal_current(
    config: SimulationConfig,
    *,
    offset_na: float,
    amplitude_na: float,
    frequency_hz: float,
    start_ms: float = 0.0,
    stop_ms: float | None = None,
) -> FloatArray:
    """Return a sinusoidal current, optionally restricted to a time window."""
    effective_stop_ms = config.duration_ms if stop_ms is None else stop_ms
    _validate_window(start_ms, effective_stop_ms, config.duration_ms)

    if not all(np.isfinite(value) for value in (offset_na, amplitude_na, frequency_hz)):
        raise ValueError("sinusoidal current parameters must be finite")
    if frequency_hz < 0:
        raise ValueError("frequency_hz must be non-negative")

    t_ms = time_axis(config)
    current_na = np.zeros_like(t_ms)
    active = (t_ms >= start_ms) & (t_ms < effective_stop_ms)
    elapsed_seconds = (t_ms[active] - start_ms) / 1_000.0
    current_na[active] = offset_na + amplitude_na * np.sin(
        2.0 * np.pi * frequency_hz * elapsed_seconds
    )
    return current_na


def gaussian_noise_current(
    config: SimulationConfig,
    *,
    mean_na: float,
    std_na: float,
    seed: int,
) -> FloatArray:
    """Return reproducible independent Gaussian current samples."""
    if not np.isfinite(mean_na):
        raise ValueError("mean_na must be finite")
    if not np.isfinite(std_na) or std_na < 0:
        raise ValueError("std_na must be finite and non-negative")

    rng = np.random.default_rng(seed)
    return rng.normal(mean_na, std_na, size=config.n_steps).astype(np.float64)
