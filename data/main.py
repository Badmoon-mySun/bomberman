from data.states.level import *
from data.components.player import *
from data.constants import *
from pygame import *

init()

WHITE = (255, 255, 255)

clock = time.Clock()

screen = display.set_mode((WIN_WIDTH, WIN_HEIGHT))
screen.fill(WHITE)

level = Level(screen)
player = Player(32, 32)

game_alive = True
while game_alive:
    screen.fill(WHITE)

    keys = key.get_pressed()
    direction = None
    if keys[K_LEFT]:
        direction = K_LEFT
    elif keys[K_RIGHT]:
        direction = K_RIGHT
    elif keys[K_UP]:
        direction = K_UP
    elif keys[K_DOWN]:
        direction = K_DOWN

    level.update_level()
    player.update(direction, level.obstacles)
    screen.blit(player.image, (player.rect.x, player.rect.y))

    display.update()

    clock.tick(60)

    for i in event.get():
        if i.type == QUIT:
            game_alive = False