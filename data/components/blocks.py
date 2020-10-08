from abc import abstractmethod, ABC

from data.constants import *
from pygame import *
import os

sprites_dir = os.path.dirname(__file__).replace("data\\components", "resources\\sprites")


class Obstacle:
    @abstractmethod
    def is_destructible(self):
        pass


class Block(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.rect = Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)


class MetalPlate(Block, Obstacle, ABC):
    def __init__(self, x, y):
        Block.__init__(self, x, y)
        self.image = image.load("%s\\metal40.png" % sprites_dir)

    def is_destructible(self):
        return False


class Box(Block, Obstacle, ABC):
    def __init__(self, x, y):
        Block.__init__(self, x, y)
        self.image = image.load("%s\\box40.png" % sprites_dir)

    def is_destructible(self):
        return True


class GrassFloor:
    def __init__(self):
        self.image = Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.image = image.load("%s\\floor40.png" % sprites_dir)