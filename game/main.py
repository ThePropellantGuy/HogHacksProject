import pygame
from main_character import Player
from level import Level
import sys
import math
import random
import functions
from zombies import BaseZombie

pygame.init()

# Globals
WIDTH, HEIGHT = 500, 500
FPS = 60
spawn_radius = 50
zombie_speed = 2

# Colors
WHITE = (0, 0, 0)

# Screen Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BrainRaid")
clock = pygame.time.Clock()

# Class Objects
player = Player(250, 250)
current_level = Level(
    0, 
    WIDTH, 
    HEIGHT,
    player,
    "Hog-Hacks-2025-main/zombieidle.gif", 
    "Hog-Hacks-2025-main/zombiemoving.gif"
)
kills = 0

# Background Loading
background = pygame.image.load("bg1.png")
background = pygame.transform.scale(background, (6000, 6000))
# Background 
bg_x, bg_y = 0, 0
bg_speed = 5
playerx = 250
playery = 250
xchange = 0
ychange = 0
def game_upd(keys):
    global playerx, playery, xchange, ychange
    move = False
    if keys[pygame.K_w] and playery >0:
        background.scroll(0, bg_speed)
        playery -= 1
        player.move_up()
        move = True
        ychange += 1
    if keys[pygame.K_s] and playery < 1901:
        background.scroll(0, -bg_speed)
        playery += 1
        player.move_down()
        move = True
        ychange -= 1
    if keys[pygame.K_a] and  playerx > 0:
        background.scroll(bg_speed,0)
        playerx -= 1
        player.move_left()
        move = True
        xchange += 1
    if keys[pygame.K_d] and playerx < 2851:
        background.scroll(-bg_speed, 0)
        playerx += 1
        player.move_right()
        move = True
        xchange -= 1

    if not move:
        player.idle_()



c = 0
zombies = []
def main():
    global bullets

    running = True
    while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        keys = pygame.key.get_pressed()
        game_upd(keys)
        
        
        if random.randint(0,100) > 75:
            e = BaseZombie(6000, 6000, player.x, player.y, 10, 1, 10, 'Hog-Hacks-2025-main/zombieidle.gif','Hog-Hacks-2025-main/zombieidle.gif')
            zombies.append(e)
        if player.health <= 0:
            print("Game Over!")
            running = False

        screen.fill((0, 0, 0))
        screen.blit(background, (-1000, -1000))
        for z in zombies:
            z.move_toward_player(player.x, player.y)
            z.draw(screen,0, 0, xchange, ychange)


        functions.draw_health_bar(screen, player)
        functions.draw_stats(screen, current_level)
        player.draw(screen)
        pygame.display.update()


        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
