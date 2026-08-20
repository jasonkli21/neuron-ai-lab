# Neuroscience × AI: Three-Year Learning and Research Roadmap

## Purpose

This document is the parent plan for a three-year program at the intersection of neuroscience and artificial intelligence.

It is intentionally higher-level than individual project specifications such as:

- `stage-1-project-1-interactive-neuron-simulator.md`

Its role is to define:

- the overall progression
- the purpose and boundaries of each stage
- the major projects within each stage
- the expected level of rigor
- the learning and research outputs
- the transition criteria between stages

Detailed project plans should be derived from this document while preserving its scope and sequencing.

---

# 1. Program thesis

The long-term goal is to use neuroscience as a source of **computational hypotheses** for improving AI systems.

The program is not based on the assumption that artificial intelligence should simply copy the brain. Instead, it uses neuroscience to ask:

- What computational problems has biological evolution already solved?
- Which mechanisms are essential to biological intelligence?
- Which mechanisms are implementation details of biological hardware?
- Where do brains and modern AI systems solve similar problems differently?
- Can biologically inspired mechanisms improve memory, learning, reasoning, robustness, efficiency, or continual adaptation in artificial systems?

The desired progression is:

> reproduce → understand → compare → hypothesize → experiment → research

The first year emphasizes scientific and computational foundations. The second year increasingly shifts toward research-shaped work. The third year aims at independent, publishable-quality research.

---

# 2. Time commitment

Default workload:

- **8 hours per week**
- approximately **400 hours per year**
- approximately **1,200 hours over three years**

This is intended to coexist with a full-time engineering career.

The program therefore favors:

- high-value reading
- learning by building
- small but rigorous experiments
- reusable technical artifacts
- synthesis writing
- avoiding large infrastructure projects unless they directly support research

A typical weekly split should vary by stage.

## Early stages

Approximately:

- 25–35% reading and conceptual learning
- 50–60% implementation and experiments
- 10–20% synthesis and notes

## Later stages

Approximately:

- 15–25% reading
- 50–60% experimentation and engineering
- 20–30% analysis, writing, and research communication

---

# 3. Program structure

| Stage | Timeline | Main objective |
|---|---:|---|
| **Stage 1: Foundations and biological intuition** | Months 0–6 | Build mechanistic intuition for neurons, learning rules, and small neural systems |
| **Stage 2: Brains versus modern AI** | Months 6–14 | Compare biological computation with transformers, memory systems, learning, attention, and representation |
| **Stage 3: Research apprenticeship** | Months 14–24 | Learn to formulate and test research questions through a focused research-shaped project |
| **Stage 4: Independent research** | Months 24–36 | Develop the strongest direction into an original, paper-quality research program |

The stages are cumulative.

Each later stage assumes the ability to:

- read technical papers
- implement models from equations
- design controlled experiments
- distinguish correlation from mechanism
- identify assumptions and limitations
- explain results clearly

---

# 4. Stage 1: Foundations and biological intuition

## Timeline

**Months 0–6**

Approximate effort:

- 24–26 weeks
- roughly 190–210 hours

## Stage objective

Develop a working mechanistic understanding of how biological neural systems perform computation at the level of:

- individual neurons
- synapses
- local learning rules
- small recurrent networks
- elementary memory and dynamical systems

The goal is not comprehensive neuroscience expertise.

The goal is to acquire enough biological and mathematical intuition to reason productively about possible computational principles.

## Stage 1 guiding questions

By the end of Stage 1, you should be able to reason about:

- How do neurons integrate signals through time?
- Why do different neurons produce different activity patterns?
- How do synapses change?
- How can learning emerge from local interactions?
- How do recurrent networks store or stabilize information?
- How does biological learning differ from backpropagation?
- Which biological properties might matter computationally?

---

## Project 1: Interactive neuron simulator

### Timeline

**Months 0–3**

Approximate effort:

- 90–100 hours

### Purpose

Build intuition for single-neuron computation by implementing models at increasing levels of abstraction.

### Core models

1. Leaky integrate-and-fire
2. Izhikevich
3. Hodgkin–Huxley

### Core concepts

- membrane potential
- resistance and capacitance
- membrane time constants
- threshold and reset
- refractory periods
- spike-frequency adaptation
- nonlinear dynamics
- ion-channel conductances
- action potentials
- model abstraction

