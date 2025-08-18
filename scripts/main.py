import pygame

pygame.init()
screen = pygame.display.set_mode((480,600))
clock = pygame.time.Clock()
font = pygame.font.Font('assets/font/editundo.ttf', 48)

bg_surf = pygame.image.load('assets/sprites/background-day.png').convert()
base_surf = pygame.image.load('assets/sprites/base.png').convert()


lost_surf = font.render('GAME OVER', False, 'red').convert()
lost_rect = lost_surf.get_rect(center = (screen.get_width() / 2, screen.get_height() / 2))

def active():

    player_surf = pygame.image.load('assets/sprites/yellowbird-midflap.png').convert_alpha()
    player_rect = player_surf.get_rect(center = (screen.get_width() / 6, screen.get_height() / 2))
    running = True

    mouse = pygame.mouse
    
    GRAVITY:float = 0.25
    vel = 0.0
    can_jump = True

    while running:

        score = round(pygame.time.get_ticks() / 1500)
        score_surf = font.render(str(score), False, (64,64,64)).convert()
        score_rect = score_surf.get_rect(center = (screen.get_width() / 2, screen.get_height() / 12))
        
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        
        # vel Logic
        vel -= GRAVITY
        if keys[pygame.K_SPACE] or mouse.get_pressed() == (True, False, False):
            if can_jump:
                vel = 6
                can_jump = False
        else:
            can_jump = True
        player_rect.bottom -= vel

        # Display the stuff
        screen.fill('black')
        screen.blit(bg_surf, (0,0))
        screen.blit(base_surf, (0,500))
        pygame.draw.rect(screen, '#c0e8ec', score_rect, border_radius=8)
        screen.blit(score_surf, score_rect)
        screen.blit(player_surf, player_rect)
        pygame.display.flip()

        if player_rect.bottom >= 500 or player_rect.top <= 0:
            inactive()

        clock.tick(60)

def inactive():
    running = False
    screen.blit(lost_surf, lost_rect)
    while not running:
        for event in pygame.event.get():
            if event == pygame.QUIT: print('quiting')
        pygame.display.flip()

        clock.tick(60)

active()
