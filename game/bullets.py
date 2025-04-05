import pygame
import math

class Bullet:
    def __init__(self, x, y, angle, speed):
        self.x = x  # World coordinate
        self.y = y  # World coordinate
        self.angle = angle
        self.speed = speed
        self.width = 10
        self.height = 5
        self.color = (255, 255, 255)

    def update(self):
        self.x += math.cos(math.radians(self.angle)) * self.speed
        self.y += math.sin(math.radians(self.angle)) * self.speed

    def draw(self, screen, bg_x, bg_y):
        # Adjust the bullet's world coordinates to screen
        screen_x = self.x + bg_x
        screen_y = self.y + bg_y
        pygame.draw.rect(screen, self.color, (screen_x, screen_y, self.width, self.height))

    def check_collision(self, zombies):
        for zombie in zombies:
            # If the bullet is close enough to the zombie, consider it a hit
            distance = math.hypot(self.x - zombie.x, self.y - zombie.y)
            if distance < 20:
                return zombie
        return None
