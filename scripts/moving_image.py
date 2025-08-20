import pygame
class MoveingImage:
    global screen
    def __init__(self, surface, image:str, pos_x:float, pos_y:float):
        super().__init__()
        self.pos = (pos_x, pos_y)
        self.screen = surface
        self.sprite = pygame.image.load(image)
        self.rect = self.sprite.get_rect()
        self.rect.topleft = (pos_x, pos_y)
    def move(self):
        self.rect.right -= 3
        if self.rect.left <= -self.sprite.get_size()[0]: self.rect.left = 480
