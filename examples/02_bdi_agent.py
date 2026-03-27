"""
Example 2: BDI Agent (Belief-Desire-Intention)
================================================
The gold standard for deliberative agents.
- Beliefs: What the agent knows about the world
- Desires: What the agent wants to achieve
- Intentions: What the agent has committed to doing

Run: python examples/02_bdi_agent.py
"""


class BDIAgent:
    """A Belief-Desire-Intention agent that reasons about goals and plans."""

    def __init__(self, name: str):
        self.name = name
        self.beliefs = {}        # Current knowledge about the world
        self.desires = []        # Goals the agent wants to achieve
        self.intentions = []     # Plans the agent is committed to
        self.plan_library = {}   # Available plans indexed by goal

    def update_beliefs(self, percepts: dict):
        """Update beliefs from new percepts."""
        self.beliefs.update(percepts)
        print(f"  [{self.name}] Beliefs updated: {self.beliefs}")

    def add_desire(self, goal: str, priority: int = 1):
        """Add a new desire/goal."""
        self.desires.append({"goal": goal, "priority": priority})
        self.desires.sort(key=lambda d: d["priority"], reverse=True)

    def register_plan(self, goal: str, preconditions: dict, actions: list):
        """Register a plan in the plan library."""
        if goal not in self.plan_library:
            self.plan_library[goal] = []
        self.plan_library[goal].append({"preconditions": preconditions, "actions": actions})

    def deliberate(self):
        """Select intentions from desires based on current beliefs."""
        self.intentions = []
        for desire in self.desires:
            goal = desire["goal"]
            if goal in self.plan_library:
                for plan in self.plan_library[goal]:
                    if self._check_preconditions(plan["preconditions"]):
                        self.intentions.append({"goal": goal, "actions": plan["actions"]})
                        print(f"  [{self.name}] Intending: {goal} ({len(plan['actions'])} actions)")
                        break

    def _check_preconditions(self, preconditions: dict) -> bool:
        """Check if preconditions are met by current beliefs."""
        for key, value in preconditions.items():
            if self.beliefs.get(key) != value:
                return False
        return True

    def execute(self):
        """Execute current intentions."""
        for intention in self.intentions:
            print(f"\n  [{self.name}] Executing plan for: {intention['goal']}")
            for step, action in enumerate(intention["actions"], 1):
                print(f"    Step {step}: {action}")
            print(f"  [{self.name}] Goal '{intention['goal']}' achieved!")

    def run_cycle(self, percepts: dict):
        """Run one BDI reasoning cycle."""
        print(f"\n{'='*50}")
        self.update_beliefs(percepts)
        self.deliberate()
        self.execute()


if __name__ == "__main__":
    print("=== BDI Agent Demo ===")

    agent = BDIAgent("DeliveryBot")

    # Register plans
    agent.register_plan(
        goal="deliver_package",
        preconditions={"has_package": True, "route_clear": True},
        actions=["navigate_to_destination", "verify_recipient", "hand_over_package", "confirm_delivery"],
    )

    agent.register_plan(
        goal="deliver_package",
        preconditions={"has_package": True, "route_clear": False},
        actions=["find_alternate_route", "navigate_alternate", "verify_recipient", "hand_over_package"],
    )

    agent.register_plan(
        goal="recharge",
        preconditions={"battery_low": True},
        actions=["navigate_to_charger", "dock", "wait_for_charge"],
    )

    # Add desires
    agent.add_desire("deliver_package", priority=2)
    agent.add_desire("recharge", priority=3)

    # Cycle 1: Has package, route clear, battery ok
    agent.run_cycle({"has_package": True, "route_clear": True, "battery_low": False})

    # Cycle 2: Battery is low
    agent.run_cycle({"has_package": True, "route_clear": True, "battery_low": True})

    # Cycle 3: Route blocked
    agent.run_cycle({"has_package": True, "route_clear": False, "battery_low": False})
