from abc import abstractmethod, ABC

from data.constants import *
from pygame import *
from data.sprites import *


class Obstacle:
    @abstractmethod
    def is_destructible(self):
        pass


class AnimatedBlock:
    @abstractmethod
    def animate(self):
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


class ExplosionCenterBlock(Block, AnimatedBlock, ABC):
    def __init__(self, x, y):
        Block.__init__(self, x, y)
        self.explosion_play = ExplosionCenterSprites().explosion_play
        self.anim_count = 0

    def animate(self):
        if self.anim_count < len(self.explosion_play) * 10:
            self.image = self.explosion_play[self.anim_count // 10]
            self.anim_count += 4
        else:
            self.kill()


class ExplosionBodyBlock(Block, AnimatedBlock, ABC):
    def __init__(self, x, y):
        Block.__init__(self, x, y)
        self.explosion_play = ExplosionBodySprites().explosion_play
        self.anim_count = 0

    def animate(self):
        if self.anim_count < len(self.explosion_play) * 10:
            self.image = self.explosion_play[self.anim_count // 10]
            self.anim_count += 4
        else:
            self.kill()


class ExplosionFinishBlock(Block, AnimatedBlock, ABC):
    def __init__(self, x, y):
        Block.__init__(self, x, y)
        self.explosion_play = ExplosionFinishSprites().explosion_play
        self.anim_count = 0

    def animate(self):
        if self.anim_count < len(self.explosion_play) * 10:
            self.image = self.explosion_play[self.anim_count // 10]
            self.anim_count += 4
        else:
            self.kill()


class GrassFloor:
    def __init__(self):
        self.image = GrassBlockSprite().image