### Expected artifacts

- LIF notebook
- Izhikevich notebook
- Hodgkin–Huxley notebook
- cross-model comparison notebook
- validation tests
- short synthesis document

### Scope boundary

Do not yet include:

- large neural networks
- synaptic plasticity
- detailed morphology
- realistic sensory data
- spiking neural-network training
- original research claims

### Exit criterion

You should be able to explain:

- what each model captures
- what each model discards
- why simpler models can be more useful
- how biological neuron dynamics differ from standard artificial units

A detailed plan should live separately in:

`stage-1-project-1-interactive-neuron-simulator.md`

---

## Project 2: Synapses, plasticity, and small neural systems

### Timeline

**Months 3–6**

Approximate effort:

- 90–110 hours

### Purpose

Move from individual neuronal dynamics to learning and computation that emerge through interactions among neurons.

### Core topics

#### Synaptic transmission

Study:

- excitatory versus inhibitory synapses
- postsynaptic potentials
- synaptic strength
- temporal and spatial summation
- synaptic delays
- basic neurotransmitter concepts

Only enough biological detail is needed to support computational understanding.

#### Hebbian learning

Implement and study:

- basic Hebbian learning
- correlation-based learning
- instability of unconstrained Hebbian rules

Key question:

> How can useful representations emerge from local activity correlations?

#### Oja's rule

Use Oja's rule to understand:

- normalized Hebbian learning
- principal-component-like representation learning
- how local learning can perform meaningful statistical computation

#### Spike-timing-dependent plasticity

Implement:

- pre-before-post strengthening
- post-before-pre weakening
- timing windows

Explore:

- how temporal correlations alter connectivity
- how repeated patterns become encoded

#### Small recurrent networks

Build toy networks demonstrating:

- recurrent excitation
- inhibition
- stable states
- oscillation
- winner-take-all behavior

#### Attractor memory

Implement a small Hopfield-style or related attractor network.

Study:

- pattern storage
- pattern completion
- robustness to corrupted input
- capacity limitations

### Expected experiments

Possible experiments include:

1. Hebbian learning from correlated inputs
2. Oja's rule recovering a dominant component
3. STDP under controlled spike timing
4. excitation/inhibition balance in a tiny recurrent network
5. attractor recovery from partial or noisy patterns
6. comparison between local plasticity and gradient-based learning

### Expected artifacts

- synaptic dynamics notebook
- learning-rules notebook
- STDP notebook
- recurrent-network notebook
- attractor-memory notebook
- Stage 1 synthesis

### Stage 1 synthesis

At the end of Month 6, write a synthesis answering:

- What computational behaviors already emerge from simple biological rules?
- Where does biology appear substantially different from modern deep learning?
- Which mechanisms seem most promising for later AI experiments?
- Which apparent similarities are only superficial analogies?
- What questions should be carried into Stage 2?

---

## Stage 1 required knowledge

### Neuroscience

Target functional understanding of:

- neuron anatomy
- membrane electrophysiology
- action potentials
- synaptic transmission
- excitatory/inhibitory interactions
- plasticity
- basic cortical organization
- hippocampal memory concepts

### Mathematics

Target practical intuition for:

- ordinary differential equations
- numerical integration
- linear algebra
- probability
- basic dynamical systems
- phase space
- stability
- simple optimization

No formal advanced mathematics curriculum is required unless a project exposes a concrete gap.

### Software

Use:

- Python
- NumPy
- Matplotlib
- Jupyter
- pytest
- simple scientific-computing patterns

Avoid premature infrastructure.

---

## Stage 1 completion criteria

Stage 1 is complete when you can:

1. implement canonical neuron models from equations
2. reproduce known qualitative neural behaviors
3. explain local plasticity rules
4. build and analyze a small recurrent neural system
5. reason about attractor memory
6. distinguish biological mechanism from mathematical abstraction
7. document assumptions and units
8. validate numerical simulations
9. identify several meaningful brain–AI comparison questions

At this point, the emphasis should shift away from foundational simulation and toward comparative analysis.

---

# 5. Stage 2: Brains versus modern AI

## Timeline

**Months 6–14**

Approximate effort:

- 8 months
- roughly 250–280 hours

## Stage objective

Develop a structured understanding of similarities and differences between biological intelligence and modern artificial intelligence.

