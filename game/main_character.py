import math
import pygame
from bullets import Bullet

WIDTH, HEIGHT = 500, 500

class Player:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.world_x = screen_width // 2
        self.world_y = screen_height // 2
        self.speed = 1
        self.health = 100
        self.max_health = 100
        desired_width = 100
        self.counter = 100
        desired_height = 100

        self.chars = []
        for i in range(1, 5):
            s = []
            for j in range(3):
                if j == 0: path = f'Hog-Hacks-2025-main/walking_sprite{i}.png'
                else: path = f'Hog-Hacks-2025-main/walking_sprite{i}_{j}.png'
                im = pygame.image.load(path, ).convert_alpha()
                s.append(pygame.transform.scale(im, (70, 70)))
                print(i, j)
            self.chars.append(s)

        self.current_sprite = self.chars[0][0]
        self.angle = 0
        self.prev = 1
        self.idle = self.chars[0][0]
        self.x = 225
        self.y = 225

        
    def move_down(self, num = 0):
        if self.prev == 2 and self.counter >= 100:
            self.prev = 1
            self.current_sprite = self.chars[num][1]
            self.idle = self.chars[num][0]
            self.counter = 0
        elif self.prev == 1 and self.counter >= 100:
            self.prev = 2
            self.current_sprite = self.chars[num][2]
            self.idle = self.chars[num][0]
            self.counter = 0
        else:
            self.counter += 15

    def move_up(self, num = 1):
        if self.prev == 2 and self.counter >= 100:
            self.prev = 1
            self.current_sprite = self.chars[num][1]
            self.idle = self.chars[num][0]
            self.counter = 0
        elif self.prev == 1 and self.counter >= 100:
            self.prev = 2
            self.current_sprite = self.chars[num][2]
            self.idle = self.chars[num][0]
            self.counter = 0
        else:
            self.counter += 15
            
    def move_right(self, num = 3):
        if self.prev == 2 and self.counter >= 100:
            self.prev = 1
            self.current_sprite = self.chars[num][1]
            self.idle = self.chars[num][0]
            self.counter = 0
        elif self.prev == 1 and self.counter >= 100:
            self.prev = 2
            self.current_sprite = self.chars[num][2]
            self.idle = self.chars[num][0]
            self.counter = 0
        else:
            self.counter += 15
            if self.counter == 15:
                self.y += 2
            if self.counter == 75:
                self.y -= 2

    def move_left(self, num = 2):
        if self.prev == 2 and self.counter >= 100:
            self.prev = 1
            self.current_sprite = self.chars[num][1]
            self.idle = self.chars[num][0]
            self.counter = 0
        elif self.prev == 1 and self.counter >= 100:
            self.prev = 2
            self.current_sprite = self.chars[num][2]
            self.idle = self.chars[num][0]
            self.counter = 0
        else:
            self.counter += 15
            if self.counter == 15:
                self.y += 2
            if self.counter == 75:
                self.y -= 2


    def idle_(self):
        self.current_sprite = self.idle
    def draw(self,  screen):
        screen.blit(self.current_sprite, (self.x, self.y))

