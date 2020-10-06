from data.components.level import *
from data.constants import *
from pygame import *

init()

WHITE = (255, 255, 255)

clock = time.Clock()

screen = display.set_mode((WIN_WIDTH, WIN_HEIGHT))
screen.fill(WHITE)

level = Level(screen)

game_alive = True
while game_alive:
    screen.fill(WHITE)

    level.update_level()

    display.update()

    clock.tick(30)

    for i in event.get():
        if i.type == QUIT:
            game_alive = False
