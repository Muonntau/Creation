from angel_rpg import Player, Game


def main():
    name = input("Enter your angel's name: ").strip() or "Unnamed Angel"
    player = Player(name)
    game = Game(player)
    game.run()


if __name__ == "__main__":
    main()
