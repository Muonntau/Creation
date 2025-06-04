class Item:
    """Represents a purchasable item in the heavenly store."""

    def __init__(self, name: str, cost: int, energy_gain: int = 0,
                 max_energy_gain: int = 0, description: str = ""):
        self.name = name
        self.cost = cost
        self.energy_gain = energy_gain
        self.max_energy_gain = max_energy_gain
        self.description = description

    def apply(self, player):
        player.karma -= self.cost
        if self.max_energy_gain:
            player.max_energy += self.max_energy_gain
            player.energy = player.max_energy
        if self.energy_gain:
            player.energy = min(player.energy + self.energy_gain, player.max_energy)

    def __str__(self) -> str:
        desc = f" - {self.description}" if self.description else ""
        return f"{self.name}{desc} (Cost: {self.cost} karma)"