The goal is not to produce simplistic one-to-one analogies such as:

> hippocampus = vector database

Instead, compare systems at the level of computational problems.

For example:

- storing information
- retrieving information
- routing information
- assigning credit
- adapting to new experience
- stabilizing old knowledge
- selecting actions
- maintaining goals
- representing uncertainty

## Stage 2 guiding framework

For every comparison, ask:

1. What computational problem is being solved?
2. How does the brain appear to solve it?
3. How does the AI system solve it?
4. What constraints differ?
5. What tradeoffs result?
6. Is the biological mechanism plausibly useful in AI?
7. What experiment could test that?

This framework should become habitual.

---

## Project 3: Brain–transformer computational map

### Approximate timeline

**Months 6–8**

### Purpose

Construct a structured comparison between core transformer mechanisms and known biological computation.

### AI topics

Study:

- token embeddings
- attention
- MLP layers
- residual streams
- positional representation
- autoregressive prediction
- KV caching
- context windows
- normalization
- training through backpropagation

### Neuroscience topics

Study at a computational level:

- cortical recurrent processing
- thalamic routing
- prefrontal executive control
- working memory
- hippocampal memory
- basal ganglia gating
- sensory hierarchy
- predictive processing

### Important rule

Do not attempt to declare direct anatomical equivalence.

Instead, organize comparisons around functional dimensions such as:

| Computational function | Biological solution | Transformer/AI solution |
|---|---|---|
| temporary information maintenance | recurrent activity / activity-silent mechanisms | context/KV state |
| long-term knowledge | distributed synaptic changes | model weights |
| selective routing | attention/gating networks | attention mechanisms |
| sequence information | recurrent temporal dynamics | positional encoding + autoregression |
| learning | local + global biological mechanisms | backpropagation |

### Expected artifacts

- computational comparison matrix
- architecture diagrams
- technical essay
- list of testable hypotheses

---

## Project 4: Memory systems in brains and AI

### Approximate timeline

**Months 8–11**

### Purpose

Deeply study memory as a candidate bridge between neuroscience and AI.

This is a high-priority area because memory is both:

- central to biological cognition
- an unresolved systems problem in advanced AI

### Biological memory topics

Study:

- working memory
- episodic memory
- semantic memory
- procedural memory
- hippocampal indexing
- systems consolidation
- replay
- reconsolidation
- forgetting
- interference

### AI memory topics

Study:

- context windows
- retrieval-augmented generation
- vector retrieval
- episodic agent memory
- summaries
- long-term memory stores
- model weights as semantic memory
- fine-tuning
- continual learning
- catastrophic forgetting

### Experiments

Build small systems that compare memory architectures.

Potential prototype:

> a minimal conversational or agentic AI system with explicit working, episodic, and semantic memory layers

Possible components:

- short-term context buffer
- episodic event store
- retrieval
- consolidation process
- forgetting or importance mechanism
- semantic summarization

### Core research questions

- Should all remembered experiences remain equally retrievable?
- Can replay improve later reasoning?
- When should episodic memory be consolidated into semantic knowledge?
- Can forgetting improve retrieval quality?
- How should memories compete for limited capacity?
- What should trigger consolidation?

### Expected artifacts

- literature map
- memory taxonomy
- prototype memory system
- benchmark tasks
- experiment report

---

## Project 5: Attention, control, and active cognition

### Approximate timeline

**Months 11–14**

### Purpose

Study mechanisms that govern what an intelligent system processes, retains, and acts upon.

### Biological topics

Potential topics:

- selective attention
- executive control
- working-memory gating
- inhibition
- basal ganglia
- prefrontal cortex
- neuromodulation
- salience
- exploration/exploitation
- active inference

### AI topics

Potential topics:

- transformer attention
- tool selection
- agent planning
- context selection
- search
- reflection
- uncertainty
- reward-guided action

### Prototype directions

Examples:

- controller that selects which memories enter context
- uncertainty-driven information gathering
- adaptive compute allocation
- inhibition mechanism that suppresses redundant paths
- exploration strategy based on novelty or prediction error

### Expected output

The objective is not necessarily a major system.

The primary deliverable is a shortlist of **researchable mechanisms** suitable for Stage 3.

---

## Stage 2 reading strategy

Reading should shift toward primary literature.

For each topic:

