from .constants import SPRITES_DIR
from pygame import image
from os import path

DEATH_FRAMES = 8
WALK_FRAMES = 6


class PlayerSprites:
    def __init__(self,  files_pred):
        self.up_stand = image.load(path.join(SPRITES_DIR, "%s_up.png" % files_pred))
        self.down_stand = image.load(path.join(SPRITES_DIR, "%s_down.png" % files_pred))
        self.left_stand = image.load(path.join(SPRITES_DIR, "%s_left.png" % files_pred))
        self.right_stand = image.load(path.join(SPRITES_DIR, "%s_right.png" % files_pred))
        self.up_play = [image.load(path.join(SPRITES_DIR, "%s_up_%s.png" % (files_pred, i)))
                        for i in range(1, WALK_FRAMES + 1)]
        self.down_play = [image.load(path.join(SPRITES_DIR, "%s_down_%s.png" % (files_pred, i)))
                          for i in range(1, WALK_FRAMES + 1)]
        self.left_play = [image.load(path.join(SPRITES_DIR, "%s_left_%s.png" % (files_pred, i)))
                          for i in range(1, WALK_FRAMES + 1)]
        self.right_play = [image.load(path.join(SPRITES_DIR, "%s_right_%s.png" % (files_pred, i)))
                           for i in range(1, WALK_FRAMES + 1)]

        # self.death_play = [image.load("%s\\%s_death_%s.png" %
        #                               (pl_sprites_dir, files_pred, i)) for i in range(1, DEATH_FRAMES)]


class BluePlayerSprites(PlayerSprites):
    def __init__(self):
        PlayerSprites.__init__(self, "player/blue_player/blue_player")


class WhitePlayerSprites(PlayerSprites):
    def __init__(self):
        PlayerSprites.__init__(self, "player/white_player/white_player")


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
        self.image = image.load(path.join(SPRITES_DIR, "%s.png" % files_pred))


class BlockPlaySpriteSingleton:
    __instance = {}

    @staticmethod
    def get_instance(file_pred, play_count):
        instance = BlockPlaySpriteSingleton.__instance
        if file_pred not in instance:
            instance[file_pred] = BlockPlaySpriteSingleton(file_pred, play_count)
            return instance[file_pred]
        return instance[file_pred]

    def __init__(self, files_pred, play_count):
        self.block_play = [image.load(path.join(SPRITES_DIR, "%s_%s.png"
                                                    % (files_pred, i))) for i in range(1, play_count + 1)]


class BlockSprite:
    def __init__(self, file_pred):
        self.image = BlockSpriteSingleton.get_instance(file_pred).image


class BoxBlockSprite(BlockSprite):
    def __init__(self):
        BlockSprite.__init__(self, "block/box")


class MetalBlockSprite(BlockSprite):
    def __init__(self):
        BlockSprite.__init__(self, "block/metal")


class GrassBlockSprite(BlockSprite):
    def __init__(self):
        BlockSprite.__init__(self, "block/grass")


class ExplosionBlockSprite:
    def __init__(self, file_pred, play_count):
        self.explosion_play = BlockPlaySpriteSingleton.get_instance(file_pred, play_count).block_play


class ExplosionCenterSprites(ExplosionBlockSprite):
    def __init__(self):
        ExplosionBlockSprite.__init__(self, "bomb/explosion_center", 4)


class ExplosionBodySprites(ExplosionBlockSprite):
    def __init__(self):
        ExplosionBlockSprite.__init__(self, "bomb/explosion_body", 4)


class ExplosionFinishSprites(ExplosionBlockSprite):
    def __init__(self):
        ExplosionBlockSprite.__init__(self, "bomb/explosion_finish", 4)


class SpeedBonusSprite(BlockSprite):
    def __init__(self):
        BlockSprite.__init__(self, "bonus/bonus_speed")


class HealBonusSprite(BlockSprite):
    def __init__(self):
        BlockSprite.__init__(self, "bonus/bonus_heal")


class BombBonusSprite(BlockSprite):
    def __init__(self):
        BlockSprite.__init__(self, "bonus/bonus_bomb")


class ForceBonusSprite(BlockSprite):
    def __init__(self):
        BlockSprite.__init__(self, "bonus/bonus_force")
