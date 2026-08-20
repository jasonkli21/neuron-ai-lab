"""Plotting helpers kept separate from scientific model logic."""

from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes
from matplotlib.figure import Figure

from neuron_lab.lif import LIFResult


def plot_lif_result(
    result: LIFResult,
    *,
    title: str | None = None,
) -> tuple[Figure, tuple[Axes, Axes]]:
    """Plot input current and membrane voltage for one simulation."""
    figure, axes_array = plt.subplots(2, 1, sharex=True, figsize=(10, 6))
    current_axis, voltage_axis = axes_array

    current_axis.plot(result.time_ms, result.input_current_na)
    current_axis.set_ylabel("Current (nA)")
    current_axis.grid(alpha=0.25)

    voltage_axis.plot(result.time_ms, result.voltage_mv)
    voltage_axis.axhline(
        result.parameters.threshold_mv,
        linestyle="--",
        linewidth=1.0,
        label="Threshold",
    )
    if result.spike_count:
        voltage_axis.scatter(
            result.spike_times_ms,
            np.full(result.spike_count, result.parameters.threshold_mv),
            marker="x",
            label="Spike event",
        )
    voltage_axis.set_xlabel("Time (ms)")
    voltage_axis.set_ylabel("Voltage (mV)")
    voltage_axis.grid(alpha=0.25)
    voltage_axis.legend(loc="best")

    if title is not None:
        figure.suptitle(title)
    figure.tight_layout()
    return figure, (current_axis, voltage_axis)


def plot_fi_curve(
    currents_na: Sequence[float],
    firing_rates_hz: Sequence[float],
) -> tuple[Figure, Axes]:
    """Plot a firing-rate–current curve."""
    figure, axis = plt.subplots(figsize=(8, 5))
    axis.plot(currents_na, firing_rates_hz, marker="o")
    axis.set_xlabel("Constant current (nA)")
    axis.set_ylabel("Firing rate (Hz)")
    axis.set_title("LIF firing-rate–current curve")
    axis.grid(alpha=0.25)
    figure.tight_layout()
    return figure, axis


def save_figure(figure: Figure, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(output_path, dpi=160, bbox_inches="tight")