1. read one strong overview
2. identify 3–6 foundational papers
3. identify 3–6 recent papers
4. reproduce at least one central experiment when practical
5. write a short synthesis
6. record open questions

Maintain a literature database containing:

- paper
- research question
- method
- key finding
- assumptions
- weaknesses
- relationship to your research interests
- possible experiment

---

## Stage 2 completion criteria

Stage 2 is complete when you can:

1. compare brain and AI mechanisms without relying on superficial analogy
2. read contemporary neuroscience and AI research papers productively
3. identify important unresolved problems
4. distinguish engineering problems from scientific questions
5. translate biological mechanisms into computational hypotheses
6. design small experiments that could falsify those hypotheses
7. select one or two promising Stage 3 research directions

The output of Stage 2 should be a **research candidate document** ranking possible directions.

---

# 6. Stage 3: Research apprenticeship

## Timeline

**Months 14–24**

Approximate effort:

- 10 months
- roughly 300–340 hours

## Stage objective

Transition from educational projects to genuine research methodology.

At this stage, the work should become question-driven rather than curriculum-driven.

The central shift is:

> Do not build something because it is interesting. Build it because it tests a specific hypothesis.

---

## Selecting the Stage 3 research question

The question should satisfy most of these criteria:

- meaningful connection between neuroscience and AI
- experimentally testable
- feasible on modest compute
- measurable outcome
- clear baselines
- accessible datasets or synthetic tasks
- ability to produce negative as well as positive results
- sufficiently narrow for several months of work
- capable of generating follow-up questions

Possible domains include:

- memory consolidation
- replay
- forgetting
- continual learning
- sparse memory
- adaptive attention
- recurrent state
- neuromodulation
- uncertainty-driven exploration
- curiosity
- temporal adaptation
- biologically inspired gating
- associative memory

---

## Canonical Stage 3 direction: biologically inspired memory research

Memory is a strong default research direction, though Stage 2 evidence may justify another.

### Example research question

> Does a hippocampal-inspired episodic replay and consolidation mechanism improve long-horizon memory and reduce interference in an LLM-based agent compared with retrieval-only memory?

This is substantially narrower than:

> build an artificial hippocampus

The narrow form is testable.

---

## Research workflow

### Phase 1: Literature review

Define:

- what is already known
- existing methods
- strongest baselines
- unresolved questions
- relevant neuroscience
- relevant AI literature

Produce a written literature review.

### Phase 2: Hypothesis

Write explicit hypotheses.

Example:

> Periodic replay of high-information episodic memories into a compressed semantic memory will improve delayed recall while using less retrieval context than storing all episodes independently.

Define what evidence would disprove the claim.

### Phase 3: Benchmark design

Develop tasks that isolate the phenomenon.

Examples:

- facts introduced over long interaction histories
- changing user preferences
- conflicting information
- delayed recall
- repeated concepts
- memory interference
- contextual dependency

### Phase 4: Baselines

Compare against strong alternatives.

Possible baselines:

- no external memory
- sliding context
- vector retrieval
- retrieval + summarization
- fixed long-term memory
- recency-based memory

### Phase 5: Experimental system

Implement only the infrastructure required to test the hypothesis.

### Phase 6: Controlled experiments

Control variables such as:

- model
- prompt
- token budget
- retrieval budget
- random seed
- memory size
- number of interactions

### Phase 7: Analysis

Measure:

- recall accuracy
- interference
- retrieval precision
- token cost
- latency
- memory growth
- robustness across tasks

### Phase 8: Ablations

Remove individual mechanisms.

For example:

- replay without consolidation
- consolidation without replay
- random replay
- importance-based replay
- no forgetting

### Phase 9: Research report

Write the project as though it were a small paper:

1. abstract
2. problem
3. related work
4. hypothesis
5. method
6. experimental setup
7. results
8. ablations
9. limitations
10. future work

---

## Other possible Stage 3 directions

### Continual learning

Question examples:

- Can replay inspired by biological memory reduce catastrophic forgetting?
- Can dual fast/slow learning systems improve adaptation?

### Associative memory

Question examples:

- Can sparse associative retrieval improve discovery across distant concepts?
- How does memory overlap affect generalization versus interference?

### Adaptive computational units

Question examples:

- Does neuronal adaptation improve temporal prediction?
- Can activity-dependent thresholds improve recurrent models?

