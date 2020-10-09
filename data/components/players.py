from data.sprites import *
from data.constants import *
from pygame import *


class Player(sprite.Sprite):
    def __init__(self, level, sprites, setup, x, y):
        sprite.Sprite.__init__(self)
        self.rect = Rect(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.image = sprites.down_stand
        self.speed = PLAYER_SPEED
        self.sprites = sprites
        self.anim_count = 0
        self.setup = setup
        self.level = level
        self.last_move = "down"

        level.entities.add(self)

    def was_last_move(self, move):
        res = self.last_move == move
        if not res:
            self.anim_count = 0
            self.last_move = move
        else:
            self.anim_count += 1

        return res

    def frame_num(self, frames_count):
        pl_fps = FPS // 2
        if self.anim_count >= pl_fps:
            self.anim_count = 0

        return int(self.anim_count / (pl_fps / frames_count))

    def update(self, keys):
        last_x, last_y = self.rect.x, self.rect.y

        if keys[self.setup[0]]:
            self.was_last_move("up")

            self.rect.y -= self.speed
            self.image = self.sprites.up_play[self.frame_num(WALK_FRAMES)]
        elif keys[self.setup[1]]:
            self.was_last_move("down")

            self.rect.y += self.speed
            self.image = self.sprites.down_play[self.frame_num(WALK_FRAMES)]
        elif keys[self.setup[2]]:
            self.was_last_move("left")

            self.rect.x -= self.speed
            self.image = self.sprites.left_play[self.frame_num(WALK_FRAMES)]
        elif keys[self.setup[3]]:
            self.was_last_move("right")

            self.rect.x += self.speed
            self.image = self.sprites.right_play[self.frame_num(WALK_FRAMES)]
        else:
            if self.last_move == "up":
                self.image = self.sprites.up_stand
            elif self.last_move == "down":
                self.image = self.sprites.down_stand
            elif self.last_move == "left":
                self.image = self.sprites.left_stand
            elif self.last_move == "right":
                self.image = self.sprites.right_stand

        for obs in self.level.obstacles:
            if sprite.collide_rect(self, obs):
                if self.rect.y - 20 < obs.rect.y:
                    self.rect.x = last_x
                    self.rect.y = last_y
                    break
