# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pygame


def fase_one():
    speed = 2
    background = pygame.image.load('images\\base_fundo_infinity.png')

    clock = pygame.time.Clock()
    move = 0
    close = False
    while not close:
        screen.blit(background, (0 - move, 0))
        screen.blit(background, (width - move, 0))

        move += speed

        if move >= width:
            move = 0

        pygame.display.update()
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = True
                pygame.display.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pygame.init()
    size = width, height = 720, 480
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Game Jam 2021')
    fase_one()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
