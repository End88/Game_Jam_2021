# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pygame
from random import randint
import sys

def txt(message, position_txt_x, position_txt_y, scale, font='palatinolinotype', color=(255, 255, 255)):
    font = pygame.font.SysFont(font, scale)
    text = font.render(message, True, color)

    screen.blit(text, [position_txt_x, position_txt_y])


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


def fase_one(difficulte):
    speed = difficulte
    radio = pygame.image.load('images\\radio.png').convert_alpha()
    cone = pygame.image.load('images\\cone.png').convert_alpha()
    obstacle_mask = pygame.mask.from_surface(cone)
    radio_mask = pygame.mask.from_surface(radio)

    volume = 0.5
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.load('songs\\GAME_JAM_-_CRINGE_tema_principal_loop_seamless_2.mp3')
    pygame.mixer.music.play(-1)

    background = pygame.image.load('images\\base_fundo_infinity.png')
    psg1 = pygame.image.load('images\\psg1.png').convert_alpha()
    psg2 = pygame.image.load('images\\psg2.png').convert_alpha()
    psg3 = pygame.image.load('images\\psg3.png').convert_alpha()
    psg4 = pygame.image.load('images\\psg4.png').convert_alpha()
    psg5 = pygame.image.load('images\\psg5.png').convert_alpha()
    psg6 = pygame.image.load('images\\psg6.png').convert_alpha()
    psg7 = pygame.image.load('images\\jump.png').convert_alpha()
    psg8 = pygame.image.load('images\\stop (1).png').convert_alpha()

    psg1_mask = pygame.mask.from_surface(psg1)
    psg2_mask = pygame.mask.from_surface(psg2)
    psg3_mask = pygame.mask.from_surface(psg3)
    psg4_mask = pygame.mask.from_surface(psg4)
    psg5_mask = pygame.mask.from_surface(psg5)
    psg6_mask = pygame.mask.from_surface(psg6)
    psg7_mask = pygame.mask.from_surface(psg7)

    sprite_psg = [psg1, psg1, psg2, psg2, psg3, psg3, psg4, psg4, psg5, psg5, psg6, psg6]
    sprite_psg_mask = [psg1_mask, psg1_mask, psg2_mask, psg2_mask, psg3_mask, psg3_mask, psg4_mask, psg4_mask,
                       psg5_mask, psg5_mask, psg6_mask, psg6_mask]
    clock = pygame.time.Clock()
    move_background = 0
    passage_sprite_psg = 0
    move_psg_x = 0
    move_psg_y = 0
    radios_caught = 0
    cone_caught = 0
    my = randint(260, 380)
    my1 = randint(260, 380)
    my2 = randint(260, 380)
    my3 = randint(260, 380)
    second_cone = randint(50, 200)
    third_cone = randint(250, 400)
    first_radio = randint(50, 200)
    hit1 = False
    hit2 = False
    hit3 = False
    hit4 = False
    cont1 = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0
    time_count = 0
    close = False
    # ____________________________________________ Game loop
    while not close:
        # ________________________________________ Draw in window
        screen.blit(background, (0 - move_background, 0))
        screen.blit(background, (width - move_background, 0))

        ox = 50 + move_psg_x
        oy = 300 + move_psg_y
        cont1 += speed
        if time_count <= 1500:
            if not hit1:
                mx = width - cont1
                offset = (mx - ox, my - oy)
                result = sprite_psg_mask[passage_sprite_psg].overlap(obstacle_mask, offset)
                if result:
                    move_psg_x -= 50
                    cone_caught += 0.5
                    hit1 = True
                screen.blit(cone, (mx, my))

            cont2 += speed
            if not hit2:
                mx1 = width - cont2 + second_cone
                offset = (mx1 - ox, my1 - oy)
                result = sprite_psg_mask[passage_sprite_psg].overlap(obstacle_mask, offset)
                if result:
                    move_psg_x -= 50
                    cone_caught += 0.5
                    hit2 = True
                screen.blit(cone, (mx1, my1))

            cont3 += speed
            if not hit3:
                mx2 = width - cont3 + third_cone
                offset = (mx2 - ox, my2 - oy)
                result = sprite_psg_mask[passage_sprite_psg].overlap(obstacle_mask, offset)
                if result:
                    move_psg_x -= 50
                    cone_caught += 0.5
                    hit3 = True
                screen.blit(cone, (mx2, my2))

            cont4 += speed
            if not hit4:
                mx3 = width - cont4 + first_radio
                offset = (mx3 - ox, my3 - oy)
                result = sprite_psg_mask[passage_sprite_psg].overlap(radio_mask, offset)
                if result:
                    radios_caught += 1
                    hit4 = True
                screen.blit(radio, (mx3, my3))
        else:
            end_game(radios_caught, cone_caught, speed)
        screen.blit(sprite_psg[passage_sprite_psg], (50 + move_psg_x, 300 + move_psg_y))
        time_count += 1
        print(time_count)
        # _______________ speed control and repeat background
        move_background += speed
        if move_background >= width:
            move_background = 0

        # ________________________________ cone restart
        if cont1 >= width:
            my = randint(260, 378)
            hit1 = False
            cont1 = 0
        if cont2 - second_cone >= width:
            my1 = randint(260, 378)
            second_cone = randint(50, 200)
            hit2 = False
            cont2 = 0
        if cont3 - third_cone >= width:
            my2 = randint(260, 378)
            third_cone = randint(50, 200)
            hit3 = False
            cont3 = 0
        if cont4 - first_radio >= width:
            my3 = randint(260, 378)
            first_radio = randint(50, 200)
            hit4 = False
            cont4 = 0
        # _______________ control sprite psg passage

        if passage_sprite_psg >= 11:
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
                pygame.display.quit()
                sys.exit()


