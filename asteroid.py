from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (200, 200, 200), (int(self.position.x), int(self.position.y)), self.radius, 2)  # Draw the asteroid in gray

    def update(self, dt):
        self.position += self.velocity * dt  # Update position based on velocity

    def split(self):
        # Split the asteroid into smaller ones
        if self.radius > ASTEROID_MIN_RADIUS:
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_rotation = random.uniform(20, 50)
            self.spawn(new_radius, self.position, self.velocity.rotate(new_rotation))
            self.spawn(new_radius, self.position, self.velocity.rotate(-new_rotation))
        self.kill()  # Remove the asteroid from the game        
    
    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity