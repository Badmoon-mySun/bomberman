from data.components.blocks import *


class Level:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.entities = sprite.Group()
        self.floor_surf = Surface(SCREEN_SIZE)
        self.player_pos = {}
        self.obstacles = []
        self.players = []
        self.x, self.y = x, y

    def update_level(self):
        # Накладываем пол на уровень
        self.screen.blit(self.floor_surf, (self.x, self.y))

        # Прорисовываем блоки
        for e in self.entities:
            if isinstance(e, AnimatedBlock):
                e.animate()
            self.screen.blit(e.image, e.rect.topleft)

        # Прорисовываем игроков
        for pl in self.players:
            pl.update(key.get_pressed())
            self.screen.blit(pl.image, pl.rect.topleft)

    def get_player_position(self, player_num):
        return self.player_pos.get(str(player_num))

    def add_player(self, player):
        if len(self.players) < len(self.player_pos):
            self.players.append(player)
        else:
            raise Exception("There is no place for a player")

    def bomb_explosion(self, bomb):
        def add_explosion_block(block):
            flag = True
            for en in self.entities:
                if sprite.collide_rect(block, en):
                    if isinstance(en, Obstacle) and isinstance(en, sprite.Sprite) and en.is_destructible():
                        en.kill()
                        if en in self.obstacles:
                            self.obstacles.remove(en)
                        flag = False
                    else:
                        return False

            self.entities.add(block)
            return flag

        def line_explosion_blocks(array_pos, angle=0):
            for position in array_pos:
                if position != array_pos[len(array_pos) - 1]:
                    blk = ExplosionBodyBlock(position[0], position[1])
                else:
                    blk = ExplosionFinishBlock(position[0], position[1])

                if angle:
                    play = blk.explosion_play
                    blk.explosion_play = [transform.rotate(play[i], angle) for i in range(len(play))]

                if not add_explosion_block(blk):
                    break

        x = bomb.rect.x
        y = bomb.rect.y
        self.entities.add(ExplosionCenterBlock(x, y))

        line_explosion_blocks([(x + (BLOCK_SIZE * i), y) for i in range(1, bomb.force)])
        line_explosion_blocks([[x - (BLOCK_SIZE * i), y] for i in range(1, bomb.force)], 180)
        line_explosion_blocks([[x, y - (BLOCK_SIZE * i)] for i in range(1, bomb.force)], 90)
        line_explosion_blocks([[x, y + (BLOCK_SIZE * i)] for i in range(1, bomb.force)], 270)


first_level = ["###############",
               "#1   ------  4#",
               "# #-#-#-#-#-# #",
               "#  ---- - - - #",
               "#-#-#-#-#-#-#-#",
               "#----- -------#",
               "#-#-#-# #-#-# #",
               "# --   - -----#",
               "#-# # #-#-#-#-#",
               "# - ----  --- #",
               "# # #-#-#-#-# #",
               "#3  --- ---  2#",
               "###############"]


class FirstLevel(Level):
    def __init__(self, screen, x, y):
        Level.__init__(self, screen, x, y)

        self.__draw_level()

    def __draw_level(self):
        x, y = self.x, self.y  # Координаты экрана с которого начинается прорисовка уровня
        floor = GrassFloor()  # Пол - трава

        for line in first_level:
            for blk in line:
                self.floor_surf.blit(floor.image, (x, y))

                if blk not in [" ", "1", "2", "3", "4"]:
                    if blk == "#":
                        obstacle = MetalPlate(x, y)
                    else:
                        obstacle = Box(x, y)

                    self.entities.add(obstacle)  # Добавляем в Group для прорисовки
                    self.obstacles.append(obstacle)  # Добавляем в список для проверки коллизий

                elif blk in [str(i) for i in range(5)]:
                    self.player_pos[blk] = (x, y)

                x += BLOCK_SIZE
            y += BLOCK_SIZE
            x = self.x
