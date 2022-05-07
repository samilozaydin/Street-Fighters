import pygame
import sys

from sympy import Q
import button
import scaleableImage
import character

pygame.init()

# General Settings
resolution = (800, 800)
screen = pygame.display.set_mode(resolution, pygame.RESIZABLE)
pygame.display.set_caption("Street Fighters!")

colors = {"white": (255, 255, 255),
          "red": (255, 0, 0),
          "blue": (0, 255, 0),
          "green": (0, 0, 255)}

# create main menu images
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

# create game screen
img_stage_1 = pygame.image.load("images/stage_1.jpg")
img_stage_1_coordinate = (0, 0)
img_stage_1 = pygame.transform.scale(img_stage_1, (800, 800))
# create character


def scale_images(images, x, y):
    for i, image in enumerate(images):
        images[i] = pygame.transform.scale(image, (x, y))


ryu_idle = [pygame.image.load("images/characters/ryu/idle/idle_0.png"),
            pygame.image.load("images/characters/ryu/idle/idle_1.png"),
            pygame.image.load("images/characters/ryu/idle/idle_2.png"),
            pygame.image.load("images/characters/ryu/idle/idle_3.png")]

ryu_move = [pygame.image.load("images/characters/ryu/move/move_0.png"),
            pygame.image.load("images/characters/ryu/move/move_1.png"),
            pygame.image.load("images/characters/ryu/move/move_2.png"),
            pygame.image.load("images/characters/ryu/move/move_3.png"),
            pygame.image.load("images/characters/ryu/move/move_4.png")]
ryu_jump = [pygame.image.load("images/characters/ryu/jump/jump_0.png"),
            pygame.image.load("images/characters/ryu/jump/jump_1.png"),
            pygame.image.load("images/characters/ryu/jump/jump_2.png"),
            pygame.image.load("images/characters/ryu/jump/jump_3.png"),
            pygame.image.load("images/characters/ryu/jump/jump_4.png"),
            pygame.image.load("images/characters/ryu/jump/jump_5.png"),
            pygame.image.load("images/characters/ryu/jump/jump_6.png")]
scale_images(ryu_idle, 132, 246)
scale_images(ryu_move, 132, 246)
scale_images(ryu_jump, 90, 273)

ani_ryu = [ryu_idle, ryu_move, ryu_jump]

ryu = character.Character(ani_ryu, 20, 400)
player = ryu
chrc_group = pygame.sprite.Group(ryu)

# music parameter
pygame.mixer.music.load("music/Intro.mp3")
pygame.mixer.music.play(-1)


def music_situation(is_playing):

    if is_playing == False:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()


def main_menu():
    is_playing = True
    situation = True
    while situation:
        clock.tick(60)
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

        music_pos = (screen.get_rect().centerx+250,
                     screen.get_rect().centerx+300)
        btn_music = button.Button(pygame.image.load(
            "images/music_button.jpg"), music_pos, "", play_font, colors["white"], colors["red"])

        for respond in [btn_play, btn_credit, btn_exit, btn_music]:
            respond.changeColor(mouse_position)
            respond.update(screen)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_play.checkForInput(mouse_position):
                    play()
                if btn_credit.checkForInput(mouse_position):
                    credits()
                if btn_music.checkForInput(mouse_position):

                    if is_playing == False:
                        is_playing = True
                    else:
                        is_playing = False
                    music_situation(is_playing)
                if btn_exit.checkForInput(mouse_position):
                    pygame.quit()
                    sys.exit()
        scl_group.update()
        scl_group.draw(screen)
        # print(str(int(clock.get_fps())))
        pygame.display.update()


def play():

    # statements
    walk_right = False
    walk_left = False
    walk_up = False

    jump_coef = 25
    ani_num = 0

    situation = True
    while situation:
        screen.fill("black")
        speed = 0.1
        events = pygame.event.get()
        user_input = pygame.key.get_pressed()

        screen.blit(img_stage_1, img_stage_1_coordinate)

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                player.animate()

        if user_input[pygame.K_RIGHT] and not (walk_up):
            ani_num = 1
            speed = 0.25
            walk_right = True
            if walk_left:
                ani_num = 1
                walk_right = False
                walk_left = False

        if user_input[pygame.K_LEFT] and not (walk_up):
            ani_num = 1
            speed = 0.25
            walk_left = True
            if walk_right:
                ani_num = 1
                walk_right = False
                walk_left = False

        if walk_up is False and user_input[pygame.K_UP]:
            ani_num = 2
            speed = 0.25
            walk_up = True

        if player.current_index == 0:
            ani_num = 0
            speed = 0.1
            if not walk_up:
                walk_left = False
                walk_right = False

        if walk_up:
            jumping(jump_coef)
            jump_coef -= 1
            if jump_coef < -25:
                jump_coef = 25
                walk_up = False
                ani_num = 0

        if walk_left:
            movement(-2)
        if walk_right:
            movement(2)

        chrc_group.update(speed, ani_num)
        chrc_group.draw(screen)
        clock.tick(60)

        pygame.display.update()


def credits():

    situation = True
    while situation:
        mouse_position = pygame.mouse.get_pos()
        clock.tick(60)

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

        screen.blit(credit_text_1, credit_text_1_coordinate)
        screen.blit(credit_text_2, credit_text_2_coordinate)
        scl_group.update()
        scl_group.draw(screen)
        pygame.display.update()


def movement(amount):
    player.rect.topleft = (player.rect.x + float(amount), player.rect.y)


def jumping(amount):

    player.rect.topleft = (player.rect.x, player.rect.y-float(amount))


main_menu()
