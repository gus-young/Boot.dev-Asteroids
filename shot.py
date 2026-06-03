from circleshape import CircleShape
import pygame
import constants


class Shot(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, constants.LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)
        out_of_bounds = False
        if self.position.x > constants.SCREEN_WIDTH or self.position.x < 0:
            out_of_bounds = True
        if self.position.y > constants.SCREEN_HEIGHT or self.position.y < 0:
            out_of_bounds = True
        if out_of_bounds: 
            self.kill()