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


pygame.init()

resolution = (500, 500)
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()

colors = {"white": (255, 255, 255),
          "red": (255, 0, 0),
          "blue": (0, 255, 0),
          "green": (0, 0, 255)}
pygame.draw.line(screen, colors["blue"], (0, 0), (100, 100), 15)

monster_1 = pygame.image.load("monster_1.png")
monster_1_coordinate = monster_1.get_rect()
monster_1_coordinate.center = screen.get_rect().center
monster_1 = pygame.transform.scale(monster_1, (50, 50))

scaleable = ScaleableImage(monster_1_coordinate.center, monster_1)
group = pygame.sprite.Group(scaleable)

thefont = pygame.font.SysFont("calibri", 32)
yazi = thefont.render("Shaking!", True, colors["white"])
yazi_coordinate = yazi.get_rect()
yazi_coordinate.center = (monster_1_coordinate.centerx,
                          monster_1_coordinate.centery+100)

scaleable_2 = ScaleableImage(yazi_coordinate.center, yazi)
group.add(scaleable_2)


situation = True
while situation:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            situation = False

    group.update()
    screen.fill(0)
    group.draw(screen)
    pygame.display.update()

pygame.quit()
exit()
