import random

from data.components.blocks import *
from data.components.bombs import Bomb
from data.components.bonuses import all_bonuses
from os import path


class Level:
    def __init__(self, screen, position):
        self.screen = screen
        self.obstacles = sprite.Group()
        self.entities = sprite.Group()
        self.players = sprite.Group()
        self.floor_surf = Surface(SCREEN_SIZE)
        self.player_pos = {}
        self.game_over = GameOverSprite().image
        self.x, self.y = position[0], position[1]

    def update(self):
        # Накладываем пол на уровень
        self.screen.blit(self.floor_surf, (self.x, self.y))

        x, y = self.x, self.y
        for pl in self.players:
            x += BLOCK_SIZE
            self.screen.blit(pl.sprites.icon, (x, y))
            for i in range(pl.health):
                x += BLOCK_SIZE
                self.screen.blit(PlayerHeart().image, (x, y))

            x += (MAX_PLAYER_HEALTH - pl.health + 1) * BLOCK_SIZE

        # Прорисовываем блоки
        for e in self.entities:
            if isinstance(e, AnimatedBlock):
                e.animate()
            self.screen.blit(e.image, e.rect.topleft)

        # Прорисовываем игроков
        for pl in self.players:
            pl.update()
            self.screen.blit(pl.image, pl.rect.topleft)

    def get_player_position(self, player_num):
        return self.player_pos.get(str(player_num))

    def add_player(self, player):
        if len(self.players) < len(self.player_pos):
            self.players.add(player)
        else:
            raise Exception("There is no place for a player")

    def blow_up_block(self, entity):
        entity.kill()
        if not isinstance(entity, Bomb) and not random.choice([0, 1, 2]):
            bonus_class = random.choice(all_bonuses)
            bonus = bonus_class(entity.rect.topleft)
            self.obstacles.add(bonus)
            self.entities.add(bonus)

    def game_is_over(self):
        return len(self.players) <= 1

    def game_over_show(self):
        self.screen.blit(self.game_over, (self.x, self.y))


first_level = ["@@@@@@@@@@@@@@@",
               "###############",
               "#1   ------   #",
               "# #-#-#-#-#-# #",
               "#  ---- - - - #",
               "#-#-#-#-#-#-#-#",
               "#----- -------#",
               "#-#-#-# #-#-# #",
               "# --   - -----#",
               "#-# # #-#-#-#-#",
               "# - ----  --- #",
               "# # #-#-#-#-# #",
               "#   --- ---  2#",
               "###############"]

second_level = ["@@@@@@@@@@@@@@@",
                "###############",
                "#1 - --#-- -  #",
                "# #- #- -# -# #",
                "# #--- #- - # #",
                "#- -#-#-#-#- -#",
                "#-# --- --- #-#",
                "# --#-#-#-#-- #",
                "#-#--- - ---#-#",
                "# - #-#-#-# - #",
                "#-# --- --- #-#",
                "# #--# - #--# #",
                "#  -# -#- #- 2#",
                "###############"]


def draw_level(level, level_array, floor_class, box_class, metal_class):
    x, y = level.x, level.y  # Координаты экрана с которого начинается прорисовка уровня
    floor = floor_class()

    for line in level_array:
        for blk in line:
            level.floor_surf.blit(floor.image, (x, y))

            if blk not in [" ", "1", "2", "3", "4", "@"]:
                if blk == "#":
                    obstacle = metal_class((x, y))
                else:
                    obstacle = box_class((x, y))

                level.entities.add(obstacle)  # Добавляем в Group для прорисовки
                level.obstacles.add(obstacle)  # Добавляем в список для проверки коллизий

            elif blk in [str(i) for i in range(5)] and line != level_array[0]:
                level.player_pos[blk] = (x, y - PLAYER_HEIGHT + BLOCK_SIZE)

            elif blk == "@":
                level.floor_surf.blit(Background().image, (x, y))
            x += BLOCK_SIZE
        y += BLOCK_SIZE
        x = level.x


class FirstLevel(Level):
    def __init__(self, screen, position):
        Level.__init__(self, screen, position)
        draw_level(self, first_level, GrassFloor, Box, MetalPlate)


class SecondLevel(Level):
    def __init__(self, screen, position):
        Level.__init__(self, screen, position)
        draw_level(self, second_level, RectGrass, Board, MetalColumn)
