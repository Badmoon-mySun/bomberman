from .blocks import *

level = ["###############",
         "#       -     #",
         "# # # # # # # #",
         "#             #",
         "# # # # # # # #",
         "#   -         #",
         "# # # # # # # #",
         "#             #",
         "# # # # # # # #",
         "#       -     #",
         "# # # # # # # #",
         "#   -         #",
         "###############"]


class Level:
    def __init__(self, screen):
        self.screen = screen
        self.entities = sprite.Group()
        self.blocks = []

        self.__draw_level()

    def __draw_level(self):
        x = y = 0
        for line in level:
            for blk in line:
                if blk != " ":
                    if blk == "#":
                        obstacle = MetalPlate(x, y)
                    else:
                        obstacle = Box(x, y)
                    self.entities.add(obstacle)
                    self.blocks.append(obstacle)
                else:
                    floor = Floor(x, y)
                    self.entities.add(floor)

                x += BLOCK_SIZE
            y += BLOCK_SIZE
            x = 0

    def update_level(self):
        for e in self.entities:
            self.screen.blit(e.image, (e.rect.x, e.rect.y))