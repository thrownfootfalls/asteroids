# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import * # I've been instructed not to worry about the wildcard for this project
from player import Player

def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # draw on the screen
        pygame.Surface.fill(screen, (0,0,0))
        player.draw(screen) # draw the player's ship
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
