from pygame import image
from os import path

sprites_dir = path.dirname(__file__).replace("data\\components", "resources\\sprites\\player")


first_player_down_play = [image.load("%s/player1_down_%s.png" % (sprites_dir, i)) for i in range(1, 10)]
first_player_down = first_player_down_play[4]

first_player_sprite = first_player_down
