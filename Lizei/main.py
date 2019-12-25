import pygame
import tkinter as tk
import math

# я на месте, детка
root = tk.Tk()
DISPLAY_SIZE = (root.winfo_screenwidth(), root.winfo_screenheight())

HERO_SPEED = 600 / 1000
JUMP_SPEED = 800 / 1000
FIRE_SPEED = 2
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
        self.fire_x = 0
        self.fire_y = 0
        self.Fire = False
        self.number_fire = 0
        self.fire_coordinate = []

    def take_angle(self):
        return self.angle

    def mouse_input_continues(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.x_mouse = event.pos[0]
            self.y_mouse = event.pos[1]
        # Стрельба, нажатие на клавишу, колличество пуль
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.Fire = True
                self.number_fire += 1
                self.fire_coordinate.append(
                    [self._player.get_position()[0] + 40, self._player.get_position()[1] + 48, self.angle])

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

        # Стрельба, скорость пули, управление координатой, удаление пули, после того, как она вышла за экран игрока
        i = 0
        while i != self.number_fire:
            if self.fire_coordinate[i][0] <= 1.4 * DISPLAY_SIZE[0]:
                self.fire_coordinate[i][0] += FIRE_SPEED * dt * math.sin(
                    (self.fire_coordinate[i][2] + 90) * math.pi / 180)
                self.fire_coordinate[i][1] += FIRE_SPEED * dt * math.cos(
                    (self.fire_coordinate[i][2] + 90) * math.pi / 180)
                i += 1
            else:
                self.number_fire -= 1
                del self.fire_coordinate[i]

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
        if self.x_mouse - pl_x - 60 != 0:
            self.angle = math.atan(-(self.y_mouse - pl_y - 50) / (self.x_mouse - pl_x - 60)) * 180 / math.pi
        else:
            self.angle = math.atan(-(self.y_mouse - pl_y - 50) / 1) * 180 / math.pi
        if math.ceil(self.angle) == 90:
            self.angle = 88
        if math.ceil(self.angle) == -89:
            self.angle = -88
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
        if self.fire_coordinate != 0:
            for i in range(self.number_fire):  # отрисова пули
                surf.blit(projectile, (self.fire_coordinate[i][0], self.fire_coordinate[i][1]))
        screen.blit(self.rot_center(hand, self.angle), (pl_x - 80, pl_y - 75))

    def take_fire_coordinate(self):
        return self.fire_coordinate


class Fly_Monster:
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
