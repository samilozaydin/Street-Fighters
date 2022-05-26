import pygame


class HpBar:

    def __init__(self, image, pos, size, hp):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.rect.width = size[0]
        self.rect.height = size[1]
        self.image = pygame.transform.scale(
            self.image, (self.image.get_rect().width, self.image.get_rect().height))

        self.hpImage = hp
        self.hpImage_rect = self.hpImage.get_rect()
        self.hpImage_rect.width = size[0]
        self.hpImage_rect.height = size[1]
        self.hpImage_rect.center = self.rect.center
        self.width = self.hpImage_rect.w
        self.hp = 1
        self.set_activate = False

    def update(self):
        if self.set_activate:
            self.hpImage = pygame.transform.scale(
                self.hpImage, (self.width * self.hp, self.hpImage_rect.h))
            self.hpImage_rect = self.hpImage.get_rect()
            self.hpImage_rect.center = self.rect.center
        self.set_activate = False

    def setHp(self, hp, is_hitted):
        self.hp = hp
        if is_hitted:
            self.set_activate = True
