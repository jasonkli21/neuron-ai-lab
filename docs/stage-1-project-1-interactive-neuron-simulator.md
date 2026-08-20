# Stage 1, Project 1: Interactive Neuron Simulator

## Position within the three-year roadmap

### Overall roadmap

| Stage | Timeline | Primary objective |
|---|---:|---|
| **Stage 1: Foundations and biological intuition** | Months 0–6 | Reproduce foundational neuroscience models and learn the relevant biology, mathematics, and computational methods |
| **Stage 2: Brains versus modern AI** | Months 6–14 | Compare biological computation with transformers, memory systems, attention, and learning algorithms |
| **Stage 3: Research apprenticeship** | Months 14–24 | Formulate hypotheses and build a research-shaped project around memory, continual learning, or another biologically inspired mechanism |
| **Stage 4: Independent research** | Months 24–36 | Develop the most promising direction into a paper-quality open-source project or submission |

### Project placement

**Interactive Neuron Simulator**

- **Stage:** 1
- **Timeline:** Months 0–3
- **Workload:** Approximately eight hours per week
- **Total budget:** Approximately 90–100 hours
- **Primary purpose:** Build intuition about neuronal computation while learning how computational neuroscience models are constructed and validated
- **End state:** A compact educational laboratory, not a production simulator or original research contribution

The project should prepare you for the rest of Stage 1 and establish conceptual tools that will reappear in later stages. It should not attempt to solve the research questions reserved for Stages 2–4.

---

## 1. Project thesis

Build a small, interactive computational neuroscience laboratory that demonstrates how increasingly detailed neuron models transform input currents into electrical activity.

The project should connect four levels:

> biological mechanism → mathematical model → simulated behavior → computational interpretation

The central question is not merely:

> How do I simulate a neuron?

It is:

> Which properties of biological neurons are preserved or discarded at different levels of abstraction, and why might those properties matter computationally?

That question creates a natural bridge from introductory neuroscience to later comparisons with artificial neural networks.

---

## 2. Learning objectives

By the end of the project, you should be able to explain:

- how neuronal membranes behave like leaky electrical circuits
- how neurons integrate inputs over time
- why sufficiently strong input produces repeated firing
- how refractory periods and adaptation affect computation
- how voltage-gated sodium and potassium channels generate action potentials
- why different neuron types produce different firing patterns
- what simpler models preserve from more biologically detailed models
- why neuroscience researchers choose different models for different questions
- how biological neurons differ from the artificial units used in modern machine learning

The main deliverable is this understanding. The software is evidence that you acquired it.

---

## 3. Scope

The project will cover three neuron models.

### Model 1: Leaky integrate-and-fire

The leaky integrate-and-fire model introduces:

- membrane voltage
- input current
- leakage
- membrane time constants
- firing thresholds
- voltage reset
- refractory periods
- firing rates

It provides the clearest introduction to temporal integration and spike-based computation.

### Model 2: Izhikevich neuron

The Izhikevich model introduces:

- nonlinear neuronal dynamics
- recovery and adaptation variables
- regular spiking
- fast spiking
- bursting
- spike-frequency adaptation
- qualitative differences among neuron types

It serves as the bridge between simple threshold models and biophysical conductance models.

### Model 3: Hodgkin–Huxley neuron

The Hodgkin–Huxley model introduces:

- membrane capacitance
- ion equilibrium potentials
- sodium conductance
- potassium conductance
- leak conductance
- channel activation and inactivation
- action-potential generation
- refractory dynamics

It explains mechanistically what the simpler models represent only abstractly.

---

## 4. Revised definition of “interactive”

For this stage, interactive should mean:

- modifying parameters in a notebook
- selecting predefined input stimuli
- rerunning simulations
- observing updated plots
- comparing predefined neuron configurations

It does **not** require:

- a deployed web application
- a polished front end
- authentication or user accounts
- persistent experiment storage
- a general-purpose plugin architecture
- production-grade performance
- support for arbitrary external datasets

Notebook widgets or simple configuration cells are sufficient.

This preserves the educational value without spending much of the project on user-interface engineering that you already know how to do.

---

## 5. Core experiments

The project should contain approximately eight carefully selected experiments rather than a large feature set.

### Experiment 1: Passive membrane response

Apply a subthreshold current to a leaky integrate-and-fire neuron.

Observe:

- voltage rising toward equilibrium
- voltage returning toward rest
- the effect of input duration

Primary concept:

> A neuronal membrane integrates current but also leaks charge.

### Experiment 2: Membrane time constant

Change membrane resistance or capacitance.

Observe:

- faster or slower voltage responses
- changes in temporal integration
- sensitivity to brief versus sustained inputs

Primary concept:

> Membrane properties determine the timescale over which information is integrated.

### Experiment 3: Threshold and firing rate

Gradually increase constant input current.

Observe:

- the transition from no firing to repeated firing
- shorter interspike intervals at stronger inputs
- the effect of the refractory period

Primary concept:

> A neuron converts continuous input magnitude into temporal spike patterns.

