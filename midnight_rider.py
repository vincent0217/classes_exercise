# Midnight Rider

import random
import sys
import textwrap
import time
import midnight_rider_text

# A text-based game of intrigue and illusion

# CONSTANTS
MAX_TOFU = 3
MAX_FUEL = 50


class Game:
    """Represent our game engine

    Attribute:
        done: describes the game is finished or not - boolean
        distance_traveled: describe the distance that we've traveled so far this game in km
        amount_of_tofu: how much tofu we have left in our inventory
        agents_distance: describe the distance between the player and the agents
        fuel: describes the amount of fuel remaining,
              starts off at 50
    """
    def __init__(self):
        self.done = False
        self.distance_traveled = 0
        self.amount_tofu = MAX_TOFU
        self.agents_distance = -20
        self.fuel = MAX_FUEL


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

        # TODO: Implement eating/hunger
        agents_distance_now = random.randrange(7, 15)
        if user_choice == "b":
            # Move the player
            player_distance_now = random.randrange(0, 8)
            self.distance_traveled += player_distance_now

            # Move the agents
            self.agents_distance += agents_distance_now - player_distance_now

            # Burn the fuel
            self.fuel -= random.randrange(1, 6)

            # Give the player some feedback
            print(f"\n-------------Mehhhhhhhhhhhh")
            print(f"---------------You traveled {player_distance_now} km.")

        # TODO: Implement slow traveling
        elif user_choice == "c":
            # Move the player
            player_distance_now = random.randrange(10, 16)
            self.distance_traveled += player_distance_now

            # Move the agents
            self.agents_distance += agents_distance_now - player_distance_now

            # Burn the fuel
            self.fuel -= random.randrange(5, 11)

            # Give the player some feedback
            print(f"\n-------------ZOOOOOOOOOOOM")
            print(f"---------------You traveled {player_distance_now} km.")

        elif user_choice == "d":
            self.fuel = MAX_FUEL
            # Decide how far the agents go
            self.agents_distance += random.randrange(7, 15)
            # Give the user feedback
            print(midnight_rider_text.REFUEL)
            time.sleep(2)
        elif user_choice == "e":
            print("---Status Check---")
            print(f"Distance Traveled: {self.distance_traveled} km")
            print(f"Fuel remaining: {self.fuel} L")
            print(f"Tofu pieces left: {self.amount_tofu} pieces")
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
