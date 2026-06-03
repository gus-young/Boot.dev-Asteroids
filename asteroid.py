import pygame
import constants
import logger
import random
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, constants.LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else: 
            logger.log_event("asteroid_split")
            rand_angle = random.uniform(20,50)
            v_asteroid_one = self.velocity.rotate(rand_angle)
            v_asteroid_two = self.velocity.rotate(-rand_angle)
            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
            asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_one.velocity = v_asteroid_one * 1.5
            asteroid_two.velocity = v_asteroid_two * 1.5