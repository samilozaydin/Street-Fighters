import pygame

pygame.init()
res = (500, 500)
screen = pygame.display.set_mode(res)

sss = True
trialBool = False

while sss:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sss = False
    pygame.display.update()

pygame.quit()
