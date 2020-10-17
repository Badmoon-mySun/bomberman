from pygame import *
from os import path

GRAY = (125, 125, 125)
GREEN = (0, 200, 64)
LIGHT_BLUE = (64, 128, 255)
YELLOW = (225, 225, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
ORANGE = (255, 150, 100)
PINK = (230, 50, 230)
WHITE = (255, 255, 255)
BROWN = (168, 66, 17)

# Название окна
TITLE = "Bomberman"

# Размер блока
BLOCK_SIZE = 40

# Размеры игрока
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 48

# Количество блоков в ширину и в длину
WIDTH_BLOCKS_COUNT = 15
HEIGHT_BLOCS_COUNT = 13

# Высчитываем размеры экрана в зависимости от количества и размера блоков
SCREEN_SIZE = (WIN_WIDTH, WIN_HEIGHT) = (WIDTH_BLOCKS_COUNT * BLOCK_SIZE, HEIGHT_BLOCS_COUNT * BLOCK_SIZE)
CENTER = (WIN_WIDTH // 2, WIN_HEIGHT // 2)

# Высчитываем размеры меню в зависимости от размера экрана
PAUSE_SIZE = (PAUSE_WIDTH, PAUSE_HEIGHT) = (WIN_WIDTH // 2, WIN_HEIGHT // 3)

# Цвет меню
MENU_COLOR = BROWN

# Скорость игроков по умолчанию
PLAYER_SPEED = 2

# Раскладка первого игрока
P1_UP = K_UP
P1_DOWN = K_DOWN
P1_LEFT = K_LEFT
P1_RIGHT = K_RIGHT
P1_DROP = K_SLASH
P1_SETUP = [P1_UP, P1_DOWN, P1_LEFT, P1_RIGHT, P1_DROP]

# Раскладка второго игрока
P2_UP = K_w
P2_DOWN = K_s
P2_LEFT = K_a
P2_RIGHT = K_d
P2_DROP = K_v
P2_SETUP = [P2_UP, P2_DOWN, P2_LEFT, P2_RIGHT, P2_DROP]

FPS = 60

SPRITES_DIR = path.dirname(__file__).replace("data", "resources\\sprites")
SOUNDS_DIR = path.dirname(__file__).replace("data", "resources\\sounds")
