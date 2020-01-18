import pygame
import tkinter as tk
import math

root = tk.Tk()
DISPLAY_SIZE = (root.winfo_screenwidth(), root.winfo_screenheight())

HERO_SPEED = 600 / 1000
JUMP_SPEED = 800 / 1000
FIRE_SPEED = 2
FALL_ACCELERATION = 9.81 * 50 / 1000 / 1000

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

bg0 = pygame.image.load("небо карта2.png")
bg0 = pygame.transform.scale(bg0, (DISPLAY_SIZE[0], int(DISPLAY_SIZE[1] / 1.7)))
bg1 = pygame.image.load("Земля.png")
bg = pygame.image.load("Лучший фон.png")

box = pygame.image.load("Ящик.jpg")


class Object:
    def __init__(self, position, hp):
        self.pos = position
        self.hp = hp

    def get_coords(self):
        return self.pos

    def set_coords(self, coords):
        self.pos = coords

    def get_hp(self):
        return self.hp

    def set_damage(self, damage):
        self.hp -= damage
        if not self.check_alive():
            self.die()

    def check_alive(self):
        return self.hp > 0

    def die(self):
        pass
        # если обьект уничтожили, или персонажа убили


class Box:
    def __init__(self, surf, picture, xp):
        self.surf = surf
        self.picture = picture
        self.xp = xp
        self.pos = 0, 0
        self.weapon = Weapon(1, 1, 1, 1, 1, False)
        self.die = False
        self.terretory = []

    def get_life(self):
        return self.die

    def get_coor(self, pos):
        self.pos = pos

    def draw(self):
        self.surf.blit(self.picture, self.pos)


# это либо герой, либо какой-то злодей
class Character:
    def __init__(self, surf):
        self.hp = 100
        self.surf = surf
        self.A = False
        self.D = False
        self._coords = (0, DISPLAY_SIZE[1] / 4 * 3)
        self._velocity = (0, 0)
        self.J = False

    def set_velocity(self, vel):
        self._velocity = vel

    def get_velocity(self):
        return self._velocity

    def move(self, delta_pos):
        if self.get_position()[1] + delta_pos[1] >= DISPLAY_SIZE[1] / 4 * 3:
            self._coords = (self._coords[0] + delta_pos[0], DISPLAY_SIZE[1] / 4 * 3 - 1)
        else:
            if 0 <= self.get_position()[0] + delta_pos[0] <= 14900:
                self._coords = (self._coords[0] + delta_pos[0],
                                self._coords[1] + delta_pos[1])

    def draw(self):
        if DISPLAY_SIZE[0] / 3 >= self.get_position()[0]:
            self.surf.blit(hero_stand, self.get_position())
        elif self._coords[0] >= 15000 - DISPLAY_SIZE[0] / 3 * 2:
            self.surf.blit(hero_stand, (self.get_position()[0] - 15000 + DISPLAY_SIZE[0], self.get_position()[1]))
        elif self.get_position()[0] >= 15000 - DISPLAY_SIZE[0] * 2 / 3:
            self.surf.blit(hero_go[1], (DISPLAY_SIZE[0] / 3, self.get_position()[1]))
        else:
            self.surf.blit(hero_stand, (DISPLAY_SIZE[0] / 3, self.get_position()[1]))

    def get_position(self):
        return self._coords

    def get_Camera_coor(self):
        if DISPLAY_SIZE[0] / 3 >= self._coords[0]:
            return 0
        elif self._coords[0] >= 15000 - DISPLAY_SIZE[0] / 3 * 2:
            return DISPLAY_SIZE[0] - 15000
        else:
            return DISPLAY_SIZE[0] / 3 - self._coords[0]

    def update(self, dt):
        if self.get_position()[1] < DISPLAY_SIZE[1] / 4 * 3 - 1:
            self._velocity = (self._velocity[0], self._velocity[1] + FALL_ACCELERATION * dt)
        else:
            self._velocity = (0, 0)
        self.move((self._velocity[0] * dt, self._velocity[1] * dt))

    def get_Window_coor(self):
        if DISPLAY_SIZE[0] / 3 >= self._coords[0]:
            return self._coords[0]
        elif self._coords[0] >= 15000 - DISPLAY_SIZE[0] / 3 * 2:
            return DISPLAY_SIZE[0] - (15000 - self._coords[0])
        else:
            return DISPLAY_SIZE[0] / 3


