from abc import ABC

from pygame import *
from data.constants import BLOCK_SIZE, SPRITES_DIR
from .blocks import AnimatedBlock, Obstacle, ExplosionBodyBlock, ExplosionFinishBlock, ExplosionCenterBlock


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
                if Rect.colliderect(self.rect, pl.player_mask):
                    flag = False

            if flag:
                self.level.obstacles.add(self)
                self.its_obstacle = True

        self.image = self.image
        self.time_delay -= 1
        if self.time_delay <= 0:
            self.kill()

    def is_destructible(self):
        return True

    def kill(self):
        sprite.Sprite.kill(self)
        self.bomb_explosion(self)

    def bomb_explosion(self, bomb):
        def add_explosion(block):
            flag = True
            for en in self.level.entities:
                if sprite.collide_rect(block, en):
                    if isinstance(en, Obstacle) and isinstance(en, sprite.Sprite) and en.is_destructible():
                        self.level.blow_up_block(en)
                        flag = False
                    else:
                        return False

            for pl in self.level.players:
                if Rect.colliderect(block.rect, pl.player_mask):
                    pl.damage()

            self.level.entities.add(block)
            return flag

        def line_explosion(array_pos, angle=0):
            for position in array_pos:
                if position != array_pos[len(array_pos) - 1]:
                    blk = ExplosionBodyBlock(position)
                else:
                    blk = ExplosionFinishBlock(position)

                if angle:
                    play = blk.explosion_play
                    blk.explosion_play = [transform.rotate(play[i], angle) for i in range(len(play))]

                if not add_explosion(blk):
                    break

        x = bomb.rect.x
        y = bomb.rect.y
        add_explosion(ExplosionCenterBlock(bomb.rect.topleft))

        line_explosion([(x + (BLOCK_SIZE * i), y) for i in range(1, bomb.force)])
        line_explosion([[x - (BLOCK_SIZE * i), y] for i in range(1, bomb.force)], 180)
        line_explosion([[x, y - (BLOCK_SIZE * i)] for i in range(1, bomb.force)], 90)
        line_explosion([[x, y + (BLOCK_SIZE * i)] for i in range(1, bomb.force)], 270)
