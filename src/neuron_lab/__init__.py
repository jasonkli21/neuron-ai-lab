"""Small, explicit computational-neuroscience models for guided learning."""

from neuron_lab.lif import LIFParameters, LIFResult, simulate_lif
from neuron_lab.simulation import SimulationConfig
from neuron_lab.stimuli import (
    gaussian_noise_current,
    pulse_current,
    sinusoidal_current,
    step_current,
    time_axis,
)

__all__ = [
    "LIFParameters",
    "LIFResult",
    "SimulationConfig",
    "gaussian_noise_current",
    "pulse_current",
    "simulate_lif",
    "sinusoidal_current",
    "step_current",
    "time_axis",
]
