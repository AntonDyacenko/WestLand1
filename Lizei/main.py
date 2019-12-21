import pygame
import tkinter as tk
import math

root = tk.Tk()
DISPLAY_SIZE = (root.winfo_screenwidth(), root.winfo_screenheight())

HERO_SPEED = 600 / 1000
JUMP_SPEED = 800 / 1000
# Загрузка изображений
projectile = pygame.image.load("Снаряд.png")  # Снаряд героя

# Герой идёт вперёд
hero_go = [pygame.image.load("1.png"), pygame.image.load("2.png"), pygame.image.load("3.png"),
           pygame.image.load("4.png"),
           pygame.image.load("5.png"), pygame.image.load("6.png"), pygame.image.load("7.png"),
           pygame.image.load("8.png"),
           pygame.image.load("9.png"), pygame.image.load("10.png"), pygame.image.load("11.png")]

# Герой идёт задом
hero_go_2 = [pygame.image.load("11.png"), pygame.image.load("10.png"), pygame.image.load("9.png"),
             pygame.image.load("8.png"), pygame.image.load("7.png"), pygame.image.load("6.png"),
             pygame.image.load("5.png"),
             pygame.image.load("4.png"), pygame.image.load("3.png"), pygame.image.load("2.png"),
             pygame.image.load("1.png")]

# Герой идёт стоит на месте
hero_stand = pygame.image.load("hero_stand.png")

# Рука с бластером
hand = pygame.image.load("рука.png")

# Задний фон
bg = pygame.image.load("Проект.jpg")
bg = pygame.transform.scale(bg, (15000 - int(15000 % DISPLAY_SIZE[0]), DISPLAY_SIZE[1]))


class Hero:

    def __init__(self, x, y):
        self._coords = (x, y)

    def move(self, delta_pos):
        self._coords = (self._coords[0] + delta_pos[0],
                        self._coords[1] + delta_pos[1])

    def get_position(self):
        return self._coords


class GameWorld:

    def __init__(self, start_x, start_y):
        self._player = Hero(start_x, start_y)
        self.coor_Picture = 0
        self.A = False
        self.D = False
        self.clock = pygame.time.Clock()
        self.Moment = 0
        self.i = 0
        self.angle = 0
        self.y_mouse = 0
        self.x_mouse = 0

    def mouse_input_continues(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.x_mouse = event.pos[0]
            self.y_mouse = event.pos[1]

    def process_input_continues(self, pressed_keys, dt):
        if pressed_keys[pygame.K_d]:
            self.A = False
            self.D = True
            if 0 <= self._player.get_position()[0] <= DISPLAY_SIZE[0] / 5:
                self._player.move((HERO_SPEED * dt, 0))
            elif DISPLAY_SIZE[0] / 5 < self._player.get_position()[0] and self.coor_Picture >= - (
                    15000 - 2 * DISPLAY_SIZE[0]):
                self.coor_Picture -= HERO_SPEED * dt
            elif self._player.get_position()[0] <= DISPLAY_SIZE[0] - 143:
                self._player.move((HERO_SPEED * dt, 0))
            else:
                self.A = False
                self.D = False
        elif pressed_keys[pygame.K_a]:
            self.D = False
            self.A = True
            if (self._player.get_position()[0] == 1660 or self._player.get_position()[0] != DISPLAY_SIZE[0] / 5) and \
                    self._player.get_position()[0] >= 100:
                self._player.move((-HERO_SPEED * dt, 0))
            else:
                if self.coor_Picture <= -100:
                    self.coor_Picture += HERO_SPEED * dt
                else:
                    if self._player.get_position()[0] >= 100:
                        self._player.move((-HERO_SPEED * dt, 0))
                    else:
                        self.A = False
                        self.D = False
        else:
            self.A = False
            self.D = False

    def rot_center(self, image, angle):
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image

    def draw(self, surf):
        Hero = hero_stand
        pl_x, pl_y = self._player.get_position()
        self.angle = math.atan(-(self.y_mouse - pl_y - 40) / (self.x_mouse - pl_x - 40)) * 180 / math.pi
        if not self.D and not self.A:
            Hero = hero_stand
        else:
            self.Moment += self.clock.tick()
            if self.Moment >= 70:
                self.i += 1
                self.Moment = 0
            if self.i > 10:
                self.i = 0
            if self.D:
                Hero = hero_go[self.i]
            elif self.A:
                Hero = hero_go_2[self.i]
        surf.blit(bg, (self.coor_Picture, 0))
        surf.blit(Hero, (pl_x - 10, pl_y, 20, 20))
        screen.blit(self.rot_center(hand, self.angle), (pl_x - 50, pl_y - 50))


class Monster:
    def __init__(self, start_x, start_y):
        self._player = Hero(start_x, start_y)
        self.x_hero = self._player.get_position()[0]


class Game:

    def __init__(self, surf):
        self._world = GameWorld(10, DISPLAY_SIZE[1] - 300)
        self._surf = surf

    def loop(self):
        self._world.draw(self._surf)

    def process_input_continues(self, pressed_keys, dt):
        self._world.process_input_continues(pressed_keys, dt)

    def mouse_input_continues(self, event):
        self._world.mouse_input_continues(event)


pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

game = Game(screen)
clock = pygame.time.Clock()

running = True
while running:

    dt = clock.tick()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        game.mouse_input_continues(event)
    game.process_input_continues(pygame.key.get_pressed(), dt)

    screen.fill((0, 0, 0))
    game.loop()
    pygame.display.flip()

pygame.quit()

print()