def end_game(score_pos, score_neg, difficult):
    background = pygame.image.load('images\\base_fundo_infinity.png')
    bg_score = pygame.image.load('images\\score_base.png')
    grey_button = pygame.image.load('images\\select_button.png')
    brown_button = pygame.image.load('images\\select_button2.png')
    psg1 = pygame.image.load('images\\Win (1).png').convert_alpha()
    psg2 = pygame.image.load('images\\Win (2).png').convert_alpha()
    sprite_psg = [psg1, psg1, psg1, psg2, psg2, psg2]

    clock = pygame.time.Clock()
    total = score_pos - score_neg
    animation = 0
    close = False
    while not close:
        screen.blit(background, (0, 0))
        screen.blit(bg_score, (200, 25))
        screen.blit(brown_button, (155, 360))
        screen.blit(grey_button, (390, 360))
        if total >= difficult:
            txt("You Won", 332, 62, 40, 'ravie', (255, 255, 0))
            screen.blit(sprite_psg[animation], (50, 260))
            if animation >= 5:
                animation = 0
            animation += 1
        else:
            txt("You Lose", 332, 62, 40, 'ravie', (223, 223, 223))
        txt("Score", 235, 111, 36, 'ravie')
        txt(("Box: " + str(score_pos)), 398, 160, 30, 'ravie')
        txt(("Cones: " + str(score_neg)), 398, 210, 30, 'ravie')
        txt(("Total: " + str(total)), 398, 260, 30, 'ravie')

        mouse_position = pygame.mouse.get_pos()
        if (155 < mouse_position[0] < 344) and (360 < mouse_position[1] < 415):
            txt("Menu", 195, 375, 30, 'ravie', (255, 255, 0))
            mouse_press = pygame.mouse.get_pressed()
            if mouse_press[0]:
                menu_screen()
        else:
            txt("Menu", 195, 375, 30, 'ravie', (0, 0, 0))

        if (390 < mouse_position[0] < 579) and (360 < mouse_position[1] < 415):
            txt("Again", 425, 375, 30, 'ravie', (255, 255, 0))
            mouse_press = pygame.mouse.get_pressed()
            if mouse_press[0]:
                fase_one(difficult)
        else:
            txt("Again", 425, 375, 30, 'ravie', (0, 0, 0))

        pygame.display.update()
        clock.tick(15)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()


