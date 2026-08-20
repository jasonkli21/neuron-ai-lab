"""Fail fast when the local runtime is unsuitable."""

from __future__ import annotations

import platform
import sys
from importlib.metadata import version


def main() -> None:
    if sys.version_info < (3, 12):
        raise SystemExit("Python 3.12 or newer is required.")

    print(f"Python: {platform.python_version()}")
    print(f"Platform: {platform.platform()}")
    for package in ("numpy", "matplotlib", "jupyterlab", "pytest", "ruff", "mypy"):
        print(f"{package}: {version(package)}")


if __name__ == "__main__":
    main()
