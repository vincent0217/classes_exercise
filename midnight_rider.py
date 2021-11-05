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
MAX_HUNGER = 50

ENDGAME_REASONS = {
    "LOSE_AGENTS": 1,
    "LOSE_FUEL": 2,
    "LOSE_HUNGER": 3,

}


class Game:
    """Represent our game engine

    Attribute:
        done: describes the game is finished or not - boolean
        distance_traveled: describe the distance that we've traveled so far this game in km
        amount_of_tofu: how much tofu we have left in our inventory
        agents_distance: describe the distance between the player and the agents
        fuel: describes the amount of fuel remaining,
              starts off at 50
        huger: describes how hungry our player is, represented by a number 0-50,
               if unger goes beyond 50, game is over
        endgame_reason: shows the index of the game ending text from midnight_rider_text.py
    """
    def __init__(self):
        self.done = False
        self.distance_traveled = 0
        self.amount_tofu = MAX_TOFU
        self.agents_distance = -20
        self.fuel = MAX_FUEL
        self.hunger = 0
        self.endgame_reason = 0

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

        agents_distance_now = random.randrange(7, 15)
        # TODO: Implement eating/hunger
        if user_choice == "a":
            # Consume one tofu IF and ONLY IF we have some available
            if self.amount_tofu > 0:
                self.amount_tofu -= 1
                self.hunger = 0
                # TODO: Add text to midnight_rider_text.py
                print(midnight_rider_text.EAT_TOFU)
            else:
                # Tell the player they don't have tofu
                print(midnight_rider_text.NO_TOFU)
        elif user_choice == "b":
            # Move the player slowly
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
            # Move the player quickly
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
            time.sleep(1.5)
        elif user_choice == "q":
            self.done = True

        # Increase hunger
        if user_choice in ["b", "c", "d"]:
            self.hunger += random.randrange(8, 18)

    def upkeep(self) -> None:
        """Give the user reminders of hunger"""
        if self.hunger > 40:
            print(midnight_rider_text.SEVERE_HUNGER)
        elif self.hunger > 25:
            print(midnight_rider_text.HUNGER)

        time.sleep(1)

    def check_endgame(self) -> None:
        """Check to see if win/lose conditions are met.
           If they are met, change the self.done flag."""
        # TODO: LOSE - Agents catch up to the player
        if self.agents_distance >= 0:
            # Allows us to quit the while loop
            self.done = True
            # Helps with pairing the right ending
            self.endgame_reason = ENDGAME_REASONS["LOSE_AGENTS"]
        # TODO: LOSE - Fuel runs out
        if self.fuel <= 0:
            self.done = True

            self.endgame_reason = ENDGAME_REASONS["LOSE_FUEL"]
        # TODO: LOSE - Perish because of hunger
        if self.hunger >= 50:
            self.done = True

            self.endgame_reason = ENDGAME_REASONS["LOSE_HUNGER"]
        # TODO: WIN - Reach the goal


def main() -> None:
    game = Game()    # Starting a new game
    # game.introduction()

    while not game.done:
        game.upkeep()
        game.show_choices()
        # TODO: Ask the player what they want to do
        game.get_choice()
        game.check_endgame()

    time.sleep(3)
    # Print out the ending
    game.typewriter_effect(
        midnight_rider_text.ENDGAME_TEXT[game.endgame_reason]
    )


if __name__ == "__main__":
    main()
