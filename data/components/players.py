from .players_sprites import *
from data.constants import *
from pygame import *


class Player(sprite.Sprite):
    def __init__(self, level, setup, x, y):
        sprite.Sprite.__init__(self)
        self.image = first_player_sprite
        self.rect = Rect(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.setup = setup
        self.speed = PLAYER_SPEED
        self.level = level

        level.entities.add(self)

    def update(self, keys):
        last_x, last_y = self.rect.x, self.rect.y

        if keys[self.setup[0]]:
            self.rect.y -= self.speed
        elif keys[self.setup[1]]:
            self.rect.y += self.speed
        elif keys[self.setup[2]]:
            self.rect.x -= self.speed
        elif keys[self.setup[3]]:
            self.rect.x += self.speed

        for obs in self.level.obstacles:
            if sprite.collide_rect(self, obs):
                if self.rect.y - 20 < obs.rect.y:
                    self.rect.x = last_x
                    self.rect.y = last_y
                    break


class FirstPlayer(Player):
    def __init__(self, level, setup, x, y):
        Player.__init__(self, level, setup, x, y)
        self.image = first_player_sprite
