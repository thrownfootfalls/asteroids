import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        """Kill this asteroid and, if large enough, return smaller ones."""
        self.kill() # It seems the rest of this code still runs, though.
        if self.radius <= ASTEROID_MIN_RADIUS:
            return []
        random_angle = random.uniform(20,50)
        angles = [self.velocity.rotate(random_angle),
                    self.velocity.rotate(-random_angle)]
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroids = [Asteroid(*self.position, new_radius)
                            for i in range(len(angles))]
        for asteroid, angle in zip(new_asteroids, angles):
            asteroid.velocity = angle
            asteroid.velocity *= 1.2
        return new_asteroids

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
