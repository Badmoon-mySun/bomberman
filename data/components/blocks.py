from abc import abstractmethod, ABC

from data.constants import *
from pygame import *
from data.sprites import *


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
        self.image = MetalBlockSprite().image

    def is_destructible(self):
        return False


class Box(Block, Obstacle, ABC):
    def __init__(self, x, y):
        Block.__init__(self, x, y)
        self.image = BoxBlockSprite().image

    def is_destructible(self):
        return True


class GrassFloor:
    def __init__(self):
        self.image = GrassBlockSprite().image
