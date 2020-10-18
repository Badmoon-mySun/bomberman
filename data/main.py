from data.components.players import *
from data.states.levels import FirstLevel
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
        level = menu_draw(screen, clock)
        if level == 1:
            level = FirstLevel(screen, 0, 0)
            level.update_level()
            pl_pos = level.get_player_position(1)
            p2_pos = level.get_player_position(2)
            player1 = Player(level, BluePlayerSprites(), P1_SETUP, (pl_pos[0], pl_pos[1]))
            player2 = Player(level, WhitePlayerSprites(), P2_SETUP, (p2_pos[0], p2_pos[1] - 9))
        menu_alive = False
        mixer.music.stop()
        mixer.music.load(music_sounds_dir + 'game_music.ogg')
        mixer.music.play(-1)

    keys = key.get_pressed()
    level.update_level()

    display.flip()

    clock.tick(FPS)

    for i in event.get():
        if i.type == QUIT:
            game_alive = False
        elif i.type == KEYDOWN and i.key == K_ESCAPE:
            Is_paused = True