class Weapon:
    def __init__(self, damage, capasity, ammo, coords, at_a_time, owner=False):
        self.damage = damage  # урон от оружия
        self.capasity = capasity  # сколько пуль может быть в магазине
        self.bullets_now = capasity  # сколько пуль в магазине прямо сейчас (изначально максимум, потом при выстреле изменяется)
        self.ammo = ammo  # сколько всего пуль
        self.owner = owner  # у кого это оружие
        self.coords = coords if not self.owner else self.owner.get_coords()  # где находится оружие (если герой не подобрал, то положение на карте, если героц подобрал, то там же где и герой)
        self.at_a_time = at_a_time  # сколько пуль вылетает за один выстрел
        self.angle = 0
        self.number_fire = 0
        self.fire_coordinate = []
        self.character = Character(screen)
        self.x_mouse = 0
        self.y_mouse = 0
        # сюда еще можно вставить определение типа оружия, в зависимости от характеристик

    def fire(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.x_mouse = event.pos[0]
            self.y_mouse = event.pos[1]
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.number_fire += 1
                self.fire_coordinate.append(
                    [character.get_Window_coor() + 40, character.get_position()[1] + 48, self.angle])

    def get_fire_coor(self):
        return self.fire_coordinate

        # if self.bullets_now > self.at_a_time:
        # dam = self.at_a_time * self.damage
        # self.bullets_now -= self.at_a_time
        # else:
        #   dam = self.bullets_now * self.damage
        #  self.bullets_now = 0
        # self.reload()
        # до этого было изменеие количества пуль, дальше уже сам выстрел
        # dam - это сколько оружие снимет за этот выстрел (если оно попало конечно)

    def reload(self):
        needed = self.capasity - self.bullets_now
        if self.ammo > needed:
            self.bullets_now = self.capasity
            self.ammo -= needed
        else:
            self.bullets_now = self.ammo
            self.ammo = 0

    def rot_center(self, image, angle):
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image

    def add_ammo(self, ammo):
        self.ammo += ammo  # если кто-то подбирает пули

    def draw(self, surf):
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
        pl_x = character.get_Window_coor()
        pl_y = character.get_position()[1]
        if self.x_mouse - pl_x - 60 != 0:
            self.angle = math.atan(-(self.y_mouse - pl_y - 50) / (self.x_mouse - pl_x - 60)) * 180 / math.pi
        else:
            self.angle = math.atan(-(self.y_mouse - pl_y - 50) / 1) * 180 / math.pi
        if math.ceil(self.angle) == 90:
            self.angle = 88
        if math.ceil(self.angle) == -89:
            self.angle = -88
        if self.fire_coordinate != 0:
            for i in range(self.number_fire):  # отрисова пули
                surf.blit(projectile, (self.fire_coordinate[i][0] + 10, self.fire_coordinate[i][1]))
        screen.blit(self.rot_center(hand, self.angle), (pl_x - 70, pl_y - 75))


class GameWorld:
    def __init__(self, surf):
        self.surf = surf
        self.character = Character(surf)

    def update(self, pressed_keys, dt):
        if pressed_keys[pygame.K_d]:
            character.move((HERO_SPEED * dt, 0))
        elif pressed_keys[pygame.K_a]:
            character.move((-HERO_SPEED * dt, 0))
        if pressed_keys[pygame.K_SPACE]:
            character.move((0, -JUMP_SPEED * dt))

    def draw(self, dt):
        # self.surf.blit(bg, (character.get_Camera_coor() / 20, 0))
        self.surf.blit(bg1, (character.get_Camera_coor(), 0))


pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

clock = pygame.time.Clock()
character = Character(screen)
game = GameWorld(screen)
clock2 = pygame.time.Clock()
running = True
weapon = Weapon(1, 1, 1, 1, 1, False)
box1 = Box(screen, box, 10)

while running:
    box1.get_coor((character.get_Camera_coor() + 1000, 940))

    dt = clock.tick()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        weapon.fire(event)
    game.update(pygame.key.get_pressed(), dt)
    character.update(dt)

    screen.fill((0, 0, 0))
    game.draw(dt)
    character.draw()
    weapon.draw(screen)
    dt2 = clock2.tick()
    if not box1.get_life():
        box1.draw()

    if dt2 != 0:
        f1 = pygame.font.Font(None, 100)
        text1 = f1.render(str(1000 // dt2), 1, (180, 0, 0), (255, 255, 255))
        screen.blit(text1, (100, 100))
    pygame.display.flip()

pygame.quit()