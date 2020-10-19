from data.components.players import *
from data.states.levels import FirstLevel, SecondLevel
from data.states.menu import *
from data.states.pause import *

init()

Is_paused = False
menu_alive = True

mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)

music_sounds_dir = path.join(SOUNDS_DIR, "music\\")

clock = time.Clock()

screen = display.set_mode(SCREEN_SIZE, HWSURFACE | DOUBLEBUF)
display.set_caption(TITLE)

game_alive = True
while game_alive:

    if Is_paused:
        return_move = pause_draw(screen, clock)
        if return_move == 1:
            menu_alive = True
        Is_paused = False

    if menu_alive:
        mixer.music.load(music_sounds_dir + 'menu_music.mp3')
        mixer.music.play(-1)
        mixer.music.set_volume(0.1)
        levels = [FirstLevel, SecondLevel]
        level = levels[menu_draw(screen, clock) - 1](screen, (0, 0))
        player1 = Player(level, BluePlayerSprites(), P1_SETUP, level.get_player_position(1))
        player2 = Player(level, WhitePlayerSprites(), P2_SETUP, level.get_player_position(2))
        menu_alive = False
        mixer.music.stop()
        mixer.music.load(music_sounds_dir + 'game_music.ogg')
        mixer.music.play(-1)
    else:
        if not level.game_is_over():
            level.update()
        else:
            level.game_over_show()
            if key.get_pressed()[K_SPACE]:
                menu_alive = True

    display.flip()

    clock.tick(FPS)

    for i in event.get():
        if i.type == QUIT:
            game_alive = False
        elif i.type == KEYDOWN and i.key == K_ESCAPE:
            Is_paused = True
