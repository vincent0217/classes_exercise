# Pygame_Drawing
# Author: Vincent
# November 9 2021

# Get introduced to Pygame and draw objects on screen

import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (  0,   0, 0)
RED   = (255,   0, 0)
GREEN = (  0, 255, 0)
BLUE  = (  0, 0, 255)

SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE   = (SCREEN_HEIGHT, SCREEN_WIDTH)
WINDOW_TITLE  = "Pygame Drawing"

def main() -> None:
    """Driver of the Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()

    # ----------- MAIN LOOP
    while not done:
        # ----------- EVENT LISTENER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True


        # # ----------- CHANGE THE ENVIRONMENT


        # ----------- DRAW THE ENVIRONMENT
        screen.fill(WHITE)  # fil the bg-colour
        for i in range(10):
            pygame.draw.rect(screen, RED, [100 + i * 10, 100 + i * 10, 75, 30])

        pygame.draw.circle(screen, GREEN, center=(110, 110), radius=30)

        # Update the screen
        pygame.display.flip()

        # ----------- CLOCK TICK
        clock.tick(60)


if __name__ == "__main__":
    main()
