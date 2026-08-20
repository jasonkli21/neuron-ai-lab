from __future__ import annotations

import numpy as np
import pytest

from neuron_lab.lif import LIFParameters, simulate_lif
from neuron_lab.simulation import SimulationConfig
from neuron_lab.stimuli import step_current


def test_default_time_constant_and_rheobase() -> None:
    parameters = LIFParameters()

    assert parameters.membrane_time_constant_ms == pytest.approx(20.0)
    assert parameters.rheobase_na == pytest.approx(0.15)


def test_zero_current_stays_at_rest() -> None:
    config = SimulationConfig(duration_ms=100.0, dt_ms=0.1)
    parameters = LIFParameters()
    current_na = np.zeros(config.n_steps, dtype=np.float64)

    result = simulate_lif(parameters, config, current_na)

    assert result.voltage_mv == pytest.approx(parameters.resting_potential_mv)
    assert result.spike_count == 0


def test_subthreshold_current_approaches_analytical_steady_state() -> None:
    config = SimulationConfig(duration_ms=300.0, dt_ms=0.05)
    parameters = LIFParameters()
    amplitude_na = 0.1
    current_na = step_current(
        config,
        amplitude_na=amplitude_na,
        start_ms=0.0,
        stop_ms=config.duration_ms,
    )

    result = simulate_lif(parameters, config, current_na)
    expected_steady_state_mv = (
        parameters.resting_potential_mv + parameters.resistance_mohm * amplitude_na
    )

    assert result.spike_count == 0
    assert result.voltage_mv[-1] == pytest.approx(expected_steady_state_mv, abs=0.01)


def test_suprathreshold_current_produces_spikes() -> None:
    config = SimulationConfig(duration_ms=200.0, dt_ms=0.1)
    parameters = LIFParameters()
    current_na = step_current(
        config,
        amplitude_na=0.22,
        start_ms=20.0,
        stop_ms=180.0,
    )

    result = simulate_lif(parameters, config, current_na)

    assert result.spike_count > 0
    assert np.all(result.spike_times_ms >= 20.0)
    assert np.all(result.spike_times_ms < 180.0)


def test_refractory_period_sets_minimum_interspike_interval() -> None:
    config = SimulationConfig(duration_ms=100.0, dt_ms=0.05)
    parameters = LIFParameters(refractory_period_ms=4.0)
    current_na = step_current(
        config,
        amplitude_na=2.0,
        start_ms=0.0,
        stop_ms=config.duration_ms,
    )

    result = simulate_lif(parameters, config, current_na)
    interspike_intervals_ms = np.diff(result.spike_times_ms)

    assert result.spike_count > 2
    assert np.all(interspike_intervals_ms >= parameters.refractory_period_ms)


def test_current_shape_must_match_simulation() -> None:
    config = SimulationConfig(duration_ms=10.0, dt_ms=0.1)
    parameters = LIFParameters()

    with pytest.raises(ValueError, match="shape"):
        simulate_lif(parameters, config, np.zeros(5, dtype=np.float64))
