class Player:
    """Represents the angelic player."""

    def __init__(self, name: str, energy: int = 10):
        self.name = name
        self.karma = 0
        self.energy = energy

    def can_perform(self, task) -> bool:
        return self.energy >= task.energy_cost

    def perform_task(self, task):
        if not self.can_perform(task):
            raise ValueError("Not enough energy to perform this task.")
        self.energy -= task.energy_cost
        self.karma += task.karma_reward

    def __str__(self):
        return f"{self.name} (Karma: {self.karma}, Energy: {self.energy})"
