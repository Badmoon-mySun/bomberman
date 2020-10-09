from data.states.levels import *
from data.components.players import *
from data.constants import *
from pygame import *

init()

clock = time.Clock()

screen = display.set_mode((WIN_WIDTH, WIN_HEIGHT), HWSURFACE | DOUBLEBUF)

level = FirstLevel(screen, 0, 0)
pl_pos = level.get_player_position(1)
player = Player(level, BluePlayerSprites(), P1_SETUP, pl_pos[0], pl_pos[1])

game_alive = True
while game_alive:
    keys = key.get_pressed()

    player.update(keys)
    level.update_level()

    display.flip()

    clock.tick(FPS)

    for i in event.get():
        if i.type == QUIT:
            game_alive = False
