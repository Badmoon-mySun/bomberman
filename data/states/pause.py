from data.constants import *
from pygame import *
from data.sprites import *

pause_sprites_dir = path.join(SPRITES_DIR, "pause/")


class TextMenu:
    def __init__(self):
        self.image = font.Font(None, 25).render("PAUSE", 0, (0, 180, 0))
        self.rect = self.image.get_rect(center=(PAUSE_WIDTH // 2, PAUSE_HEIGHT // 5 * 1))


class ExitButton(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = image.load(pause_sprites_dir + "exit.png")
        self.rect = self.image.get_rect(center=(PAUSE_WIDTH // 4 * 1, PAUSE_HEIGHT // 6 * 3))


class ReplayButton(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = image.load(pause_sprites_dir + "replay.png")
        self.rect = self.image.get_rect(center=(PAUSE_WIDTH // 4 * 2, PAUSE_HEIGHT // 6 * 3))


class PlayButton(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = image.load(pause_sprites_dir + "play.png")
        self.rect = self.image.get_rect(center=(PAUSE_WIDTH // 4 * 3, PAUSE_HEIGHT // 6 * 3))


class PauseText(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = font.Font(None, 30).render("PAUSE", 1, (255, 255, 255))
        self.rect = self.image.get_rect(center=(PAUSE_WIDTH // 2, PAUSE_HEIGHT // 8 * 2))


class PauseTime(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(pause_sprites_dir + "pause.png"), (PAUSE_WIDTH, PAUSE_HEIGHT))
        self.rect = self.image.get_rect(center=CENTER)
        self.pause_text = PauseText()
        self.exitButton = ExitButton()
        self.rectExitButton = Rect((
            WIN_WIDTH // 2 - self.image.get_width() // 2 +
            PAUSE_WIDTH // 4 * 1 - self.exitButton.image.get_width() // 2,
            WIN_HEIGHT // 2 - self.image.get_height() // 2 +
            PAUSE_HEIGHT // 6 * 3 - self.exitButton.image.get_height() // 2,
            self.exitButton.image.get_width(), self.exitButton.image.get_height()))
        self.replayButton = ReplayButton()
        self.rectReplayButton = Rect((
            WIN_WIDTH // 2 - self.image.get_width() // 2 +
            PAUSE_WIDTH // 4 * 2 - self.replayButton.image.get_width() // 2,
            WIN_HEIGHT // 2 - self.image.get_height() // 2 +
            PAUSE_HEIGHT // 6 * 3 - self.replayButton.image.get_height() // 2,
            self.replayButton.image.get_width(), self.replayButton.image.get_height()))
        self.playButton = PlayButton()
        self.rectPlayButton = Rect((
            WIN_WIDTH // 2 - self.image.get_width() // 2 +
            PAUSE_WIDTH // 4 * 3 - self.playButton.image.get_width() // 2,
            WIN_HEIGHT // 2 - self.image.get_height() // 2 +
            PAUSE_HEIGHT // 6 * 3 - self.playButton.image.get_height() // 2,
            self.playButton.image.get_width(), self.playButton.image.get_height()))


def pause_update():
    pause = PauseTime()
    pause.image.blit(pause.pause_text.image, pause.pause_text.rect)
    pause.image.blit(pause.exitButton.image, pause.exitButton.rect)
    pause.image.blit(pause.replayButton.image, pause.replayButton.rect)
    pause.image.blit(pause.playButton.image, pause.playButton.rect)
    return pause


def pause_draw(screen, clock):
    is_paused = True

    while is_paused:
        pause = pause_update()
        screen.blit(pause.image, pause.rect)
        display.flip()
        clock.tick(FPS)

        for i in event.get():
            if i.type == QUIT:
                exit()
            elif i.type == KEYDOWN and i.key == K_ESCAPE:
                is_paused = False
            elif i.type == MOUSEBUTTONDOWN:
                if pause.rectExitButton.collidepoint(i.pos[0], i.pos[1]):
                    return 1
                if pause.rectReplayButton.collidepoint(i.pos[0], i.pos[1]):
                    is_paused = False
                if pause.rectPlayButton.collidepoint(i.pos[0], i.pos[1]):
                    is_paused = False
