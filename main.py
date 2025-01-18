# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import * # I've been instructed not to worry about the wildcard for this project
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField() # any worries about asteroidfield name?

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for item in updatable:
            item.update(dt)
        #player.update(dt)

        # draw on the screen
        pygame.Surface.fill(screen, (0,0,0))
        for item in drawable:
            item.draw(screen)
        #player.draw(screen) # draw the player's ship
        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
