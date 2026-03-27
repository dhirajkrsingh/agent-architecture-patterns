# Agent Architecture Patterns

> **Design patterns for building intelligent agents — from reactive to BDI to hybrid.**

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://python.org)
[![Level](https://img.shields.io/badge/Level-Intermediate-C96E12)](#)
[![Track](https://img.shields.io/badge/Track-Agent%20Systems-0A7EA4)](#)

## Architectures Covered

This repository is the design-pattern layer of the agent track.

Use it after [multi-agent-system-basics](https://github.com/dhirajkrsingh/multi-agent-system-basics) if you want to understand how different agent decision models are structured.

## What You Will Learn

By the end of this repository, you should be able to:

- distinguish reactive, BDI, layered, and utility-based agent styles
- choose an architecture based on the problem rather than on hype
- understand where fast response, planning, and trade-off reasoning fit into agent design

## Prerequisites

Recommended before starting:

- [multi-agent-system-basics](https://github.com/dhirajkrsingh/multi-agent-system-basics)
- basic Python familiarity

## Recommended Next Repositories

Continue with:

- [autonomous-agent-design](https://github.com/dhirajkrsingh/autonomous-agent-design) for agent loops, self-correction, and goal-directed behavior
- [agent-planning-reasoning](https://github.com/dhirajkrsingh/agent-planning-reasoning) for planning and deliberate reasoning structures

| Pattern | Complexity | When to Use |
|---------|-----------|-------------|
| **Reactive** | Low | Fast response, no planning needed |
| **BDI (Belief-Desire-Intention)** | High | Goal-driven, deliberative agents |
| **Layered/Hybrid** | Medium | Combine reactive speed with deliberation |
| **Utility-Based** | Medium | Decisions require tradeoff analysis |

## Examples

| File | Description |
|------|-------------|
| [`examples/01_reactive_agent.py`](examples/01_reactive_agent.py) | Subsumption-style reactive layers |
| [`examples/02_bdi_agent.py`](examples/02_bdi_agent.py) | Belief-Desire-Intention architecture |
| [`examples/03_utility_agent.py`](examples/03_utility_agent.py) | Utility function-based decision making |

## Best Practices

1. **Match architecture to problem** — Don't use BDI for simple reflexes
2. **Separate perception from action** — Keep sensor processing and actuators modular
3. **Use state machines for reactive layers** — Finite state machines are debuggable
4. **Test each layer independently** — Layered architectures should have isolated tests
5. **Profile decision time** — Ensure deliberation doesn't cause real-time violations

## References

| Resource | Description |
|----------|-------------|
| [Brooks - Subsumption Architecture](https://people.csail.mit.edu/brooks/) | Reactive robotics pioneer |
| [jason-lang/jason](https://github.com/jason-lang/jason) | BDI agent programming in AgentSpeak |
| [AIMA Chapter 2](https://aima.cs.berkeley.edu/) | Russell & Norvig agent architectures |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | Modern agent framework |

---

## Author

Dhiraj Singh

## Usage Notice

This repository is shared publicly for learning and reference.
It is made available for everyone through [VAIU Research Lab](https://vaiu.ai/Research_Lab).
For reuse, redistribution, adaptation, or collaboration, contact Dhiraj Singh / [VAIU Research Lab](https://vaiu.ai/Research_Lab).
