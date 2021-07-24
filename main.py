# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pygame
from random import randint


def left_is_down():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        return True
    return False


def right_is_down():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        return True
    return False


def up_is_down():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        return True
    return False


def down_is_down():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        return True
    return False


class Cone():
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y


def fase_one():
    speed = 2
    bluepill = pygame.image.load('images\\bluepill.png').convert_alpha()
    cone = pygame.image.load('images\\cone.png').convert_alpha()
    obstacle_mask = pygame.mask.from_surface(cone)

    volume = 0.5
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.load('songs\\GAME JAM - CRINGE tema principal.wav')
    pygame.mixer.music.play(-1)

    background = pygame.image.load('images\\base_fundo_infinity.png')
    psg1 = pygame.image.load('images\\psg1.png').convert_alpha()
    psg2 = pygame.image.load('images\\psg2.png').convert_alpha()
    psg3 = pygame.image.load('images\\psg3.png').convert_alpha()
    psg4 = pygame.image.load('images\\psg4.png').convert_alpha()
    psg5 = pygame.image.load('images\\psg5.png').convert_alpha()
    psg6 = pygame.image.load('images\\psg6.png').convert_alpha()
    psg7 = pygame.image.load('images\\psg7.png').convert_alpha()
    psg8 = pygame.image.load('images\\psg8.png').convert_alpha()

    psg1_mask = pygame.mask.from_surface(psg1)
    psg2_mask = pygame.mask.from_surface(psg2)
    psg3_mask = pygame.mask.from_surface(psg3)
    psg4_mask = pygame.mask.from_surface(psg4)
    psg5_mask = pygame.mask.from_surface(psg5)
    psg6_mask = pygame.mask.from_surface(psg6)
    psg7_mask = pygame.mask.from_surface(psg7)
    psg8_mask = pygame.mask.from_surface(psg8)

    sprite_psg = [psg1, psg1, psg2, psg2, psg3, psg3, psg4, psg4, psg5, psg5, psg6, psg6, psg7, psg7, psg8, psg8]
    sprite_psg_mask = [psg1_mask, psg1_mask, psg2_mask, psg2_mask, psg3_mask, psg3_mask, psg4_mask, psg4_mask,
                       psg5_mask, psg5_mask, psg6_mask, psg6_mask, psg7_mask, psg7_mask, psg8_mask, psg8_mask]
    clock = pygame.time.Clock()
    move_background = 0
    passage_sprite_psg = 0
    move_psg_x = 0
    move_psg_y = 0
    my = randint(260, 380)
    my1 = randint(260, 380)
    my2 = randint(260, 380)
    second_cone = randint(50, 200)
    third_cone = randint(250, 400)
    hit1 = False
    hit2 = False
    hit3 = False
    cont1 = 0
    cont2 = 0
    cont3 = 0
    close = False
    # ____________________________________________ Game loop
    while not close:
        # ________________________________________ Draw in window
        screen.blit(background, (0 - move_background, 0))
        screen.blit(background, (width - move_background, 0))

        cont1 += speed
        if not hit1:
            ox = 50 + move_psg_x
            oy = 320 + move_psg_y
            mx = width - cont1
            offset = (mx - ox, my - oy)
            result = sprite_psg_mask[passage_sprite_psg].overlap(obstacle_mask, offset)
            if result:
                move_psg_x -= 50
                hit1 = True
            screen.blit(cone, (mx, my))

        cont2 += speed
        if not hit2:
            ox = 50 + move_psg_x
            oy = 320 + move_psg_y
            mx1 = width - cont2 + second_cone
            offset = (mx1 - ox, my1 - oy)
            result = sprite_psg_mask[passage_sprite_psg].overlap(obstacle_mask, offset)
            if result:
                move_psg_x -= 50
                hit2 = True
            screen.blit(cone, (mx1, my1))

        cont3 += speed
        if not hit3:
            ox = 50 + move_psg_x
            oy = 320 + move_psg_y
            mx2 = width - cont3 + third_cone
            offset = (mx2 - ox, my2 - oy)
            result = sprite_psg_mask[passage_sprite_psg].overlap(obstacle_mask, offset)
            if result:
                move_psg_x -= 50
                hit3 = True
            screen.blit(cone, (mx2, my2))

        screen.blit(sprite_psg[passage_sprite_psg], (50 + move_psg_x, 320 + move_psg_y))

        # _______________ speed control and repeat background
        move_background += speed
        if move_background >= width:
            move_background = 0

        # ________________________________ cone restart
        if cont1 >= width:
            my = randint(260, 380)
            hit1 = False
            cont1 = 0
        if cont2 - second_cone >= width:
            my1 = randint(260, 380)
            second_cone = randint(50, 200)
            hit2 = False
            cont2 = 0
        if cont3 - third_cone >= width:
            my2 = randint(260, 380)
            third_cone = randint(50, 200)
            hit3 = False
            cont3 = 0
        # _______________ control sprite psg passage

        if passage_sprite_psg >= 14:
            passage_sprite_psg = 0
        passage_sprite_psg += 1

        # _______________ move control
        if right_is_down():
            if move_psg_x <= 424:
                move_psg_x += 2
        if left_is_down():
            if 0 <= move_psg_x <= 426:
                move_psg_x += -4
        if up_is_down():
            if -128 <= move_psg_y <= 2:
                move_psg_y += -2
        if down_is_down():
            if -130 <= move_psg_y <= 0:
                move_psg_y += 2
        pygame.display.update()
        clock.tick(30)
        # ______________________________ Close game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = True
                pygame.display.quit()


if __name__ == '__main__':
    pygame.init()
    size = width, height = 720, 480
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Game Jam 2021')
    fase_one()
