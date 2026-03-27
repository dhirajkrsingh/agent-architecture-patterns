"""
Example 1: Reactive Agent (Subsumption Architecture)
=====================================================
A layered reactive architecture where higher-priority behaviors suppress lower ones.
Inspired by Rodney Brooks' subsumption architecture for robotics.

Run: python examples/01_reactive_agent.py
"""


class Behavior:
    """A single reactive behavior with a priority level."""

    def __init__(self, name: str, priority: int):
        self.name = name
        self.priority = priority  # Higher = more important

    def is_applicable(self, percepts: dict) -> bool:
        raise NotImplementedError

    def execute(self, percepts: dict) -> str:
        raise NotImplementedError


class AvoidObstacle(Behavior):
    def __init__(self):
        super().__init__("AvoidObstacle", priority=3)

    def is_applicable(self, percepts: dict) -> bool:
        return percepts.get("obstacle_distance", 100) < 10

    def execute(self, percepts: dict) -> str:
        return "TURN_AWAY"


class FollowTarget(Behavior):
    def __init__(self):
        super().__init__("FollowTarget", priority=2)

    def is_applicable(self, percepts: dict) -> bool:
        return percepts.get("target_visible", False)

    def execute(self, percepts: dict) -> str:
        return "MOVE_TOWARD_TARGET"


class Wander(Behavior):
    def __init__(self):
        super().__init__("Wander", priority=1)

    def is_applicable(self, percepts: dict) -> bool:
        return True  # Always applicable as fallback

    def execute(self, percepts: dict) -> str:
        return "RANDOM_WALK"


class SubsumptionAgent:
    """Agent using subsumption architecture — higher priority behaviors suppress lower ones."""

    def __init__(self, name: str):
        self.name = name
        self.behaviors = []

    def add_behavior(self, behavior: Behavior):
        self.behaviors.append(behavior)
        self.behaviors.sort(key=lambda b: b.priority, reverse=True)

    def act(self, percepts: dict) -> str:
        for behavior in self.behaviors:
            if behavior.is_applicable(percepts):
                action = behavior.execute(percepts)
                print(f"  [{self.name}] {behavior.name}(p={behavior.priority}) -> {action}")
                return action
        return "IDLE"


if __name__ == "__main__":
    print("=== Subsumption Architecture Demo ===\n")

    robot = SubsumptionAgent("Robot")
    robot.add_behavior(AvoidObstacle())
    robot.add_behavior(FollowTarget())
    robot.add_behavior(Wander())

    scenarios = [
        {"name": "Clear path, target visible", "percepts": {"obstacle_distance": 50, "target_visible": True}},
        {"name": "Obstacle close!", "percepts": {"obstacle_distance": 5, "target_visible": True}},
        {"name": "Nothing around", "percepts": {"obstacle_distance": 100, "target_visible": False}},
        {"name": "Obstacle and no target", "percepts": {"obstacle_distance": 3, "target_visible": False}},
    ]

    for s in scenarios:
        print(f"  Scenario: {s['name']}")
        robot.act(s["percepts"])
        print()
