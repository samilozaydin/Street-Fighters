from re import A
import pygame


class Character(pygame.sprite.Sprite):

    def __init__(self, images, x, y):
        super().__init__()
        self.sprites = []
        self.sprites.extend(images)
        self.is_animate = False
        self.is_idle = True
        self.current_index = 0
        self.image = images[0][0]
        self.rect = self.image.get_rect()

        self.rect.topleft = [x, y]

    def update(self, speed,ani_num):
        if self.is_animate == True:
            self.current_index += speed
            if self.current_index >= len(self.sprites[ani_num]):
                self.current_index = 0
                self.is_animate = False
                self.is_idle = True
            self.image = self.sprites[ani_num][int(self.current_index)]
        else:
            self.current_index += speed
            if self.current_index >= len(self.sprites[ani_num]):
                self.current_index = 0
            self.image = self.sprites[ani_num][int(self.current_index)]
            print(self.current_index)

    def animate(self):
        self.is_animate = True
        self.is_idle = False
    