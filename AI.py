import pygame
import random

#this is just some scribbles .It is not used.

def gameAI(player, computer, flip_str):

    if flip_str:
        distance = player.rect.topright[0] - computer.rect.topleft[0]
    else:
        distance = player.rect.topleft[0] - computer.rect.topright[0]

    if distance < -150:
        computer.movement(-2)
        computer.update(0.25, 1, flip_str)
    elif distance > 150 :
        computer.movement(2)
        computer.update(0.25, 1, flip_str)
    else: 
        randNum = randint(0,10)
        if computer.current_index ==0:
            print(computer.current_index)
            if randNum == 0:#idle
                computer.update(0.1, 0, flip_str)
            if randNum == 1:#move left
                computer.movement(-2)
                computer.update(0.25, 1, flip_str)
            if randNum == 2: #move right
                computer.movement(2)
                computer.update(0.25, 1, flip_str)
            if randNum == 3 : #punching
                computer.update(0.25,1,flip_str)
                computer.animate()
                computer.is_attacking = True
                computer.is_punching = True
 