### Neuromodulation

Question examples:

- Can context-dependent learning-rate or routing signals improve multi-task learning?
- Can novelty or uncertainty act as a useful global modulation signal?

### Active information gathering

Question examples:

- Can prediction-error-driven exploration improve research agents?
- When should an agent seek information rather than continue reasoning internally?

---

## Stage 3 research practices

Adopt professional research habits.

### Experiment tracking

Record:

- code commit
- configuration
- dataset version
- model version
- random seed
- metrics
- result
- interpretation

### Reproducibility

Every meaningful experiment should be reproducible from configuration.

### Negative results

Record failed hypotheses.

Negative results are useful if:

- the experiment was valid
- the baseline was strong
- the failure teaches something

### Statistical reasoning

Use:

- multiple runs
- confidence intervals where useful
- effect sizes
- baseline comparisons

Do not rely solely on visually compelling examples.

### Research log

Maintain:

- hypotheses
- experiment outcomes
- contradictions
- literature connections
- next questions

---

## Stage 3 completion criteria

Stage 3 is complete when you have:

1. formulated a precise research question
2. performed a literature review
3. built meaningful baselines
4. designed a controlled evaluation
5. run reproducible experiments
6. performed ablations
7. interpreted negative results when applicable
8. written a paper-style report
9. identified the strongest follow-up direction

Publication is not required.

The primary goal is to learn how to do research well.

---

# 7. Stage 4: Independent research

## Timeline

**Months 24–36**

Approximate effort:

- 12 months
- roughly 350–400 hours

## Stage objective

Take the strongest research direction from Stage 3 and develop it into an original research contribution.

Possible outcomes include:

- arXiv preprint
- workshop submission
- conference paper
- substantial open-source research project
- collaboration with an academic or industry research group
- strong research portfolio artifact

The project should now emphasize novelty, rigor, and external relevance.

---

## Stage 4 structure

Stage 4 should be iterative rather than planned completely in advance.

### Months 24–27: Refine the question

Use Stage 3 results to identify the most important unresolved issue.

Perform:

- deeper literature review
- replication of closest competing methods
- benchmark refinement
- preliminary experiments

The research question should become narrower and stronger.

### Months 27–30: Build the core result

Focus on:

- main method
- strongest baselines
- core experiments
- robustness
- scaling behavior
- failure cases

Avoid adding unrelated features.

### Months 30–33: Ablations and generalization

Test:

- mechanism necessity
- sensitivity to parameters
- generalization to other tasks
- generalization to other models
- compute/cost tradeoffs

This period determines whether the finding is robust enough to claim.

### Months 33–36: Communication and release

Produce:

- clean repository
- reproducible experiment scripts
- final figures
- research paper or report
- documentation
- public technical explanation

Potentially:

- submit to a workshop
- submit to a conference
- request external review
- contact relevant researchers
- open-source the work

---

# 8. Potential Stage 4 research themes

The exact theme should emerge from prior evidence, but several areas are especially compatible with the program.

## Memory consolidation

Possible hypothesis:

> Hierarchical consolidation improves long-term agent memory by transforming episodic experience into reusable semantic representations.

## Complementary learning systems

Biological inspiration:

- hippocampus learns quickly
- cortex learns slowly

AI question:

> Can separate fast and slow memory systems improve adaptation without catastrophic interference?

## Replay

AI question:

> Which experiences should an artificial system replay, and when?

Potential mechanisms:

- surprise
- novelty
- uncertainty
- reward
- interference
- information gain

## Forgetting

Biological memory forgets aggressively.

Research question:

> Can controlled forgetting improve AI memory by reducing interference and retrieval noise?

## Associative discovery

Research question:

> Can structured associative memory improve cross-domain reasoning and scientific hypothesis generation?

## Neuromodulatory control

Research question:

> Can learned global control signals dynamically change learning, retrieval, or computation based on uncertainty or task state?

## Active cognition

Research question:

> Can an agent learn when to retrieve, reason, search externally, or ask for more information?

This connects executive control, active inference, and agentic AI.

---

# 9. Cross-cutting philosophy and consciousness thread

Philosophy should remain a secondary but persistent thread throughout the program.

It should inform conceptual clarity rather than become an isolated detour.

Relevant questions include:

