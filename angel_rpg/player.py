class Player:
    """Represents the angelic player."""

    def __init__(self, name: str, energy: int = 10, max_energy: int = 10):
        self.name = name
        self.karma = 0
        self.energy = energy
        self.max_energy = max_energy
        self.level = 1
        self._next_level = 50

    def can_perform(self, task) -> bool:
        return self.energy >= task.energy_cost

    def perform_task(self, task):
        if not self.can_perform(task):
            raise ValueError("Not enough energy to perform this task.")
        self.energy -= task.energy_cost
        self.karma += task.karma_reward
        self._check_level_up()

    def rest(self, amount: int = 2):
        """Restore some energy."""
        self.energy = min(self.energy + amount, self.max_energy)

    def _check_level_up(self):
        if self.karma >= self._next_level:
            self.level += 1
            self.max_energy += 2
            self.energy = self.max_energy
            self._next_level += 50 * self.level
            print(f"You ascended to level {self.level}! Max energy increased.")

    def __str__(self):
        return (
            f"{self.name} (Level: {self.level}, Karma: {self.karma}, "
            f"Energy: {self.energy}/{self.max_energy})"
        )
