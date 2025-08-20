import pygame, sys
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
background2 = MoveingImage(screen, 'assets/sprites/background-day.png', background.sprite.get_size()[0], 0)
background3 = MoveingImage(screen, 'assets/sprites/background-day.png', background.sprite.get_size()[0] * 2, 0)
base = MoveingImage(screen, 'assets/sprites/base.png', 0, 400)
base2 = MoveingImage(screen, 'assets/sprites/base.png', base.sprite.get_size()[0], 400)
base3 = MoveingImage(screen, 'assets/sprites/base.png', base.sprite.get_size()[0] * 2, 400)


def active():

    die_sfx = pygame.mixer.Sound('assets/audio/die.wav')
    fly_sfx = pygame.mixer.Sound('assets/audio/wing.wav')
    fly_sfx.set_volume(0.3)

    score = 0

    pipe = Pipe(screen, 1.5)
    pipe2 = Pipe(screen, 2.5)

    player = Player(screen)
    player.position = screen.get_height() / 2
    player.rect.center = (screen.get_width() / 6, player.position)
    running = True

    mouse = pygame.mouse
    
    GRAVITY:float = 0.25
    vel = 0.0
    can_jump = True

    player_death = [pipe.rect, pipe.rect_clone, pipe2.rect, pipe2.rect_clone]
    moving_objects = [base, base2, base3,background, background2, background3, pipe, pipe2]
    stuff_to_draw = {
        background.sprite:background.rect,
        background2.sprite:background2.rect,
        background3.sprite:background3.rect,
        player.sprite:player.rect,
        pipe.sprite:pipe.rect,
        pipe.sprite_clone:pipe.rect_clone,
        pipe2.sprite:pipe2.rect,
        pipe2.sprite_clone:pipe2.rect_clone,
        base.sprite:base.rect,
        base2.sprite:base2.rect,
        base3.sprite:base3.rect
    }

    while running:

        # score = round(pygame.time.get_ticks() / 2000)
        score_surf = font.render(str(score), False, (64,64,64)).convert()
        score_rect = score_surf.get_rect(center = (screen.get_width() / 2, screen.get_height() / 12))
        
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # vel logic
        vel -= GRAVITY
        if keys[pygame.K_SPACE] or mouse.get_pressed() == (True, False, False):
            if can_jump:
                fly_sfx.play()
                vel = 6
                can_jump = False
        else:
            can_jump = True
        player.rect.bottom -= vel

        for drawing in stuff_to_draw:
            screen.blit(drawing, stuff_to_draw[drawing])
        pygame.draw.rect(screen, '#c0e8ec', score_rect, border_radius=8)
        screen.blit(score_surf, score_rect)
        pygame.display.flip()

        for object in moving_objects:object.move()

        for area in player_death:
            if player.rect.colliderect(area):
                die_sfx.play()
                running = False
                inactive('GAMEOVER', 'red')
        if player.rect.bottom >= 400 or player.rect.top <= 0:
                die_sfx.play()
                running = False
                inactive('GAMEOVER', 'red')

        if player.rect.colliderect(pipe.score_rect) or player.rect.colliderect(pipe2.score_rect):
            if can_score:
                can_score = False
                score += 1 
        else:
            can_score = True

        clock.tick(60)

def inactive(text:str, bg_color:str):
    lost_surf = font.render(text, False, 'black').convert()
    lost_rect = lost_surf.get_rect(center = (screen.get_width() / 2, screen.get_height() / 2))
    running = False
    while not running:
        screen.fill(bg_color)
        screen.blit(lost_surf, lost_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP: active()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: active()
        pygame.display.flip()

        clock.tick(60)

inactive('START', 'blue')