- What counts as a representation?
- What makes a system cognitive?
- What distinguishes simulation from explanation?
- Are higher-level concepts reducible to lower-level mechanisms?
- What is emergence?
- What makes consciousness different, if anything, from other emergent phenomena?
- What kinds of evidence could distinguish theories of consciousness?

Potential areas:

- functionalism
- predictive processing
- global workspace theory
- integrated information theory
- higher-order theories
- embodied cognition
- extended mind
- emergence
- levels of explanation

These questions should be connected to computational projects where possible.

Example:

> If consciousness requires global availability of information, what computational properties does "global availability" imply?

The objective is not to solve consciousness within three years.

The objective is to use philosophical analysis to sharpen scientific questions.

---

# 10. Reading program

Reading should support projects rather than become a separate curriculum.

## Stage 1

Favor textbooks and foundational explanations.

Possible sources:

- introductory neuroscience
- computational neuroscience textbooks
- canonical neuron-model papers
- neural dynamics tutorials

## Stage 2

Shift toward review articles and primary research.

Focus areas:

- memory
- predictive coding
- attention
- decision making
- transformers
- mechanistic interpretability
- continual learning
- AI agents

## Stage 3

Reading should be dominated by literature directly relevant to the selected research question.

## Stage 4

Reading becomes continuous literature surveillance around the research niche.

---

# 11. Suggested knowledge map

The overall program should gradually cover the following areas.

## Neurobiology

- membrane electrophysiology
- synapses
- neurotransmission
- plasticity
- neuromodulation
- neural circuits

## Systems neuroscience

- cortex
- hippocampus
- basal ganglia
- thalamus
- cerebellum
- sensory systems
- executive networks

## Cognitive neuroscience

- memory
- attention
- learning
- decision making
- perception
- executive control

## Computational neuroscience

- neuron models
- dynamical systems
- coding
- recurrent networks
- attractors
- Bayesian models
- predictive processing
- reinforcement learning

## AI

- deep learning
- transformers
- reinforcement learning
- representation learning
- retrieval
- continual learning
- agents
- memory systems
- interpretability

## Mathematics

- linear algebra
- probability
- optimization
- differential equations
- dynamical systems
- information theory
- statistics

## Philosophy

- philosophy of mind
- consciousness
- emergence
- representation
- intelligence
- epistemology

Depth should be driven by research need rather than completeness.

---

# 12. Project-specification template

Every detailed project plan derived from this roadmap should contain approximately the following sections.

## 1. Position within roadmap

Specify:

- stage
- timeline
- expected hours
- dependencies
- downstream role

## 2. Project thesis

State the central purpose in one or two paragraphs.

## 3. Learning or research objectives

Define what should be understood or demonstrated.

## 4. Scope

List:

- required concepts
- required models
- required experiments

## 5. Explicit non-goals

Protect the project from unnecessary expansion.

## 6. Core experiments

For every experiment define:

- question
- manipulation
- expected observation
- concept learned
- validation method

## 7. Deliverables

Examples:

- notebook
- software module
- experiment report
- literature review
- synthesis document

## 8. Architecture

Specify only the software organization needed for the project's objectives.

## 9. Timeline

Break the project into:

- weeks
- milestones
- approximate hours

## 10. Validation

Include:

- scientific validation
- numerical validation
- experimental baselines
- reproducibility requirements

## 11. Completion criteria

State exactly when the project should stop.

## 12. Connection to later stages

Explain which concepts or artifacts will be reused later.

---

# 13. Research-quality ladder

The program should deliberately increase rigor over time.

## Level 1: Educational reproduction

Typical Stage 1.

Characteristics:

- known model
- known expected behavior
- objective is understanding

Example:

> Reproduce an action potential using Hodgkin–Huxley.

## Level 2: Comparative experiment

Typical Stage 2.

Characteristics:

- compare mechanisms
- controlled variables
- synthesis across fields

Example:

> Compare biological attractor memory with vector retrieval on corrupted-pattern recovery.

## Level 3: Research-shaped experiment

Typical Stage 3.

Characteristics:

- explicit hypothesis
- strong baselines
- measurable outcome
- ablations

Example:

> Test whether replay-based consolidation improves delayed recall in an agent.

## Level 4: Original research

Typical Stage 4.

Characteristics:

- novel method or finding
- literature positioning
- rigorous evaluation
- reproducible results
- external communication

