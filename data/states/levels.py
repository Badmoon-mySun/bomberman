from data.components.blocks import *


class Level:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.entities = sprite.Group()
        self.floor_surf = Surface(SCREEN_SIZE)
        self.player_pos = {}
        self.obstacles = []
        self.x, self.y = x, y

    def update_level(self):
        # Накладываем пол на уровень
        self.screen.blit(self.floor_surf, (self.x, self.y))

        # Прорисовываем блоки
        for e in self.entities:
            self.screen.blit(e.image, (e.rect.x, e.rect.y))

    def get_player_position(self, player_num):
        return self.player_pos.get(str(player_num))


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

second_level = ["###############",
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
