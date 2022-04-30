import pygame


class ScaleableImage(pygame.sprite.Sprite):
    def __init__(self, center, image):
        super().__init__()
        self.originalImage = image
        self.image = image
        self.rect = image.get_rect(center=center)
        self.grow = 0
        self.mode = 1

    def update(self):
        if self.grow > 50:
            self.mode = -1
        if self.grow < 1:
            self.mode = 1

        self.grow += 1*self.mode

        orig_x, orig_y = self.originalImage.get_size()
        size_x = orig_x + round(self.grow)
        size_y = orig_y + round(self.grow)*(orig_y/orig_x)
        self.image = pygame.transform.scale(
            self.originalImage, (size_x, size_y))
        self.rect = self.image.get_rect(center=self.rect.center)
