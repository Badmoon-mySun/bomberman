from abc import ABC

from data.components.blocks import Obstacle
from data.constants import *
from data.sprites import SpeedBonusSprite, BombBonusSprite, ForceBonusSprite, HealBonusSprite


class Bonus(sprite.Sprite, Obstacle, ABC):
    def __init__(self, position):
        sprite.Sprite.__init__(self)
        self.rect = Rect(position, (BLOCK_SIZE, BLOCK_SIZE))

    def use_bonus(self, player):
        pass

    def is_destructible(self):
        return False


class SpeedBonus(Bonus, ABC):
    def __init__(self, position):
        Bonus.__init__(self, position)
        self.image = SpeedBonusSprite().image

    def use_bonus(self, player):
        if player.speed <= MAX_PLAYER_SPEED:
            player.speed += 1

        self.kill()


class BombBonus(Bonus, ABC):
    def __init__(self, position):
        Bonus.__init__(self, position)
        self.image = BombBonusSprite().image

    def use_bonus(self, player):
        if player.bomb_count <= MAX_PLAYER_BOMB_COUNT:
            player.bomb_count += 1

        self.kill()


class ForceBonus(Bonus, ABC):
    def __init__(self, position):
        Bonus.__init__(self, position)
        self.image = ForceBonusSprite().image

    def use_bonus(self, player):
        if player.force <= MAX_PLAYER_FORCE:
            player.force += 1

        self.kill()


class HealBonus(Bonus, ABC):
    def __init__(self, position):
        Bonus.__init__(self, position)
        self.image = HealBonusSprite().image

    def use_bonus(self, player):
        if player.health <= MAX_PLAYER_HEALTH:
            player.health += 1

        self.kill()


all_bonuses = [SpeedBonus, BombBonus, HealBonus, ForceBonus]