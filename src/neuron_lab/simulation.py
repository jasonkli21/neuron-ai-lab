"""Shared simulation configuration."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import numpy.typing as npt

FloatArray = npt.NDArray[np.float64]
IntArray = npt.NDArray[np.int64]


@dataclass(frozen=True, slots=True)
class SimulationConfig:
    """Numerical settings.

    Units:
        duration_ms: milliseconds
        dt_ms: milliseconds
    """

    duration_ms: float = 200.0
    dt_ms: float = 0.1

    def __post_init__(self) -> None:
        if not np.isfinite(self.duration_ms) or self.duration_ms <= 0:
            raise ValueError("duration_ms must be finite and positive")
        if not np.isfinite(self.dt_ms) or self.dt_ms <= 0:
            raise ValueError("dt_ms must be finite and positive")
        if self.dt_ms > self.duration_ms:
            raise ValueError("dt_ms must not exceed duration_ms")

    @property
    def n_steps(self) -> int:
        """Number of recorded time samples, including t=0."""
        return int(np.floor(self.duration_ms / self.dt_ms)) + 1
