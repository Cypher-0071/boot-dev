from typing import override
from circleshape import *
import pygame
from constants import LINE_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        
    @override
    def draw(self,screen):
        pygame.draw.circle(screen,"white", self.position,self.radius, LINE_WIDTH )
    
    @override
    def update(self, dt):
        self.position += self.velocity * dt
        
        