from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
import pygame # ok to do it again here?

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown = 0

    # define the triangle shape of the player's appearance
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        # from exercise spec
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shot = Shot(*self.position) # will the * work?
        shot.velocity = pygame.Vector2((0,1)) * PLAYER_SHOOT_SPEED
        shot.velocity = shot.velocity.rotate(self.rotation)
        return shot # but really this needs to go into the shots group

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shoot_cooldown -= dt
        shot = None

        if keys[pygame.K_a]:
            self.rotate(-dt) # turn left
        if keys[pygame.K_d]:
            self.rotate(dt) # turn right
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE] and self.shoot_cooldown <= 0:
            # fire, but only if enough time has passed since the last shot
            self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN
            shot = self.shoot()
#            print("Pew!")
        return shot
