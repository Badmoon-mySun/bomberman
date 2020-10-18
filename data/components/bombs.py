from abc import ABC

from pygame import *
from data.constants import BLOCK_SIZE, SPRITES_DIR
from .blocks import AnimatedBlock, Obstacle


class Bomb(sprite.Sprite, Obstacle, AnimatedBlock, ABC):
    def __init__(self, force, level, position):
        sprite.Sprite.__init__(self)
        self.image = image.load(SPRITES_DIR + "\\bomb\\bomb.png")
        self.rect = Rect(position, (BLOCK_SIZE, BLOCK_SIZE))
        self.its_obstacle = False
        self.time_delay = 100
        self.level = level
        self.force = force
        level.entities.add(self)

    def animate(self):
        if not self.its_obstacle:
            flag = True
            for pl in self.level.players:
                if sprite.collide_rect(self, pl):
                    flag = False

            if flag:
                self.level.obstacles.append(self)
                self.its_obstacle = True

        self.image = self.image
        self.time_delay -= 1
        if self.time_delay <= 0:
            self.kill()

    def is_destructible(self):
        return True

    def kill(self):
        sprite.Sprite.kill(self)
        if self.its_obstacle:
            self.level.obstacles.remove(self)
        self.level.bomb_explosion(self)

