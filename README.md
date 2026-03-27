# Agent Architecture Patterns

> **Design patterns for building intelligent agents — from reactive to BDI to hybrid.**

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## Architectures Covered

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

**Author:** [Dhiraj Kumar Singh](https://github.com/dhirajkrsingh) — AI Trainer
