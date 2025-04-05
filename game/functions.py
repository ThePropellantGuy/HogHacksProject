import pygame

def draw_health_bar(screen, player):
    pygame.draw.rect(screen, (255, 0, 0), (10, 10, 200, 20))
    pygame.draw.rect(screen, (0, 255, 0), (10, 10, 2 * player.health, 20))

def draw_stats(screen, level):
    font = pygame.font.Font(None, 36)
    kill_text = font.render(f"survived: {level.kills}", True, (0, 0, 0))
    wave_text = font.render(f"Wave: {level.wave}", True, (0, 0, 0))
    screen.blit(kill_text, (10, 40))
    screen.blit(wave_text, (10, 70))