def menu_screen():
    background = pygame.image.load('images\\base_fundo_infinity.png')
    grey_button = pygame.image.load('images\\select_button.png')
    brown_button = pygame.image.load('images\\select_button2.png')

    events = []
    clock = pygame.time.Clock()
    close = False
    while not close:
        screen.blit(background, (0, 0))
        screen.blit(grey_button, (width/2-105, 200))
        screen.blit(brown_button, (width/2-105, 280))
        txt("Fatec SCS", width / 2 - 170, 50, 50, 'ravie', (255, 255, 0))
        txt("Game Jam 2021", width / 2 - 290, 110, 60, 'ravie', (255, 255, 0))

        mouse_position = pygame.mouse.get_pos()
        if (256 < mouse_position[0] < 442) and (201 < mouse_position[1] < 256):
            txt("Start", width / 2 - 70, 215, 30, 'ravie', (255, 255, 0))
            if 'PRESS' in events:
                difficult_screen()
        else:
            txt("Start", width / 2 - 70, 215, 30, 'ravie', (0, 0, 0))

        if (256 < mouse_position[0] < 442) and (281 < mouse_position[1] < 336):
            txt("Exit", width / 2 - 55, 295, 30, 'ravie', (255, 255, 0))
            mouse_press = pygame.mouse.get_pressed(3)
            if mouse_press[0]:
                pygame.display.quit()
                sys.exit()
        else:
            txt("Exit", width / 2 - 55, 295, 30, 'ravie', (0, 0, 0))
        pygame.display.update()
        clock.tick(60)

        events = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                events.append('PRESS')


def difficult_screen():
    background = pygame.image.load('images\\base_fundo_infinity.png')
    brown_button = pygame.image.load('images\\select_button2.png')

    clock = pygame.time.Clock()
    close = False
    events = []
    while not close:

        screen.blit(background, (0, 0))
        screen.blit(brown_button, (width / 2 - 105, 120))
        screen.blit(brown_button, (width / 2 - 105, 200))
        screen.blit(brown_button, (width / 2 - 105, 280))

        mouse_position = pygame.mouse.get_pos()
        if (256 < mouse_position[0] < 442) and (121 < mouse_position[1] < 175):
            txt("Easy", width / 2 - 60, 135, 30, 'ravie', (255, 255, 0))
            if 'PRESS' in events:
                fase_one(2)
        else:
            txt("Easy", width / 2 - 60, 135, 30, 'ravie', (0, 0, 0))

        if (256 < mouse_position[0] < 442) and (201 < mouse_position[1] < 256):
            txt("Normal", width / 2 - 80, 215, 30, 'ravie', (255, 255, 0))
            if 'PRESS' in events:
                fase_one(3)
        else:
            txt("Normal", width / 2 - 80, 215, 30, 'ravie', (0, 0, 0))

        if (256 < mouse_position[0] < 442) and (281 < mouse_position[1] < 336):
            txt("Hard", width / 2 - 60, 295, 30, 'ravie', (255, 255, 0))
            if 'PRESS' in events:
                fase_one(5)
        else:
            txt("Hard", width / 2 - 60, 295, 30, 'ravie', (0, 0, 0))
        pygame.display.update()
        clock.tick(60)
        events = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                events.append('PRESS')

        print(mouse_position[1])


if __name__ == '__main__':
    pygame.init()
    size = width, height = 720, 480
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Game Jam 2021')
    # fase_one()
    # end_game(10, 5)
    menu_screen()
    # difficult_screen()
