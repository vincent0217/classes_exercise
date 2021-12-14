# Collecting Blocks Example
# Author: Vincent

import random
import time
import pygame
pygame.init()
WHITE =     (255, 255, 255)
BLACK =     (  0,   0,   0)
RED   =     (255,   0,   0)
GREEN =     (  0, 255,   0)
BLUE  =     (  0,   0, 255)
ETON_BLUE = (135, 187, 162)
RAD_RED =   (255,  56, 100)
BLK_CHOCOLATE = (25, 17, 2)
BGCOLOUR =  WHITE
SCREEN_WIDTH =  800
SCREEN_HEIGHT = 600
SCREEN_SIZE   = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE  = "Collecting Blocks"


class Player(pygame.sprite.Sprite):
    """Describes a player object
    A subclass of pygame.sprite.Sprite
    Attributes:≤
        image: Surface that is the visual
            representation of our Block
        rect: numerical representation of
            our Block [x, y, width, height]
        hp: describe how much health our
            player has
    """
    def __init__(self) -> None:
        # Call the superclass constructor
        super().__init__()
        # Create the image of the block
        self.image = pygame.image.load("./images/smb_mario.png")
        self.image = pygame.transform.scale(self.image, (48, 64))
        # Based on the image, create a Rect for the block
        self.rect = self.image.get_rect()
        # Initial health points
        self.hp = 250

    def hp_remaining(self) -> float:
        """Return the percent of health remaining"""
        return self.hp / 250


class Enemy(pygame.sprite.Sprite):
    """The enemy sprites
    Attributes:
        image: Surface that is the visual representation
        rect: Rect (x, y, width, height)
        x_vel: x velocity
        y_vel: y velocity
    """
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./images/spaceinvaders.png")
        # Resize the image (scale)
        self.image = pygame.transform.scale(self.image, (56, 40))
        self.rect = self.image.get_rect()
        # Define the initial location
        self.rect.x, self.rect.y = (
            random.randrange(SCREEN_WIDTH),
            random.randrange(SCREEN_HEIGHT)
        )
        # Define the initial velocity
        self.x_vel = random.choice([-4, -3, 3, 4])
        self.y_vel = random.choice([-4, -3, 3, 4])

    def update(self) -> None:
        """Calculate movement"""
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel
        # Constrain movement
        # X -
        if self.rect.left < 0:
            self.rect.x = 0
            self.x_vel = -self.x_vel    # bounce
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.x_vel = -self.x_vel    # bounce
        # Y -
        if self.rect.y < 0:
            self.rect.y = 0
            self.y_vel = -self.y_vel
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.y_vel = -self.y_vel


class Bullet(pygame.sprite.Sprite):
    """Bullet
    Attributes:
        image: visual representation
        rect: mathematical representation (hit box)
        vel_y: y velocity in px/sec
    """
    def __init__(self, coords: tuple):
        """
        Arguments:
            coords: tuple of (x,y) to represent initial location
        """
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        # Set the middle of the bullet to be at coords
        self.rect.center = coords

        self.vel_y = 3

    def update(self):
        self.rect.y -= self.vel_y


def main() -> None:
    """Driver of the Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)
    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()
    num_enemies = 15
    score = 0
    time_start = time.time()
    time_invincible = 5             # seconds
    game_state = "running"
    endgame_cooldown = 5            # seconds
    time_ended = 0.0
    endgame_messages = {
        "win": "Congratulations, you won!",
        "lose": "Sorry, they got you. Play again!",
    }
    font = pygame.font.SysFont("Arial", 25)
    pygame.mouse.set_visible(False)
    # Create groups to hold Sprites
    all_sprites = pygame.sprite.Group()
    enemy_sprites = pygame.sprite.Group()
    bullet_sprites = pygame.sprite.Group()

    # Create enemy sprites
    for i in range(num_enemies):
        # Create an enemy
        enemy = Enemy()
        # Add it to the sprites list (enemy_sprites and all_sprites)
        enemy_sprites.add(enemy)
        all_sprites.add(enemy)
    # Create the Player block
    player = Player()
    # Add the Player to all_sprites group
    all_sprites.add(player)
    pygame.mouse.set_visible(True)
    # ----------- MAIN LOOP
    while not done:
        # ----------- EVENT LISTENER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONUP:
                if len(bullet_sprites) < 3 and time.time() - time_start > time_invincible:
                    bullet = Bullet(player.rect.midtop)

                    bullet_sprites.add(bullet)
                    all_sprites.add(bullet)

        # TODO: LOSE CONDITION - Player's hp goes below 0
        if player.hp_remaining() <= 0:
            done = True
        # ----------- CHANGE ENVIRONMENT
        # Process player movement based on mouse pos
        mouse_pos = pygame.mouse.get_pos()
        player.rect.x = mouse_pos[0] - player.rect.width / 2
        player.rect.y = mouse_pos[1] - player.rect.height / 2
        # Update the location of all sprites
        all_sprites.update()
        # Check all collisions between player and the ENEMIES
        enemies_collided = pygame.sprite.spritecollide(player, enemy_sprites, False)
        # Set a time for invincibility at the beginning of the game
        if time.time() - time_start > time_invincible and game_state != "won":
            for enemy in enemies_collided:
                player.hp -= 1

        # Check bullet collisions with enemies
        # Kill the bullets when they've left the screen
        for bullet in bullet_sprites:
            enemies_bullet_collided = pygame.sprite.spritecollide(
                bullet,
                enemy_sprites,
                True
            )

            # If the bullet has struck some enemy
            if len(enemies_bullet_collided) > 0:
                bullet.kill()
                score += 1

            if bullet.rect.y < 0:
                bullet.kill()

        # ----------- DRAW THE ENVIRONMENT
        screen.fill(BGCOLOUR)      # fill with bgcolor

        # Draw all sprites
        all_sprites.draw(screen)
        # Draw the score on the screen
        screen.blit(
            font.render(f"Score: {score}", True, BLACK),
            (5, 5)
        )
        # Draw a health bar
        # Draw the background rectangle
        pygame.draw.rect(screen, GREEN, [580, 5, 215, 20])
        # Draw the foreground rectangle which is the remaining health
        life_remaining = 215 - int(215 * player.hp_remaining())
        pygame.draw.rect(screen, BLUE, [580, 5, life_remaining, 20])
        # If we've won, draw the text on the screen
        if game_state == "won":
            screen.blit(
                font.render(endgame_messages["win"], True, BLACK),
                (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
            )
        # Update the screen
        pygame.display.flip()
        # ----------- CLOCK TICK
        clock.tick(75)


if __name__ == "__main__":
    main()
