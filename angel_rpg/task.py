class Task:
    """Represents a task the angel can perform."""

    def __init__(self, name: str, karma_reward: int, energy_cost: int,
                 description: str = ""):
        self.name = name
        self.karma_reward = karma_reward
        self.energy_cost = energy_cost
        self.description = description

    def __str__(self) -> str:
        desc = f" - {self.description}" if self.description else ""
        return f"{self.name}{desc} (Karma: +{self.karma_reward}, Energy Cost: {self.energy_cost})"
