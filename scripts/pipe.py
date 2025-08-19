import pygame
from random import *
class Pipe:
    def __init__(self, screen):
        super().__init__()
        position = screen.get_width() / 2
        self.position = randrange(300, screen.get_height() + 50)
        self.sprite = pygame.image.load('assets/sprites/pipe-green.png')
        self.rect = self.sprite.get_rect(center = (screen.get_width(), self.position))
        self.sprite_clone = pygame.image.load('assets/sprites/pipe-green.png')
        self.sprite_clone = pygame.transform.flip(self.sprite_clone, False, True)
        self.rect_clone = self.sprite.get_rect(center = (screen.get_width(), self.position - 425))

        self.score_surf = pygame.surface.Surface((self.sprite.get_size()[0], self.sprite.get_size()[1]))
        self.score_rect = self.score_surf.get_rect()
    def move(self):
        self.rect.right -= 3
        if self.rect.left <= -self.sprite.get_size()[0]:
            self.rect.left = 480
        self.rect_clone.right = self.rect.right
        self.score_rect = self.score_surf.get_rect(right = self.rect.right, left = self.rect.left, bottom = self.rect.bottom, top = self.rect_clone.bottom)
