import pygame

pygame.init()
screen = pygame.display.set_mode((100,100))
clock = pygame.time.Clock()

player_surf = pygame.surface.Surface((50,50))

while True:
    for shelby in pygame.event.get():
        if shelby.type == pygame.KEYDOWN:
            if shelby.key == pygame.K_SPACE: player_surf = pygame.transform.rotate(player_surf, 15)
        if shelby.type == pygame.QUIT: pygame.quit()

    screen.fill('purple')
    screen.blit(player_surf, (25, 25))
    pygame.display.flip()
    clock.tick(30)
