# Midnight Rider

import midnight_rider_text

# A text-based game of intrigue and illusion


class Game:
    """Represent our game engine

    """
    def introduction(self) -> None:
        """Print the introduction text"""
        print(midnight_rider_text.INTRODUCTION)


def main() -> None:
    game = Game() # Starting a new game
    game.introduction()


if __name__ == "__main__":
    main()