### Experiment 4: Temporally structured input

Compare responses to:

- constant input
- brief pulses
- sinusoidal input
- noisy input

Primary concept:

> Neurons respond to temporal structure, not only average input strength.

### Experiment 5: Spike-frequency adaptation

Use an adapting Izhikevich neuron.

Observe:

- rapid initial firing
- gradual slowing during sustained input
- recovery after input stops

Primary concept:

> Neuronal responses depend on recent activity, not just present input.

### Experiment 6: Neuron firing classes

Compare several standard Izhikevich configurations, such as:

- regular spiking
- fast spiking
- bursting

Primary concept:

> Different neurons can transform identical inputs into qualitatively different outputs.

### Experiment 7: Action-potential mechanism

Run the Hodgkin–Huxley model and visualize:

- membrane voltage
- sodium current
- potassium current
- relevant channel variables

Primary concept:

> An action potential emerges from coordinated voltage-dependent ionic currents.

### Experiment 8: Model-abstraction comparison

Apply comparable stimuli to all three models.

Compare:

- whether they fire
- firing times
- spike shapes
- adaptation
- internal variables
- computational cost
- biological interpretability

Primary concept:

> A useful model preserves the properties relevant to the question being studied; greater detail is not automatically better.

---

## 6. Minimum deliverables

The project should produce five main artifacts.

### Deliverable 1: Leaky integrate-and-fire notebook

Contains:

- short conceptual explanation
- model equations
- parameter descriptions and units
- passive membrane experiment
- threshold experiment
- firing-rate experiment
- interpretation of results

### Deliverable 2: Izhikevich notebook

Contains:

- short conceptual explanation
- model equations
- recovery-variable interpretation
- adaptation experiment
- firing-class comparison
- interpretation of results

### Deliverable 3: Hodgkin–Huxley notebook

Contains:

- short biological introduction
- conductance-based model explanation
- action-potential simulation
- sodium and potassium current visualization
- one channel-conductance perturbation
- interpretation of results

### Deliverable 4: Model-comparison notebook

Contains:

- shared stimulus comparisons
- concise abstraction table
- qualitative comparison of outputs
- runtime or computational-complexity comparison
- discussion of appropriate use cases for each model

### Deliverable 5: Synthesis document

A relatively short written explanation covering:

1. What each model represents
2. What each model omits
3. What became clearer through implementation
4. Which neuronal properties might matter for AI
5. Which questions should be carried into later stages

This could eventually become a public technical essay, but publication is optional during Stage 1.

---

## 7. Minimal project architecture

The original plan proposed a larger reusable simulation platform. For this stage, the architecture should remain deliberately small.

Conceptually, it only needs:

```text
project/
  notebooks/
    01_leaky_integrate_and_fire
    02_izhikevich
    03_hodgkin_huxley
    04_model_comparison

  neuron_models/
    lif
    izhikevich
    hodgkin_huxley

  stimuli/
    constant
    pulse
    sinusoidal
    noisy

  validation/
    reference_behaviors

  notes/
    neuroscience_concepts
    model_comparison
    final_synthesis
```

The scientific model logic should be separable from plotting code, but there is no need to design a generalized framework for unknown future use cases.

A small amount of duplication is acceptable if it keeps the project comprehensible.

---

## 8. Twelve-week progression

### Month 1: Electrical foundations and LIF

#### Weeks 1–2: Conceptual foundations

Learn only the material required to understand the first model:

- neuron and membrane structure
- membrane potential
- current, resistance, and capacitance
- RC circuits
- membrane time constants
- basic differential equations
- numerical integration intuition

Outcome:

You can explain the passive membrane equation and predict its qualitative behavior.

#### Weeks 3–4: LIF model and experiments

Cover:

- threshold and reset
- refractory periods
- constant and pulsed input
- firing-rate-versus-current behavior
- membrane parameter changes

Outcome:

A complete LIF notebook and a clear understanding of temporal integration.

### Month 2: Nonlinear dynamics and Izhikevich neurons

#### Weeks 5–6: Dynamical-systems intuition

Learn enough to interpret:

- coupled state variables
- nonlinear feedback
- phase-plane trajectories
- adaptation
- stable and unstable behavior
- qualitative firing regimes

Formal mathematical depth should remain limited to what the model requires.

#### Weeks 7–8: Izhikevich model and experiments

Cover:

- recovery-variable behavior
- regular spiking
- fast spiking
- bursting
- adaptation
- parameter-dependent firing classes

Outcome:

A complete Izhikevich notebook and an intuitive understanding of how internal dynamics create different temporal behaviors.

### Month 3: Biophysical mechanisms and synthesis

#### Weeks 9–10: Hodgkin–Huxley foundations

Learn:

- ion concentration gradients
- equilibrium potentials
- conductance-based currents
- sodium-channel activation and inactivation
- potassium-channel activation
- action-potential phases
- refractory dynamics

#### Week 11: Hodgkin–Huxley experiments

Complete:

