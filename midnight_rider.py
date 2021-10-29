# Midnight Rider

import sys
import textwrap
import time
import midnight_rider_text

# A text-based game of intrigue and illusion


class Game:
    """Represent our game engine

    Attribute:
        done: describes the game is finished or not - boolean
        distance_traveled: describe the distance that we've traveled so far this game in km
        amount_of_tofu: how much tofu we have left in our inventory
        agents_distance: describe the distance between the player and the agents
    """
    def __init__(self):
        self.done = False
        self.distance_traveled = 0
        self.amount_tofu = 3
        self.agents_distance = -20


    def introduction(self) -> None:
        """Print the introduction text"""
        print(midnight_rider_text.INTRODUCTION)
        self.typewriter_effect(midnight_rider_text.INTRODUCTION)

    def typewriter_effect(self, text: str) -> None:
        """Print out to console with a typewriter effect"""
        for char in textwrap.dedent(text):
            time.sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()

    def show_choices(self) -> None:
        """Show the user their choices"""
        time.sleep(1)
        print(midnight_rider_text.CHOICES)
        time.sleep(1)

    def get_choice(self) -> None:
        """Gets the user's choice and changes the environment"""
        # Get the user's response
        user_choice = input().lower().strip("?!.,")

        # Based on their choice, change the attributes of the class
        if user_choice == "e":
            print("---Status Check---")
            # print out distance traveled
            print(f"Distance Traveled: {self.distance_traveled}")
            # print out amount of tofu left
            print(f"Tofu pieces left: {self.amount_tofu}")
            # print out agent distance
            print(f"Agent's distance: {abs(self.agents_distance)} km behind")
            print("---------------------------------")
            time.sleep(2)
        elif user_choice == "q":
            self.done = True


def main() -> None:
    game = Game()    # Starting a new game
    # game.introduction()

    while not game.done:
        game.show_choices()
        # TODO: Ask the player what they want to do
        game.get_choice()
        # TODO: Check win/lose condition


if __name__ == "__main__":
    main()
