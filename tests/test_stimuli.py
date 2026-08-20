from __future__ import annotations

import numpy as np
import pytest

from neuron_lab.simulation import SimulationConfig
from neuron_lab.stimuli import pulse_current, step_current, time_axis


def test_time_axis_includes_zero_and_uses_dt() -> None:
    config = SimulationConfig(duration_ms=10.0, dt_ms=0.1)

    t_ms = time_axis(config)

    assert t_ms[0] == pytest.approx(0.0)
    assert t_ms[-1] == pytest.approx(10.0)
    assert np.diff(t_ms) == pytest.approx(0.1)


def test_step_current_uses_half_open_window() -> None:
    config = SimulationConfig(duration_ms=10.0, dt_ms=1.0)

    current_na = step_current(
        config,
        amplitude_na=0.25,
        start_ms=2.0,
        stop_ms=5.0,
    )

    assert current_na.tolist() == [0.0, 0.0, 0.25, 0.25, 0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]


def test_pulse_current_combines_multiple_pulses() -> None:
    config = SimulationConfig(duration_ms=10.0, dt_ms=1.0)

    current_na = pulse_current(
        config,
        amplitude_na=0.1,
        pulse_starts_ms=[1.0, 5.0],
        pulse_width_ms=2.0,
    )

    assert current_na.tolist() == [0.0, 0.1, 0.1, 0.0, 0.0, 0.1, 0.1, 0.0, 0.0, 0.0, 0.0]


def test_invalid_step_window_is_rejected() -> None:
    config = SimulationConfig(duration_ms=10.0, dt_ms=0.1)

    with pytest.raises(ValueError, match="stop_ms"):
        step_current(config, amplitude_na=0.1, start_ms=5.0, stop_ms=5.0)
