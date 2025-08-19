import pygame
from player import Player
from pipe import Pipe
from moving_image import MoveingImage

pygame.init()
screen = pygame.display.set_mode((480,500))
clock = pygame.time.Clock()
font = pygame.font.Font('assets/font/editundo.ttf', 48)

# bg_surf = pygame.image.load('assets/sprites/background-day.png').convert()
# base_surf = pygame.image.load('assets/sprites/base.png').convert()
background = MoveingImage(screen, 'assets/sprites/background-day.png', 0, 0)
base = MoveingImage(screen, 'assets/sprites/base.png', 0, 400)

lost_surf = font.render('GAME OVER', False, 'red').convert()
lost_rect = lost_surf.get_rect(center = (screen.get_width() / 2, screen.get_height() / 2))

def active():

    die_sfx = pygame.mixer.Sound('assets/audio/die.wav')
    fly_sfx = pygame.mixer.Sound('assets/audio/wing.wav')

    score = 0

    pipe = Pipe(screen)

    player = Player(screen)
    player.position = 300
    running = True

    mouse = pygame.mouse
    
    GRAVITY:float = 0.25
    vel = 0.0
    can_jump = True

    while running:

        # score = round(pygame.time.get_ticks() / 2000)
        score_surf = font.render(str(score), False, (64,64,64)).convert()
        score_rect = score_surf.get_rect(center = (screen.get_width() / 2, screen.get_height() / 12))
        
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        vel -= GRAVITY
        if keys[pygame.K_SPACE] or  mouse.get_pressed() == (True, False, False):
            if can_jump:
                fly_sfx.play()
                vel = 6
                can_jump = False
        else:
            can_jump = True
        player.rect.bottom -= vel

        # Display the stuff
        screen.fill('purple')
        screen.blit(background.sprite, background.rect)
        screen.blit(player.sprite, player.rect)
        screen.blit(pipe.sprite, pipe.rect)
        screen.blit(pipe.sprite_clone, pipe.rect_clone)
        # screen.blit(pipe.score_surf, pipe.score_rect)
        screen.blit(base.sprite, base.rect)
        pygame.draw.rect(screen, '#c0e8ec', score_rect, border_radius=8)
        screen.blit(score_surf, score_rect)
        pygame.display.flip()

        base.move()
        background.move()
        pipe.move()

        if player.rect.bottom >= 400 or player.rect.top <= 0 or player.rect.colliderect(pipe.rect) or player.rect.colliderect(pipe.rect_clone):
            die_sfx.play()
            running = False
            inactive()
        
        if player.rect.colliderect(pipe.score_rect):
            if can_score:
                can_score = False
                score += 1 
        else:
            can_score = True

        clock.tick(60)

def inactive():
    running = False
    screen.blit(lost_surf, lost_rect)
    while not running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP: active()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: active()
        pygame.display.flip()

        clock.tick(60)

active()
