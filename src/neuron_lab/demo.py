"""Generate a command-line LIF demonstration plot."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt

from neuron_lab.lif import LIFParameters, simulate_lif
from neuron_lab.plotting import plot_lif_result, save_figure
from neuron_lab.simulation import SimulationConfig
from neuron_lab.stimuli import step_current


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("outputs/lif_demo.png"),
        help="Path for the generated PNG.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = SimulationConfig(duration_ms=200.0, dt_ms=0.1)
    parameters = LIFParameters()
    current_na = step_current(
        config,
        amplitude_na=0.22,
        start_ms=25.0,
        stop_ms=175.0,
    )
    result = simulate_lif(parameters, config, current_na)
    figure, _ = plot_lif_result(
        result,
        title=f"LIF neuron: {result.spike_count} spikes, {result.firing_rate_hz:.1f} Hz",
    )
    save_figure(figure, args.output)
    plt.close(figure)
    print(f"Saved {args.output}")
    print(f"Membrane time constant: {parameters.membrane_time_constant_ms:.1f} ms")
    print(f"Passive rheobase estimate: {parameters.rheobase_na:.3f} nA")
    print(f"Spike times: {result.spike_times_ms.tolist()}")


if __name__ == "__main__":
    main()
