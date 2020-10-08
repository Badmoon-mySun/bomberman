from pygame import *

# Размер блока
BLOCK_SIZE = 40

# Размеры игрока
PLAYER_WIDTH = 34
PLAYER_HEIGHT = 48

# Количество блоков в ширину и в длину
WIDTH_BLOCKS_COUNT = 15
HEIGHT_BLOCS_COUNT = 13

# Высчитываем размары экрана в зависимости от количества и размера блоков
WIN_WIDTH = WIDTH_BLOCKS_COUNT * BLOCK_SIZE
WIN_HEIGHT = HEIGHT_BLOCS_COUNT * BLOCK_SIZE

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
