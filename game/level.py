import pygame
import random
import math
import time
from zombies import BaseZombie

class Level:
    def __init__(self, level_number, screen_width, screen_height, player, zombie_idle_sprite_path, zombie_moving_sprite_path):
        self.level_number = level_number
        self.kills = 0
        self.wave = 1
        self.player = player
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.zombie_idle_sprite_path = zombie_idle_sprite_path
        self.zombie_moving_sprite_path = zombie_moving_sprite_path
        self.zombies = []
        self.zombie_speed = 2 + (level_number * 0.5)
        self.zombie_health = 100 + (level_number * 20)
        self.spawn_interval = max(0.5, 2 - (level_number * 0.2))
        self.last_spawn_time = time.time()

    def spawn_zombie(self):
        zombie = BaseZombie(
            self.screen_width,
            self.screen_height,
            self.player.world_x,
            self.player.world_y,
            100,
            self.zombie_speed,
            self.zombie_health,
            self.zombie_idle_sprite_path,
            self.zombie_moving_sprite_path
        )
        self.zombies.append(zombie)

    def update(self, bullets):
        # Existing zombie logic
        for zombie in self.zombies:
            zombie.move_toward_player(self.player.world_x, self.player.world_y)

        # Update bullets
        for bullet in list(bullets):
            bullet.update()
            zombie_hit = bullet.check_collision(self.zombies)
            if zombie_hit:
                self.remove_zombie(zombie_hit)
                bullets.remove(bullet)

        # Example: Add any other logic, like spawning zombies or wave progression
        current_time = pygame.time.get_ticks()
        if current_time - self.last_spawn_time > self.spawn_interval:
            self.spawn_zombie()
            self.last_spawn_time = current_time

        
    def draw(self, screen, bg_x, bg_y):
        for zombie in self.zombies:
            zombie.draw(screen, bg_x, bg_y)

    def remove_zombie(self, zombie):
        self.zombies.remove(zombie)
        self.kills += 1
        self.update_wave()

    def update_zombie_stats(self):
        self.zombie_speed *= 1.2
        self.zombie_health *= 1.2

    def remove_zombie(self, zombie):
        self.zombies.remove(zombie)
        self.kills += 1
        if self.kills % 10 == 0:
            self.update_zombie_stats()

    def update_wave(self):
        if self.kills % 10 == 0 and self.kills != 0:
            self.wave += 1
            self.player.regenerate_health()
            self.zombie_speed *= 1.2
            self.zombie_health *= 1.2
