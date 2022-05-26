from re import A
import pygame
from regex import F


class Character(pygame.sprite.Sprite):

    def __init__(self, images, x, y):
        super().__init__()
        self.sprites = []
        self.sprites.extend(images)
        self.is_animate = False
        self.is_idle = True
        self.is_hitted = False
        self.is_attacking = False
        self.is_hitted_animate = False
        self.is_kicking = False
        self.is_punching = False
        self.is_reverse = False
        self.hp = 1
        self.current_index = 0
        self.current_index_idle = 0
        self.image = images[0][0]
        self.rect = self.image.get_rect()

        self.hitbox_body_rect = pygame.Rect(
            self.rect.midbottom[0], self.rect.midbottom[1], 60, 210)
        self.hitbox_head_rect = pygame.Rect(
            self.rect.midleft[0], self.rect.midleft[1], 50, 40)
        self.hitbox_attack_rect = pygame.Rect(
            self.rect.topleft[0], self.rect.topleft[1], 120, 30)
        self.rect.topleft = [x, y]
        self.hitbox_attack_kick_rect = pygame.Rect(
            self.rect.topleft[0], self.rect.topleft[1], 90, 30)

    def update(self, speed, ani_num, is_reverse):
        topleft = self.rect.topleft
        if is_reverse:
            if self.is_animate == True:
                self.current_index += speed

                if self.current_index >= len(self.sprites[ani_num]):
                    self.current_index = 0
                    self.is_animate = False
                    self.is_idle = True
                    self.is_attacking = False
                    self.is_kicking = False
                    self.is_punching = False
                    self.is_hitted_animate = False

                old_image = self.image
                self.image = self.sprites[ani_num][int(self.current_index)]
                self.rect = self.image.get_rect()
                self.rect.topleft = (
                    topleft[0]-(self.rect.w-old_image.get_rect().w), topleft[1])
                self.hitbox_body_rect.midbottom = (
                    self.rect.midbottom[0], self.rect.midbottom[1])
                self.hitbox_head_rect.topleft = (
                    self.rect.x+(self.rect.w/2-self.hitbox_head_rect.w/2), self.rect.y)
                if self.is_reverse:

                    self.hitbox_attack_rect.topleft = (
                        self.rect.x-60, self.rect.y+30)
                    self.hitbox_attack_kick_rect.topleft = (
                        self.rect.x-45, self.rect.y+200)
                else:
                    self.hitbox_attack_rect.topleft = (
                        self.rect.x+100, self.rect.y+30)
                    self.hitbox_attack_kick_rect.topleft = (
                        self.rect.x+100, self.rect.y+200)
            else:
                self.current_index_idle += speed
                if self.current_index_idle >= len(self.sprites[ani_num]):
                    self.current_index_idle = 0
                    self.is_hitted_animate = False

                self.image = self.sprites[ani_num][int(
                    self.current_index_idle)]
                self.rect = self.image.get_rect()
                self.rect.topleft = topleft
                self.hitbox_body_rect.midbottom = (
                    self.rect.midbottom[0], self.rect.midbottom[1])
                self.hitbox_head_rect.topleft = (
                    self.rect.x+(self.rect.w/2-self.hitbox_head_rect.w/2), self.rect.y)
                if self.is_reverse:

                    self.hitbox_attack_rect.topleft = (
                        self.rect.x-60, self.rect.y+30)
                    self.hitbox_attack_kick_rect.topleft = (
                        self.rect.x-45, self.rect.y+200)
                else:
                    self.hitbox_attack_rect.topleft = (
                        self.rect.x+100, self.rect.y+30)
                    self.hitbox_attack_kick_rect.topleft = (
                        self.rect.x+100, self.rect.y+200)
        else:
            if self.is_animate == True:
                self.current_index += speed
                if self.current_index >= len(self.sprites[ani_num]):
                    self.current_index = 0
                    self.is_animate = False
                    self.is_idle = True
                    self.is_attacking = False
                    self.is_kicking = False
                    self.is_punching = False
                    self.is_hitted_animate = False

                self.image = self.sprites[ani_num][int(self.current_index)]
                self.rect = self.image.get_rect()
                self.rect.topleft = topleft
                self.hitbox_body_rect.midbottom = (
                    self.rect.midbottom[0], self.rect.midbottom[1])
                self.hitbox_head_rect.topleft = (
                    self.rect.x+(self.rect.w/2-self.hitbox_head_rect.w/2), self.rect.y)
                if self.is_reverse:

                    self.hitbox_attack_rect.topleft = (
                        self.rect.x-60, self.rect.y+30)
                    self.hitbox_attack_kick_rect.topleft = (
                        self.rect.x-45, self.rect.y+200)
                else:
                    self.hitbox_attack_rect.topleft = (
                        self.rect.x+100, self.rect.y+30)
                    self.hitbox_attack_kick_rect.topleft = (
                        self.rect.x+100, self.rect.y+200)
            else:
                self.current_index_idle += speed
                if self.current_index_idle >= len(self.sprites[ani_num]):
                    self.current_index_idle = 0
                    self.is_hitted_animate = False

                self.image = self.sprites[ani_num][int(
                    self.current_index_idle)]
                self.rect = self.image.get_rect()
                self.rect.topleft = topleft
                self.hitbox_body_rect.midbottom = (
                    self.rect.midbottom[0]-10, self.rect.midbottom[1])

                if self.is_reverse:

                    self.hitbox_attack_rect.topleft = (
                        self.rect.x-60, self.rect.y+30)
                    self.hitbox_attack_kick_rect.topleft = (
                        self.rect.x-45, self.rect.y+200)

                else:
                    self.hitbox_attack_rect.topleft = (
                        self.rect.x+100, self.rect.y+30)
                    self.hitbox_attack_kick_rect.topleft = (
                        self.rect.x+100, self.rect.y+200)

    def animate(self):
        self.is_animate = True
        self.is_idle = False
        self.current_index_idle = 0

    def movement(self, amount):
        self.rect.topleft = (self.rect.x + float(amount), self.rect.y)
        if 0 > self.rect.topleft[0]:
            self.rect.topleft = (0, self.rect.y)
        if 800 < self.rect.topright[0]:
            self.rect.topright = (800, self.rect.y)

    def jumping(self, amount):
        self.rect.topleft = (self.rect.x, self.rect.y-float(amount))
    # Silinebilir.

    def reverseHitBox(self):
        self.is_reverse = False if self.is_reverse else True
