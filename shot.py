from circleshape import CircleShape
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 200, 0), (int(self.position.x), int(self.position.y)), self.radius, 2) # Draw the shot in green

    def update(self, dt):
        self.position += self.velocity * dt  # Update position based on velocity