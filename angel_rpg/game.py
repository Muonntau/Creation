import random
from typing import List
from .player import Player
from .task import Task
from .item import Item


ANGEL_ART = r'''
   .-.
  ((@))
   ) (    The Angel RPG
  /   \     Spread your wings!
  `""""`
'''

DEFAULT_TASKS = [
    Task("Help the poor", 10, 2, "Assist at a local shelter"),
    Task("Heal the sick", 15, 3, "Visit a hospital and heal patients"),
    Task("Guide the lost", 5, 1, "Provide directions to wandering souls"),
    Task("Protect the innocent", 8, 2, "Shield someone from harm"),
    Task("Inspire hope", 12, 2, "Give encouragement to those in despair"),
    Task("Deliver miracles", 20, 4, "Perform a small miracle for someone"),
    Task("Tend celestial gardens", 7, 1, "Water the flowers of heaven"),
    Task("Write inspirational verses", 9, 2, "Pen uplifting poetry"),
    Task("Spread peace", 11, 2, "Calm quarrelling souls"),
    Task("Clean the clouds", 4, 1, "Polish the silver linings"),
]

STORE_ITEMS = [
    Item(
        "Energy Potion",
        cost=10,
        energy_gain=5,
        description="Restore 5 energy",
    ),
    Item(
        "Wing Upgrade",
        cost=30,
        max_energy_gain=5,
        description="Increase max energy by 5",
    ),
]


class Game:
    def __init__(self, player: Player, tasks: List[Task] = None):
        self.player = player
        self.tasks = tasks or list(DEFAULT_TASKS)
        self.completion_messages = [
            "Your halo glows a little brighter!",
            "Another feather in your wings!",
            "The heavens cheer your good deeds.",
        ]

    def open_store(self):
        print("\n-- Heavenly Store --")
        print(f"You have {self.player.karma} karma to spend.")
        for idx, item in enumerate(STORE_ITEMS, 1):
            print(f"{idx}. {item}")
        choice = input("Select an item or press Enter to exit: ").strip()
        if not choice:
            return
        try:
            idx = int(choice) - 1
            if idx < 0 or idx >= len(STORE_ITEMS):
                raise ValueError
            item = STORE_ITEMS[idx]
            if self.player.karma < item.cost:
                print("Not enough karma.")
                return
            item.apply(self.player)
            print(f"You purchased {item.name}!")
        except ValueError:
            print("Invalid selection.")

    def _print_intro(self):
        print(ANGEL_ART)
        print(f"Welcome, {self.player.name}! You are an angel on Earth.")
        print(
            "Complete tasks to earn karma. "
            "Type the task number, 'r' to rest, 's' for the store, or 'q' to quit."
        )

    def choose_tasks(self) -> List[Task]:
        return random.sample(self.tasks, k=min(3, len(self.tasks)))

    def run(self):
        self._print_intro()
        while self.player.energy > 0:
            print(f"\n{self.player}")
            available = self.choose_tasks()
            for idx, task in enumerate(available, 1):
                print(f"{idx}. {task}")
            choice = input(
                "Choose a task ('r' rest, 's' store, 'q' quit): "
            ).strip().lower()
            if choice == 'q':
                break
            if choice == 'r':
                self.player.rest()
                print("You take a celestial breather. Ahh...")
                continue
            if choice == 's':
                self.open_store()
                continue
            try:
                idx = int(choice) - 1
                if idx < 0 or idx >= len(available):
                    raise ValueError
                task = available[idx]
                if self.player.can_perform(task):
                    self.player.perform_task(task)
                    print(f"You completed the task: {task.name}!")
                    print(random.choice(self.completion_messages))
                else:
                    print("You don't have enough energy for that task.")
            except ValueError:
                print("Invalid choice. Please select a valid task number.")
        print(f"\nGame over! Final stats: {self.player}")
