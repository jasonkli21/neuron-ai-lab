# Neuron Lab

A compact computational neuroscience learning project. The first milestone implements and explores a **leaky integrate-and-fire (LIF) neuron** with explicit units, reproducible simulations, validation tests, and a guided notebook.

## Current scope

Model 1 covers:

- passive membrane dynamics
- membrane time constants
- threshold, reset, and refractory behavior
- constant and pulsed current inputs
- firing-rate–current (F–I) curves
- numerical time-step checks

This repository intentionally does **not** yet include Hodgkin–Huxley, Izhikevich, synapses, networks, plasticity, or a web interface.

## Scientific unit convention

The initial model uses:

| Quantity | Unit |
|---|---|
| Time | milliseconds (`ms`) |
| Voltage | millivolts (`mV`) |
| Current | nanoamps (`nA`) |
| Resistance | megaohms (`MΩ`) |
| Capacitance | nanoFarads (`nF`) |

These units are convenient because:

- `MΩ × nA = mV`
- `MΩ × nF = ms`

## macOS prerequisites

Open Terminal and verify that Git is available:

```bash
git --version
```

When macOS prompts you to install the Xcode Command Line Tools, accept the prompt. You can also request them manually:

```bash
xcode-select --install
```

Install `uv`, which will manage the project Python version, virtual environment, and dependencies:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Restart Terminal, or reload your shell configuration:

```bash
source ~/.zshrc
```

Verify the installation:

```bash
uv --version
```

Optional but recommended for pushing to GitHub from the terminal:

```bash
brew install gh
gh auth login
```

GitHub Desktop also works; the repository itself does not depend on the GitHub CLI.

## Create the local project

Unzip the downloaded project and move it wherever you keep personal code:

```bash
mkdir -p ~/code
mv ~/Downloads/neuron-lab-model-1 ~/code/neuron-lab
cd ~/code/neuron-lab
```

If the downloaded folder has a different location or name, adjust the command accordingly.

## Install and verify

The repository pins Python 3.12 in `.python-version`.

Create the environment and install the project plus development dependencies:

```bash
uv sync --all-groups
```

`uv sync` creates `uv.lock`. Commit that file so local development and CI resolve the same dependency set.

Run the complete verification suite:

```bash
make check
```

This runs formatting checks, linting, static type checking, and tests.

## Launch the notebook

```bash
make lab
```

Open:

```text
notebooks/01_lif_foundations.ipynb
```

The notebook imports the implementation from `src/neuron_lab`; the scientific logic is not hidden inside notebook cells.

## Run the command-line demonstration

```bash
make demo
```

This saves:

```text
outputs/lif_demo.png
```

## Git and personal GitHub setup

Initialize the local Git repository:

```bash
git init
git add .
git commit -m "Bootstrap leaky integrate-and-fire neuron lab"
git branch -M main
```

### Option A: GitHub CLI

Create a new private repository and push it:

```bash
gh repo create neuron-lab \
  --private \
  --source=. \
  --remote=origin \
  --push
```

Change `--private` to `--public` when you are ready to share it.

### Option B: GitHub website

1. Create a new empty repository named `neuron-lab`.
2. Do not initialize it with a README, `.gitignore`, or license.
3. Add the remote and push:

```bash
git remote add origin https://github.com/YOUR_USERNAME/neuron-lab.git
git push -u origin main
```

## Suggested working rhythm

Use small commits that each preserve a runnable project:

```text
docs: clarify membrane time constant
test: add passive steady-state validation
feat: add pulse current stimulus
experiment: compare refractory periods
```

A useful branch convention is:

```text
main
experiment/lif-time-constant
experiment/lif-fi-curve
```

Do not create a branch for every notebook edit. Use branches for meaningful experiments that may be abandoned or reviewed separately.

## Repository layout

```text
.
├── .github/workflows/ci.yml
├── notebooks/01_lif_foundations.ipynb
├── notes/lab_log.md
├── notes/model_1_synthesis.md
├── outputs/.gitkeep
├── scripts/verify_environment.py
├── src/neuron_lab/
│   ├── __init__.py
│   ├── demo.py
│   ├── lif.py
│   ├── plotting.py
│   ├── simulation.py
│   └── stimuli.py
├── tests/
│   ├── test_lif.py
│   └── test_stimuli.py
├── .gitignore
├── .python-version
├── Makefile
├── pyproject.toml
└── README.md
```

## Model equation

The subthreshold LIF dynamics are:

```text
C_m dV/dt = -(V - E_L) / R_m + I(t)
```

Equivalently:

```text
dV/dt = [E_L - V + R_m I(t)] / τ_m
τ_m = R_m C_m
```

When the simulated voltage reaches the threshold:

1. record a spike event;
2. hold/reset the model at `V_reset`;
3. prevent another spike during the absolute refractory period.

The threshold marker is an **event representation**, not a biophysically realistic action-potential waveform.

## Default parameters

| Parameter | Default | Interpretation |
|---|---:|---|
| Resting potential | `-65 mV` | Leak reversal/resting level |
| Reset potential | `-65 mV` | Voltage following a spike |
| Threshold | `-50 mV` | Event threshold |
| Resistance | `100 MΩ` | Input resistance |
| Capacitance | `0.2 nF` | Membrane capacitance |
| Time constant | `20 ms` | `R_m × C_m` |
| Refractory period | `2 ms` | Minimum post-spike pause |

With these defaults, a constant current below approximately `0.15 nA` is subthreshold because the passive steady-state voltage is:

```text
V∞ = E_L + R_m I
```

and threshold requires:

```text
I ≥ (V_threshold - E_L) / R_m
```

The exact first-spike behavior also depends on stimulus duration and numerical time step.

## Development commands

```bash
make sync       # install/update dependencies
make format     # apply Ruff formatting and safe fixes
make lint       # check formatting and lint rules
make typecheck  # run mypy
make test       # run pytest
make check      # all non-mutating checks
make demo       # generate an example plot
make lab        # launch JupyterLab
make clean      # remove generated caches and outputs
```

## Definition of done for Model 1

Model 1 is complete when:

- the notebook can reproduce passive charging and decay;
- the steady-state voltage matches the analytical solution within tolerance;
- supra-threshold current produces spikes;
- the refractory period limits spike frequency;
- an F–I curve is generated and interpreted;
- reducing `dt` does not materially change the qualitative result;
- equations, units, reset conventions, and limitations are documented;
- `make check` passes locally and in GitHub Actions.

## Next work, deliberately deferred

After finishing the notebook and writing your own short interpretation, the next additions should be educational rather than architectural:

1. add a sinusoidal current experiment;
2. compare brief pulses with equal total charge;
3. derive the analytical passive-membrane solution;
4. investigate Euler time-step error;
5. write the Model 1 synthesis.

Do not add another neuron model until these foundations feel intuitive.
