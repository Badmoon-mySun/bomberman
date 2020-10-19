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
    def __init__(self, position):
        sprite.Sprite.__init__(self)
        self.image = Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.rect = Rect(position, (BLOCK_SIZE, BLOCK_SIZE))


class MetalPlate(Block, Obstacle, ABC):
    def __init__(self, position):
        Block.__init__(self, position)
        self.image = MetalBlockSprite().image

    def is_destructible(self):
        return False


class Box(Block, Obstacle, ABC):
    def __init__(self, position):
        Block.__init__(self, position)
        self.image = BoxBlockSprite().image

    def is_destructible(self):
        return True


class MetalColumn(Block, Obstacle, ABC):
    def __init__(self, position):
        Block.__init__(self, position)
        self.image = MetalColumnBlockSprite().image

    def is_destructible(self):
        return False


class Board(Block, Obstacle, ABC):
    def __init__(self, position):
        Block.__init__(self, position)
        self.image = BoardBlockSprite().image

    def is_destructible(self):
        return True


class ExplosionCenterBlock(Block, AnimatedBlock, ABC):
    def __init__(self, position):
        Block.__init__(self, position)
        self.explosion_play = ExplosionCenterSprites().explosion_play
        self.anim_count = 0

    def animate(self):
        if self.anim_count < len(self.explosion_play) * 10:
            self.image = self.explosion_play[self.anim_count // 10]
            self.anim_count += 4
        else:
            self.kill()


class ExplosionBodyBlock(Block, AnimatedBlock, ABC):
    def __init__(self, position):
        Block.__init__(self, position)
        self.explosion_play = ExplosionBodySprites().explosion_play
        self.anim_count = 0

    def animate(self):
        if self.anim_count < len(self.explosion_play) * 10:
            self.image = self.explosion_play[self.anim_count // 10]
            self.anim_count += 4
        else:
            self.kill()


class ExplosionFinishBlock(Block, AnimatedBlock, ABC):
    def __init__(self, position):
        Block.__init__(self, position)
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


class RectGrass:
    def __init__(self):
        self.image = RectGrassSprite().image


class PlayerHeart:
    def __init__(self):
        self.image = PlayerHeartSprite().image


class Background:
    def __init__(self):
        self.image = BackgroundSprite().image
