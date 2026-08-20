"""Leaky integrate-and-fire neuron.

Unit convention:
    time: milliseconds
    voltage: millivolts
    current: nanoamps
    resistance: megaohms
    capacitance: nanoFarads

With these units:
    MΩ * nA = mV
    MΩ * nF = ms
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from neuron_lab.simulation import FloatArray, IntArray, SimulationConfig
from neuron_lab.stimuli import time_axis


@dataclass(frozen=True, slots=True)
class LIFParameters:
    """Biophysical and event parameters for the LIF model."""

    resting_potential_mv: float = -65.0
    reset_potential_mv: float = -65.0
    threshold_mv: float = -50.0
    resistance_mohm: float = 100.0
    capacitance_nf: float = 0.2
    refractory_period_ms: float = 2.0
    initial_potential_mv: float | None = None

    def __post_init__(self) -> None:
        finite_values = {
            "resting_potential_mv": self.resting_potential_mv,
            "reset_potential_mv": self.reset_potential_mv,
            "threshold_mv": self.threshold_mv,
            "resistance_mohm": self.resistance_mohm,
            "capacitance_nf": self.capacitance_nf,
            "refractory_period_ms": self.refractory_period_ms,
        }
        for name, value in finite_values.items():
            if not np.isfinite(value):
                raise ValueError(f"{name} must be finite")

        if self.initial_potential_mv is not None and not np.isfinite(self.initial_potential_mv):
            raise ValueError("initial_potential_mv must be finite when provided")
        if self.resistance_mohm <= 0:
            raise ValueError("resistance_mohm must be positive")
        if self.capacitance_nf <= 0:
            raise ValueError("capacitance_nf must be positive")
        if self.refractory_period_ms < 0:
            raise ValueError("refractory_period_ms must be non-negative")
        if self.reset_potential_mv >= self.threshold_mv:
            raise ValueError("reset_potential_mv must be below threshold_mv")
        if self.resting_potential_mv >= self.threshold_mv:
            raise ValueError("resting_potential_mv must be below threshold_mv")

    @property
    def membrane_time_constant_ms(self) -> float:
        """Return τ_m = R_m C_m."""
        return self.resistance_mohm * self.capacitance_nf

    @property
    def rheobase_na(self) -> float:
        """Passive current at which steady-state voltage reaches threshold.

        This is an asymptotic threshold estimate, not a guarantee of a spike
        for a finite-duration stimulus.
        """
        return (self.threshold_mv - self.resting_potential_mv) / self.resistance_mohm

    @property
    def starting_potential_mv(self) -> float:
        if self.initial_potential_mv is None:
            return self.resting_potential_mv
        return self.initial_potential_mv


@dataclass(frozen=True, slots=True)
class LIFResult:
    """Recorded output from a LIF simulation."""

    time_ms: FloatArray
    voltage_mv: FloatArray
    input_current_na: FloatArray
    spike_indices: IntArray
    spike_times_ms: FloatArray
    parameters: LIFParameters
    config: SimulationConfig

    @property
    def spike_count(self) -> int:
        return int(self.spike_times_ms.size)

    @property
    def firing_rate_hz(self) -> float:
        duration_seconds = self.config.duration_ms / 1_000.0
        return self.spike_count / duration_seconds


def simulate_lif(
    parameters: LIFParameters,
    config: SimulationConfig,
    input_current_na: FloatArray,
) -> LIFResult:
    """Simulate a LIF neuron with forward Euler integration.

    The recorded threshold point marks a spike event. On following samples,
    voltage is held at the reset potential during the absolute refractory
    period. This is not a biophysical action-potential waveform.
    """
    current = np.asarray(input_current_na, dtype=np.float64)
    if current.shape != (config.n_steps,):
        raise ValueError(
            f"input_current_na must have shape ({config.n_steps},), got {current.shape}"
        )
    if not np.all(np.isfinite(current)):
        raise ValueError("input_current_na must contain only finite values")

    t_ms = time_axis(config)
    voltage_mv = np.empty(config.n_steps, dtype=np.float64)
    voltage_mv[0] = parameters.starting_potential_mv

    spike_indices: list[int] = []
    refractory_until_ms = -np.inf
    tau_ms = parameters.membrane_time_constant_ms

    for index in range(1, config.n_steps):
        current_time_ms = t_ms[index]

        if current_time_ms < refractory_until_ms:
            voltage_mv[index] = parameters.reset_potential_mv
            continue

        previous_voltage_mv = voltage_mv[index - 1]
        if previous_voltage_mv >= parameters.threshold_mv:
            previous_voltage_mv = parameters.reset_potential_mv

        dv_dt_mv_per_ms = (
            parameters.resting_potential_mv
            - previous_voltage_mv
            + parameters.resistance_mohm * current[index - 1]
        ) / tau_ms
        candidate_voltage_mv = previous_voltage_mv + config.dt_ms * dv_dt_mv_per_ms

        if candidate_voltage_mv >= parameters.threshold_mv:
            voltage_mv[index] = parameters.threshold_mv
            spike_indices.append(index)
            refractory_until_ms = current_time_ms + parameters.refractory_period_ms
        else:
            voltage_mv[index] = candidate_voltage_mv

    spike_index_array = np.asarray(spike_indices, dtype=np.int64)
    spike_times_ms = t_ms[spike_index_array]

    return LIFResult(
        time_ms=t_ms,
        voltage_mv=voltage_mv,
        input_current_na=current.copy(),
        spike_indices=spike_index_array,
        spike_times_ms=spike_times_ms,
        parameters=parameters,
        config=config,
    )
