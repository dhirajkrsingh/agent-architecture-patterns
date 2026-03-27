"""
Example 3: Utility-Based Agent
================================
An agent that makes decisions by computing utility scores for each available action.
The action with the highest expected utility is selected.

Run: python examples/03_utility_agent.py
"""


class UtilityAgent:
    """An agent that selects actions based on expected utility."""

    def __init__(self, name: str):
        self.name = name
        self.utility_functions = {}
        self.weights = {}

    def register_action(self, action: str, utility_fn, weight: float = 1.0):
        """Register an action with its utility function and weight."""
        self.utility_functions[action] = utility_fn
        self.weights[action] = weight

    def compute_utilities(self, state: dict) -> dict:
        """Compute utility for each action given current state."""
        utilities = {}
        for action, fn in self.utility_functions.items():
            raw_utility = fn(state)
            weighted = raw_utility * self.weights[action]
            utilities[action] = round(weighted, 3)
        return utilities

    def decide(self, state: dict) -> str:
        """Select the action with highest utility."""
        utilities = self.compute_utilities(state)
        best_action = max(utilities, key=utilities.get)

        print(f"  [{self.name}] Utility scores:")
        for action, utility in sorted(utilities.items(), key=lambda x: -x[1]):
            marker = " <-- SELECTED" if action == best_action else ""
            print(f"    {action}: {utility}{marker}")

        return best_action


# Utility functions for different actions
def explore_utility(state: dict) -> float:
    """Exploration is more valuable when knowledge is low and resources are high."""
    knowledge = state.get("knowledge_level", 0.5)
    energy = state.get("energy", 0.5)
    return (1 - knowledge) * energy


def exploit_utility(state: dict) -> float:
    """Exploitation is valuable when knowledge is high."""
    knowledge = state.get("knowledge_level", 0.5)
    resources = state.get("nearby_resources", 0)
    return knowledge * min(resources / 10, 1.0)


def rest_utility(state: dict) -> float:
    """Resting is important when energy is low."""
    energy = state.get("energy", 0.5)
    return max(0, 1 - energy * 2)


def communicate_utility(state: dict) -> float:
    """Communication is valuable when there are nearby agents and new information."""
    nearby_agents = state.get("nearby_agents", 0)
    knowledge = state.get("knowledge_level", 0.5)
    return (nearby_agents / 5) * knowledge


if __name__ == "__main__":
    print("=== Utility-Based Agent Demo ===\n")

    agent = UtilityAgent("Explorer")
    agent.register_action("explore", explore_utility, weight=1.2)
    agent.register_action("exploit", exploit_utility, weight=1.0)
    agent.register_action("rest", rest_utility, weight=1.5)
    agent.register_action("communicate", communicate_utility, weight=0.8)

    scenarios = [
        {"name": "Fresh start", "state": {"knowledge_level": 0.1, "energy": 0.9, "nearby_resources": 2, "nearby_agents": 1}},
        {"name": "Found resources", "state": {"knowledge_level": 0.8, "energy": 0.7, "nearby_resources": 8, "nearby_agents": 0}},
        {"name": "Exhausted", "state": {"knowledge_level": 0.5, "energy": 0.1, "nearby_resources": 3, "nearby_agents": 2}},
        {"name": "Social opportunity", "state": {"knowledge_level": 0.7, "energy": 0.6, "nearby_resources": 1, "nearby_agents": 4}},
    ]

    for s in scenarios:
        print(f"\n  Scenario: {s['name']} | State: {s['state']}")
        action = agent.decide(s["state"])
        print(f"  Decision: {action}\n")