- action-potential simulation
- ionic-current visualization
- gating-variable visualization
- one channel perturbation
- numerical sanity checks

#### Week 12: Comparison and synthesis

Complete:

- cross-model experiment
- model-abstraction comparison
- validation review
- final synthesis document
- list of open questions for future stages

Outcome:

A completed educational laboratory and an explicit conceptual bridge to the remainder of the roadmap.

---

## 9. Approximate time allocation

Across roughly 96 hours:

| Activity | Approximate hours |
|---|---:|
| Targeted neuroscience and mathematical reading | 25 |
| Model construction and notebook work | 35 |
| Experiments and visualizations | 18 |
| Validation and debugging | 8 |
| Comparison and written synthesis | 10 |
| **Total** | **96** |

This maintains the broader preference for learning through building while preserving enough reading to avoid implementing equations without understanding them.

The split is approximately:

- **25–30% reading and conceptual study**
- **70–75% building, experimenting, and explaining**

---

## 10. Validation requirements

The project should be scientifically credible but does not need research-grade validation.

### Required validation

For every model:

- confirm equations against a trusted textbook, course, or original source
- clearly document units
- reproduce canonical qualitative behavior
- verify that reducing the simulation time step does not radically change results
- explain any artificial spike reset or threshold conventions

For Hodgkin–Huxley:

- verify the expected sequence of sodium and potassium activity
- confirm a plausible action-potential shape
- distinguish biological currents from visualization choices

### Not required during this project

- comparison with experimental neural recordings
- formal parameter estimation
- statistical hypothesis testing
- benchmarking against large neuroscience simulators
- extensive solver comparisons
- publication-grade biological claims

Those belong to later research stages.

---

## 11. Scope boundaries

The project should explicitly exclude:

- multicompartment neurons
- dendritic morphology
- detailed synaptic models
- learning or synaptic plasticity
- networks of neurons
- spiking neural-network training
- neuromodulators
- realistic sensory data
- parameter fitting from recordings
- large parameter sweeps
- GPU optimization
- production deployment
- original research claims

A tiny two-neuron demonstration may be acceptable at the very end only if time remains, but it should not become a formal deliverable.

The second half of Stage 1 will provide a better place to move from individual neurons toward synapses, learning rules, and small networks.

---

## 12. Relationship to the rest of Stage 1

Project 1 should establish:

- electrical neuron intuition
- differential-equation simulation experience
- temporal representations
- model abstraction habits
- scientific validation habits
- comfort reading computational neuroscience equations

The remainder of Stage 1 can then build on this through topics such as:

- synapses
- Hebbian learning
- spike-timing-dependent plasticity
- small recurrent networks
- attractor dynamics
- introductory representations of memory and learning

Project 1 should therefore stop at the point where you understand individual neuronal computation. It should not consume the material intended for the next foundational project.

---

## 13. Connections to later stages

### Stage 2: Brains versus modern AI

The simulator will provide concrete examples for comparing:

- spikes versus continuous artificial activations
- temporal integration versus transformer token processing
- adaptation versus static neural-network activations
- recurrent neuronal state versus feedforward computation
- biological heterogeneity versus mostly homogeneous artificial units
- local dynamics versus global backpropagation

At this stage, you may return to the models for focused comparisons, but you should not substantially expand the simulator.

### Stage 3: Research apprenticeship

The project may later supply components or intuition for research on:

- continual learning
- temporal memory
- adaptive units
- sparse event-driven computation
- local learning
- biologically inspired recurrent systems

The Stage 3 project should be driven by a research question, not by a desire to add simulator features.

### Stage 4: Independent research

Only if an earlier experiment suggests a promising direction should any part of the simulator become research infrastructure.

Possible examples include:

- testing whether neuronal adaptation improves continual-learning behavior
- comparing learned artificial units with known neuronal dynamics
- evaluating biologically inspired temporal mechanisms
- studying model reduction or differentiable neuron models

The decision should emerge from Stage 2 or Stage 3 evidence. It should not be predetermined during Stage 1.

---

## 14. Completion criteria

The project is complete when:

1. The four notebooks run reproducibly.
2. All three neuron models display their canonical qualitative behavior.
3. Every parameter and state variable has a documented interpretation and unit.
4. The eight core experiments are complete.
5. The comparison notebook clearly explains the tradeoff between abstraction and biological detail.
6. You can explain the major results without relying on the notebook text.
7. The synthesis identifies several connections to AI without making unsupported equivalence claims.
8. Remaining ideas are documented as future questions rather than added to the current scope.

A polished web interface is not part of the completion criteria.

---

## 15. Final project standard

At the end of Month 3, the project should feel like:

> a well-understood computational neuroscience laboratory created by a technically strong beginner

It should not attempt to look like:

> a comprehensive neural-simulation framework or mature neuroscience research platform

The proper measure of success is whether you have built enough intuition to move confidently into synaptic learning, small neural systems, and eventually brain–AI comparisons.

The project should leave you curious and equipped for the next stage—not exhausted from maintaining infrastructure that the roadmap does not yet require.
