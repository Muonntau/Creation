import random
from typing import List
from .player import Player
from .task import Task


DEFAULT_TASKS = [
    Task("Help the poor", 10, 2, "Assist at a local shelter"),
    Task("Heal the sick", 15, 3, "Visit a hospital and heal patients"),
    Task("Guide the lost", 5, 1, "Provide directions to wandering souls"),
    Task("Protect the innocent", 8, 2, "Shield someone from harm"),
    Task("Inspire hope", 12, 2, "Give encouragement to those in despair"),
]


class Game:
    def __init__(self, player: Player, tasks: List[Task] = None):
        self.player = player
        self.tasks = tasks or list(DEFAULT_TASKS)

    def choose_tasks(self) -> List[Task]:
        return random.sample(self.tasks, k=min(3, len(self.tasks)))

    def run(self):
        print(f"Welcome, {self.player.name}! You are an angel on Earth.")
        print("Complete tasks to earn karma. Type the task number to perform it or 'q' to quit.")
        while self.player.energy > 0:
            print(f"\n{self.player}")
            available = self.choose_tasks()
            for idx, task in enumerate(available, 1):
                print(f"{idx}. {task}")
            choice = input("Choose a task (or 'q' to quit): ").strip().lower()
            if choice == 'q':
                break
            try:
                idx = int(choice) - 1
                if idx < 0 or idx >= len(available):
                    raise ValueError
                task = available[idx]
                if self.player.can_perform(task):
                    self.player.perform_task(task)
                    print(f"You completed the task: {task.name}!")
                else:
                    print("You don't have enough energy for that task.")
            except ValueError:
                print("Invalid choice. Please select a valid task number.")
        print(f"\nGame over! Final stats: {self.player}")
