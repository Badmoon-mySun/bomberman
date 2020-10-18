from data.sprites import *
from data.constants import *
from pygame import *
from .bombs import Bomb


class Player(sprite.Sprite):
    def __init__(self, level, sprites, setup, position):
        sprite.Sprite.__init__(self)
        self.rect = Rect(position, (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.max_bomb_count = PLAYER_BOMB_COUNT
        self.speed = PLAYER_SPEED
        self.force = PLAYER_FORCE
        self.health = PLAYER_HP
        self.sprites = sprites
        self.anim_count = 0
        self.setup = setup
        self.level = level
        self.last_move = "down"
        self.bombs_dropped = []
        self.player_mask = Rect((0, 0), (PL_MASK_WIDTH, PL_MASK_HEIGHT))
        self.__move_mask(position)
        level.add_player(self)

    def __move_mask(self, player_pos):
        # config
        position_x = player_pos[0] + 1
        position_y = player_pos[1] + (PLAYER_HEIGHT - PL_MASK_HEIGHT)

        self.player_mask.topleft = (position_x, position_y)

    def was_last_move(self, move):
        res = self.last_move == move
        if not res:
            self.anim_count = 0
            self.last_move = move
        else:
            self.anim_count += 1

        return res

    def frame_num(self, frames_count):
        pl_fps = FPS // 1.5
        if self.anim_count >= pl_fps:
            self.anim_count = 0

        return int(self.anim_count / (pl_fps / frames_count))

    def set_bomb(self, position):
        for bomb in self.bombs_dropped:
            if not bomb.alive():
                self.bombs_dropped.remove(bomb)

        flag = True
        for bomb in self.bombs_dropped:
            if bomb.rect.topleft == position:
                flag = False

        bomb_count = len(self.bombs_dropped)
        if self.max_bomb_count > bomb_count and flag:
            bomb = Bomb(3, self.level, position)
            self.bombs_dropped.append(bomb)

    def damage(self):
        self.health -= 1

    def update(self):
        keys = key.get_pressed()
        if self.health > 0:
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

            if keys[self.setup[4]]:
                x = self.player_mask.centerx // BLOCK_SIZE * BLOCK_SIZE
                y = self.player_mask.centery // BLOCK_SIZE * BLOCK_SIZE

                self.set_bomb((x, y))

            self.__move_mask((self.rect.x, self.rect.y))

            for obs in self.level.obstacles:
                if Rect.colliderect(self.player_mask, obs.rect):
                    self.__move_mask((last_x, last_y))
                    self.rect.x = last_x
                    self.rect.y = last_y
                    break
        else:
            self.was_last_move("die")
            # self.image = self.sprites.death_play[self.frame_num(WALK_FRAMES)]
            self.kill()

    def kill(self):
        sprite.Sprite.kill(self)
        self.level.players.remove(self)
