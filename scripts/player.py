import pygame
class Player:

    def __init__(self, screen):
        super().__init__()
        self.position = (screen.get_width() / 6, screen.get_height() / 2)
        self.sprite = pygame.image.load('assets/sprites/yellowbird-midflap.png')
        self.rect = self.sprite.get_rect()
        self.rect.center = self.position
    
    # def vel_logic(self):
    #     vel:float
    #     keys = pygame.key.get_pressed()

    #     vel -= GRAVITY
    #     if keys[pygame.K_SPACE] or mouse.get_pressed() == (True, False, False):
    #         if can_jump:
    #             vel = 6
    #             can_jump = False
    #     else:
    #         can_jump = True
    #     self.rect.bottom -= vel
    #     self.sprite = pygame.transform.rotate(self.sprite, 10)
