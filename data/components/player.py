from data.constants import BLOCK_SIZE, PLAYER_SPEED
from pygame import *
import os

sprites_dir = os.path.dirname(__file__).replace("data\\components", "resources\\sprites")


class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load("%s\\player.png" % sprites_dir)
        self.rect = Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
        self.speed = PLAYER_SPEED

    def update(self, direction, obstacles):
        last_x, last_y = self.rect.x, self.rect.y

        if direction == K_UP:
            self.rect.y -= self.speed
        elif direction == K_DOWN:
            self.rect.y += self.speed
        elif direction == K_LEFT:
            self.rect.x -= self.speed
        elif direction == K_RIGHT:
            self.rect.x += self.speed

        for obs in obstacles:
            if sprite.collide_rect(self, obs):
                self.rect.x = last_x
                self.rect.y = last_y
                break
