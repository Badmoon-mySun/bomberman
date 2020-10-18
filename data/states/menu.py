from data.constants import *
from pygame import *
from data.sprites import *
from data.constants import SPRITES_DIR

menu_sprites_dir = path.join(SPRITES_DIR, "menu/")
length_line = 200
line_point = length_line // 100
volume_size = 100


class MainImage1:
    def __init__(self):
        self.image = transform.scale(image.load(menu_sprites_dir + "main_image1.png"), (175, 250))
        self.rect = self.image.get_rect(center=(WIN_WIDTH // 2 - 75, WIN_HEIGHT // 2 - 110))


class MainImage2:
    def __init__(self):
        self.image = transform.scale(image.load(menu_sprites_dir + "main_image2.png"), (150, 225))
        self.rect = self.image.get_rect(center=(WIN_WIDTH // 2 + 75, WIN_HEIGHT // 2 - 80))


class Play(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = image.load(menu_sprites_dir + "play.png")
        self.rect = self.image.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 + 70))


class Settings(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = image.load(menu_sprites_dir + "settings.png")
        self.rect = self.image.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 + 110))


class Exit(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = image.load(menu_sprites_dir + "exit.png")
        self.rect = self.image.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 + 150))


class MenuTime(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = image.load(menu_sprites_dir + "menu.png")
        self.rect = self.image.get_rect()
        self.play = Play()
        self.settings = Settings()
        self.exit = Exit()
        self.mainImage1 = MainImage1()
        self.mainImage2 = MainImage2()


class Back(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = image.load(menu_sprites_dir + "back.png")
        self.rect = self.image.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 + 150))


class Volume(sprite.Sprite):
    global length_line, volume_size

    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = Surface((350, 30))
        self.rect = self.image.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 + 100))
        self.bg_volume_line = Surface((200, self.image.get_height()))
        self.rect_bg_volume_line = self.bg_volume_line.get_rect()
        self.rect_sc_bg_volume_line = Rect((WIN_WIDTH // 2 - self.image.get_width() // 2,
                                            WIN_HEIGHT // 2 + 100 - self.image.get_height() // 2,
                                            self.bg_volume_line.get_width(), self.bg_volume_line.get_height()))
        self.volume_line = Surface((length_line, self.image.get_height()))
        self.rect_volume_line = self.volume_line.get_rect()
        self.font = font.Font(None, 30)
        self.volume_text = self.font.render(str(volume_size) + " volume", 1, WHITE)
        self.rect_volume_text = self.volume_text.get_rect(center=(275, 16))


def update_volume_line(events):
    global length_line, volume_size, line_point
    volume = Volume()
    volume.image.set_colorkey(BLACK)
    volume.volume_line.fill(RED)
    volume.bg_volume_line.fill(WHITE)
    volume.bg_volume_line.blit(volume.volume_line, volume.rect_volume_line)
    volume.image.blit(volume.bg_volume_line, volume.rect_bg_volume_line)
    volume.image.blit(volume.volume_text, volume.rect_volume_text)

    pressed = key.get_pressed()

    if pressed[K_LEFT]:
        if length_line > 0:
            length_line -= line_point
            volume_size -= 1
    elif pressed[K_RIGHT]:
        if length_line < 177:
            length_line += line_point
            volume_size += 1

    for i in events:
        if i.type == MOUSEBUTTONDOWN:
            if volume.rect_sc_bg_volume_line.collidepoint(i.pos[0], i.pos[1]):
                length_line = i.pos[0] - WIN_WIDTH // 2 + volume.image.get_width() // 2
                volume_size = length_line // line_point

    return volume


def draw_volume_line(screen, clock, events):
    volume = update_volume_line(events)
    screen.blit(volume.image, volume.rect)
    display.flip()
    clock.tick(FPS)


class SettingsTime(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = image.load(menu_sprites_dir + "menu.png")
        self.rect = self.image.get_rect()
        self.back = Back()
        self.mainImage1 = MainImage1()
        self.mainImage2 = MainImage2()


def menu_update():
    menu = MenuTime()
    menu.image.blit(menu.mainImage2.image, menu.mainImage2.rect)
    menu.image.blit(menu.mainImage1.image, menu.mainImage1.rect)
    menu.image.blit(menu.play.image, menu.play.rect)
    menu.image.blit(menu.settings.image, menu.settings.rect)
    menu.image.blit(menu.exit.image, menu.exit.rect)
    return menu


def menu_draw(screen, clock):
    menu_alive = True

    while menu_alive:
        menu = menu_update()
        screen.blit(menu.image, menu.rect)
        display.flip()
        clock.tick(FPS)

        for i in event.get():
            if i.type == QUIT or i.type == KEYDOWN and i.key == K_ESCAPE:
                exit()
            elif i.type == MOUSEBUTTONDOWN:
                if menu.play.rect.collidepoint(i.pos):
                    menu_alive = False
                if menu.settings.rect.collidepoint(i.pos):
                    settings_draw(screen, clock)
                if menu.exit.rect.collidepoint(i.pos):
                    exit()


def settings_update(clock, events):
    settings = SettingsTime()
    settings.image.blit(settings.mainImage2.image, settings.mainImage2.rect)
    settings.image.blit(settings.mainImage1.image, settings.mainImage1.rect)
    draw_volume_line(settings.image, clock, events)
    settings.image.blit(settings.back.image, settings.back.rect)
    return settings


def settings_draw(screen, clock):
    settings_alive = True

    while settings_alive:

        events = event.get()

        mixer.music.set_volume(volume_size / 100)
        settings = settings_update(clock, events)
        screen.blit(settings.image, settings.rect)
        display.flip()
        clock.tick(FPS)

        for i in events:
            if i.type == QUIT:
                exit()
            elif i.type == KEYDOWN and i.key == K_ESCAPE:
                settings_alive = False
            elif i.type == MOUSEBUTTONDOWN:
                if settings.back.rect.collidepoint(i.pos):
                    settings_alive = False
