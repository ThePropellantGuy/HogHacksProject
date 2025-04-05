import pygame, random, math
import functions

class BaseZombie:
    def __init__(self, screen_width, screen_height, player_x, player_y, spawn_radius, zombie_speed, zombie_health, idle_sprite_path, moving_sprite_path):
        self.speed = zombie_speed
        self.health = zombie_health
        self.x, self.y = self.generate_spawn_position(screen_width, screen_height, player_x, player_y, spawn_radius)
        self.idle_sprite = pygame.image.load(idle_sprite_path)
        self.idle_sprite = pygame.transform.scale(self.idle_sprite, (50, 50))
        self.moving_sprite = pygame.image.load(moving_sprite_path)
        self.moving_sprite = pygame.transform.scale(self.moving_sprite, (50, 50))
        self.current_sprite = self.idle_sprite
        self.is_moving = False

    def generate_spawn_position(self, screen_width, screen_height, player_x, player_y, spawn_radius):
        while True:
            x = random.randint(0, screen_width)
            y = random.randint(0, screen_height)
            distance = math.sqrt((player_x - x)**2 + (player_y - y)**2)
            if distance > spawn_radius:
                return x, y

    def move_toward_player(self, player_x, player_y):
        dx = player_x - self.x
        dy = player_y - self.y
        magnitude = math.sqrt(dx**2 + dy**2)
        if magnitude > 0:
            dx /= magnitude
            dy /= magnitude
            self.x += dx * self.speed
            self.y += dy * self.speed

    def take_damage(self, damage):
        self.health -= damage
        return self.health <= 0

    def draw(self, screen, bg_x, bg_y, xchange, ychange):
        screen.blit(self.current_sprite, ((self.x - bg_x) + xchange, ychange + (self.y - bg_y)))
