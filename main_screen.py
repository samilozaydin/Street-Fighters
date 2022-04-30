import pygame
import sys
import button
import scaleableImage

pygame.init()

# General Settings
resolution = (800, 800)
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Street Fighters!")

colors = {"white": (255, 255, 255),
          "red": (255, 0, 0),
          "blue": (0, 255, 0),
          "green": (0, 0, 255)}

img_bckgnd = pygame.image.load("images/background.jpg")
img_bckgnd_coordinate = (0, 0)
img_bckgnd = pygame.transform.scale(img_bckgnd, (800, 800))

img_bckgnd_text = pygame.image.load("images/bckgnd_text2.png")
img_bckgnd_text = pygame.transform.scale(img_bckgnd_text, (600, 300))
img_bckgnd_text_rect = img_bckgnd_text.get_rect(x=100, y=80)

scl_img_bckgnd_text = scaleableImage.ScaleableImage(
    img_bckgnd_text_rect.center, img_bckgnd_text)

scl_group = pygame.sprite.Group(scl_img_bckgnd_text)
clock = pygame.time.Clock()


def main_menu():

    situation = True
    while situation:
        screen.fill("black")
        mouse_position = pygame.mouse.get_pos()
        screen.blit(img_bckgnd, img_bckgnd_coordinate)
       # screen.blit(img_bckgnd_text, img_bckgnd_text_coordinate)
        play_font = pygame.font.SysFont("calibri", 50)
        play_pos = (screen.get_rect().centerx, screen.get_rect().centery+50)
        btn_play = button.Button(
            None, play_pos, "Play", play_font, colors["white"], colors["red"])

        credit_pos = (screen.get_rect().centerx, screen.get_rect().centery+100)
        btn_credit = button.Button(
            None, credit_pos, "Credit", play_font, colors["white"], colors["red"])

        exit_pos = (screen.get_rect().centerx, screen.get_rect().centery+150)
        btn_exit = button.Button(
            None, exit_pos, "Exit", play_font, colors["white"], colors["red"])

        for respond in [btn_play, btn_credit, btn_exit]:
            respond.changeColor(mouse_position)
            respond.update(screen)
        events = pygame.event.get()
        for event in events:
            clock.tick(60)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_play.checkForInput(mouse_position):
                    play()
                if btn_credit.checkForInput(mouse_position):
                    credits()
                if btn_exit.checkForInput(mouse_position):
                    pygame.quit()
                    sys.exit()
        scl_group.update()
        scl_group.draw(screen)
        pygame.display.update()


def play():

    situation = True
    while situation:
        screen.fill("black")

        play_font = pygame.font.SysFont("calibri", 32)
        play_text = play_font.render("Play", True, colors["white"])
        play_rect = play_text.get_rect(center=(640, 240))

        screen.blit(play_text, play_rect)


def credits():

    situation = True
    while situation:
        mouse_position = pygame.mouse.get_pos()

        screen.fill("black")
        screen.blit(img_bckgnd, img_bckgnd_coordinate)
        #screen.blit(img_bckgnd_text, img_bckgnd_text_coordinate)

        credit_font = pygame.font.SysFont("calibri", 36)

        credit_text_1 = credit_font.render(
            "Samil Bilal OZAYDIN", True, colors["white"])
        credit_text_1_coordinate = (
            screen.get_rect().centerx - 150, screen.get_rect().centery+25)

        credit_text_2 = credit_font.render(
            "Yunus SUMER", True, colors["white"])
        credit_text_2_coordinate = (
            screen.get_rect().centerx - 120, screen.get_rect().centery+75)

        exit_pos = (screen.get_rect().centerx-20,
                    screen.get_rect().centery+175)
        btn_exit = button.Button(
            None, exit_pos, "Exit", pygame.font.SysFont("calibri", 36), colors["white"], colors["red"])

        for respond in [btn_exit]:
            respond.changeColor(mouse_position)
            respond.update(screen)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_exit.checkForInput(mouse_position):
                    main_menu()
            scl_group.update()
            scl_group.draw(screen)

            screen.blit(credit_text_1, credit_text_1_coordinate)
            screen.blit(credit_text_2, credit_text_2_coordinate)

            pygame.display.update()


main_menu()
