from .constants import SPRITES_DIR
from pygame import image
from os import path

pl_sprites_dir = path.join(SPRITES_DIR, "player")
blk_sprites_dir = path.join(SPRITES_DIR, "block")

DEATH_FRAMES = 8
WALK_FRAMES = 6


class PlayerSprites:
    def __init__(self,  files_pred):
        self.up_stand = image.load(path.join(pl_sprites_dir, "%s_up.png" % files_pred))
        self.down_stand = image.load(path.join(pl_sprites_dir, "%s_down.png" % files_pred))
        self.left_stand = image.load(path.join(pl_sprites_dir, "%s_left.png" % files_pred))
        self.right_stand = image.load(path.join(pl_sprites_dir, "%s_right.png" % files_pred))
        self.up_play = [image.load(path.join(pl_sprites_dir, "%s_up_%s.png" % (files_pred, i)))
                        for i in range(1, WALK_FRAMES + 1)]
        self.down_play = [image.load(path.join(pl_sprites_dir, "%s_down_%s.png" % (files_pred, i)))
                          for i in range(1, WALK_FRAMES + 1)]
        self.left_play = [image.load(path.join(pl_sprites_dir, "%s_left_%s.png" % (files_pred, i)))
                          for i in range(1, WALK_FRAMES + 1)]
        self.right_play = [image.load(path.join(pl_sprites_dir, "%s_right_%s.png" % (files_pred, i)))
                           for i in range(1, WALK_FRAMES + 1)]

        # self.death_play = [image.load("%s\\%s_death_%s.png" %
        #                               (pl_sprites_dir, files_pred, i)) for i in range(1, DEATH_FRAMES)]


class BluePlayerSprites(PlayerSprites):
    def __init__(self):
        PlayerSprites.__init__(self, "blue_player/blue_player")


class WhitePlayerSprites(PlayerSprites):
    def __init__(self):
        PlayerSprites.__init__(self, "white_player/white_player")


class BlockSpriteSingleton:
    __instance = {}

    @staticmethod
    def get_instance(file_pred):
        instance = BlockSpriteSingleton.__instance
        if file_pred not in instance:
            instance[file_pred] = BlockSpriteSingleton(file_pred)
            return instance[file_pred]
        return instance[file_pred]

    def __init__(self, files_pred):
        self.image = image.load(path.join(blk_sprites_dir, "%s_block.png" % files_pred))


class BlockSprite:
    def __init__(self, file_pred):
        self.image = BlockSpriteSingleton.get_instance(file_pred).image


class BoxBlockSprite(BlockSprite):
    def __init__(self):
        BlockSprite.__init__(self, "box")


class MetalBlockSprite(BlockSprite):
    def __init__(self):
        BlockSprite.__init__(self, "metal")


class GrassBlockSprite(BlockSprite):
    def __init__(self):
        BlockSprite.__init__(self, "grass")