The program should not force Stage 1 projects to meet Stage 4 standards.

---

# 14. Infrastructure philosophy

Software engineering is a means, not the objective.

Prefer:

- Python
- Jupyter
- small reusable libraries
- configuration-driven experiments
- pytest
- Git
- GitHub
- lightweight experiment logging

Introduce heavier infrastructure only when experiments require it.

Potential later tools:

- PyTorch
- Hugging Face
- vector databases
- experiment trackers
- cloud GPUs
- distributed execution

Do not introduce them simply because they are standard industry tools.

---

# 15. Portfolio strategy

Each major project should ideally create one artifact that can eventually be shared.

Possible public outputs:

## Stage 1

- educational repository
- technical notebook
- explanatory article

## Stage 2

- brain–AI comparison essay
- memory-systems survey
- experimental prototype

## Stage 3

- research report
- benchmark
- reproducible experiment repository

## Stage 4

- preprint
- workshop paper
- mature open-source research project

Public release is optional during early learning.

Quality should take priority over frequency.

---

# 16. Decision checkpoints

## Month 3

Ask:

- Is computational neuroscience engaging enough to continue?
- Which topics felt most intuitive?
- Which mathematical gaps need attention?

Do not substantially change the roadmap yet unless motivation strongly shifts.

## Month 6

Ask:

- Which biological mechanisms seem most computationally interesting?
- Is memory still the strongest candidate?
- Which Stage 2 comparisons deserve more depth?

## Month 10–12

Begin ranking possible research directions.

Evaluate:

- novelty
- feasibility
- compute
- available benchmarks
- personal interest
- relevance to frontier AI

## Month 14

Choose the Stage 3 research question.

## Month 20

Ask:

- Is the hypothesis producing meaningful evidence?
- Is the methodology sound?
- Should the research question narrow or change?

## Month 24

Choose the Stage 4 direction based on evidence rather than initial preference.

## Month 30

Decide whether the project merits:

- further research
- external collaboration
- workshop submission
- preprint

---

# 17. What success looks like after three years

The goal is not merely to know neuroscience terminology.

A successful outcome would be the ability to:

- read neuroscience and AI papers critically
- move between biological and computational levels of explanation
- implement models from technical descriptions
- design experiments
- identify useful abstractions
- avoid superficial brain–AI analogies
- formulate falsifiable hypotheses
- build systems that test those hypotheses
- analyze experimental evidence
- communicate research clearly
- contribute an original idea or result

The ideal final skill is:

> the ability to look at an unsolved AI problem, understand how biological systems approach a related computational problem, and design a rigorous experiment testing whether that principle transfers.

---

# 18. Compact roadmap

```text
YEAR 1
│
├── Stage 1 — Foundations (Months 0–6)
│   ├── Project 1: Individual neuron models
│   │   ├── LIF
│   │   ├── Izhikevich
│   │   └── Hodgkin–Huxley
│   │
│   └── Project 2: Learning and small neural systems
│       ├── synapses
│       ├── Hebbian learning
│       ├── Oja's rule
│       ├── STDP
│       ├── recurrent dynamics
│       └── attractor memory
│
├── Stage 2 — Brains vs AI (Months 6–14)
│   ├── Project 3: Brain–transformer computational map
│   ├── Project 4: Biological and AI memory systems
│   └── Project 5: Attention, control, and active cognition
│
YEAR 2
│
├── Stage 3 — Research Apprenticeship (Months 14–24)
│   ├── literature review
│   ├── hypothesis
│   ├── benchmark
│   ├── baselines
│   ├── implementation
│   ├── controlled experiments
│   ├── ablations
│   └── paper-style report
│
YEAR 3
│
└── Stage 4 — Independent Research (Months 24–36)
    ├── refine research question
    ├── reproduce closest prior work
    ├── develop novel mechanism
    ├── run rigorous evaluation
    ├── test generalization
    ├── analyze failures
    ├── produce research repository
    └── paper / preprint / workshop submission
```

---

# 19. Guiding principle

At every point in the roadmap, prefer the smallest project that answers the current question.

Avoid:

> "What impressive system could I build?"

Prefer:

> "What is the smallest experiment that would teach me whether this computational hypothesis is true?"

That principle should keep the three-year program focused on learning and research rather than infrastructure accumulation.
