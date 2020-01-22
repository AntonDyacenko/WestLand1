import pygame
import tkinter as tk
import math
import random
import time
import copy

running = True
TIME = time.time()
print(TIME)

root = tk.Tk()
DISPLAY_SIZE = (root.winfo_screenwidth(), root.winfo_screenheight())

HERO_SPEED = 300 / 1000
JUMP_SPEED = 500 / 1000
FIRE_SPEED = 2
PLANT_FIRE_SPEED = 3.5
HERO_HEALTH = 100
FALL_ACCELERATION = 9.81 * 50 / 1000 / 1000

menu_foto = pygame.image.load("Меню.jpg")
menu_foto = pygame.transform.scale(menu_foto, (DISPLAY_SIZE[0], int(DISPLAY_SIZE[1])))
titers_im = pygame.image.load("Титры.jpg")
titers_im = pygame.transform.scale(titers_im, (DISPLAY_SIZE[0], int(DISPLAY_SIZE[1])))
# Загрузка изображений
projectile = pygame.image.load("Снаряд.png")  # Снаряд героя

# ///////////////////////ZOMBIE////////////////////////CHECKED
zombie_go = [pygame.image.load("1_Зомби.png"), pygame.image.load("2_Зомби.png"), pygame.image.load("3_Зомби.png"),
             pygame.image.load("4_Зомби.png"),
             pygame.image.load("5_Зомби.png"), pygame.image.load("6_Зомби.png"), pygame.image.load("7_Зомби.png"),
             pygame.image.load("8_Зомби.png"),
             pygame.image.load("9_Зомби.png"), pygame.image.load("10_Зомби.png"), pygame.image.load("11_Зомби.png")]

zombie_go_2 = [pygame.image.load("1_Зомби2.png"), pygame.image.load("2_Зомби2.png"), pygame.image.load("3_Зомби2.png"),
               pygame.image.load("4_Зомби2.png"),
               pygame.image.load("5_Зомби2.png"), pygame.image.load("6_Зомби2.png"), pygame.image.load("7_Зомби2.png"),
               pygame.image.load("8_Зомби2.png"),
               pygame.image.load("9_Зомби2.png"), pygame.image.load("10_Зомби2.png"),
               pygame.image.load("11_Зомби2.png")]

zombie_stand1 = [pygame.image.load("Зомби_Стоит.png")]

ded_zombie = pygame.image.load("зомби_умер.png")
zombie_stand = pygame.image.load("Зомби_Стоит.png")
zombie = pygame.image.load("1.png")
zombie_die = pygame.image.load("зомби_умер.png")
# ///////////////////////ZOMBIE////////////////////////
# Герой идёт вперёд
hero_go = [pygame.image.load("1.png"), pygame.image.load("2.png"), pygame.image.load("3.png"),
           pygame.image.load("4.png"),
           pygame.image.load("5.png"), pygame.image.load("6.png"), pygame.image.load("7.png"),
           pygame.image.load("8.png"),
           pygame.image.load("9.png"), pygame.image.load("10.png"), pygame.image.load("11.png")]

hero_go_2 = [pygame.image.load("1_1.png"), pygame.image.load("2_1.png"), pygame.image.load("3_1.png"),
           pygame.image.load("4_1.png"),
           pygame.image.load("5_1.png"), pygame.image.load("6_1.png"), pygame.image.load("7_1.png"),
           pygame.image.load("8_1.png"),
           pygame.image.load("9_1.png"), pygame.image.load("10_1.png"), pygame.image.load("11_1.png")]

hero_go_1 = hero_go_2[::-1]

# Герой идёт задом
hero_go1 = [pygame.image.load("11.png"), pygame.image.load("10.png"), pygame.image.load("9.png"),
             pygame.image.load("8.png"), pygame.image.load("7.png"), pygame.image.load("6.png"),
             pygame.image.load("5.png"),
             pygame.image.load("4.png"), pygame.image.load("3.png"), pygame.image.load("2.png"),
             pygame.image.load("1.png")]

# Герой идёт стоит на месте
hero_stand = pygame.image.load("hero_stand.png")
hero_stand_1 = pygame.image.load("hero_stand_1.png")


# Рука с бластером
hand = pygame.image.load("рука.png")
hand_1 = pygame.image.load('рука_1.png')

bg0 = pygame.image.load("небо карта2.png")
bg0 = pygame.transform.scale(bg0, (DISPLAY_SIZE[0], int(DISPLAY_SIZE[1] / 1.7)))
bg1 = pygame.image.load("Земля.gif")
bg1 = pygame.transform.scale(bg1, (15000, DISPLAY_SIZE[1]))
bg = pygame.image.load("Лучший фон.png")

box = pygame.image.load("Ящик.jpg")
kit = pygame.image.load("Аптечка.jpg")
box_die = pygame.image.load("Ящик_сломанный.png")
ammunition_picture = pygame.image.load("Патроны.png")

sprout = pygame.image.load("тело.png")
sprout = pygame.transform.scale(sprout, (150, 300))
head = pygame.image.load("голова_закрыта.png")
head = pygame.transform.scale(head, (200, 200))
head_1 = pygame.image.load("голова_закрыта_1.png")
head_1 = pygame.transform.scale(head_1, (200, 200))
head_fire = pygame.image.load("голова_открыта.png")
head_fire = pygame.transform.scale(head_fire, (200, 200))
head_fire_1 = pygame.image.load("голова_открыта_1.png")
head_fire_1 = pygame.transform.scale(head_fire_1, (200, 200))
dead_plant = pygame.image.load("растение_умерло.png")
dead_dude = pygame.image.load('чувак_умер.png')
dead_plant = pygame.transform.scale(dead_plant, (150, 150))
plant_fire = pygame.image.load('харча.png')

intr = pygame.image.load("Интерфейс.png")
intr_pp = pygame.image.load("Патроны_интерфейс.jpg")

# ///////////////////////////////////////////// ФОНОВЫЙ ЗВУК /////////////////////////////////////////////////
# ///////////////////////////////////////////// ФОНОВЫЙ ЗВУК /////////////////////////////////////////////////
# ///////////////////////////////////////////// ФОНОВЫЙ ЗВУК /////////////////////////////////////////////////
# ///////////////////////////////////////////// ФОНОВЫЙ ЗВУК /////////////////////////////////////////////////
pygame.init()
pygame.mixer.music.load('FON.mp3')
pygame.font.init()
z_position = 1500
rad_attack = 100
z_v = 0.5
p = 0
zflug = False
if running:
    pygame.mixer.music.play()
# ///////////////////////////////////////////// ФОНОВЫЙ ЗВУК /////////////////////////////////////////////////
# ///////////////////////////////////////////// ФОНОВЫЙ ЗВУК /////////////////////////////////////////////////
# ///////////////////////////////////////////// ФОНОВЫЙ ЗВУК /////////////////////////////////////////////////
# ///////////////////////////////////////////// ФОНОВЫЙ ЗВУК /////////////////////////////////////////////////

sound_bullet = pygame.mixer.Sound('richoc.wav')
hit = pygame.mixer.Sound('boxing_hit4.wav')
no_bullet = pygame.mixer.Sound("NO_BULLET.wav")
get_ammunition = pygame.mixer.Sound("OPENCAN.wav")


class Object:
    def __init__(self, position, xp):
        self.pos = position
        self.xp = xp

    def get_coords(self):
        return self.pos

    def set_coords(self, coords):
        self.pos = coords

    def get_xp(self):
        return self.xp

    def set_damage(self, damage):
        self.xp -= damage
        if not self.check_alive():
            self.die()

    def check_alive(self):
        return self.xp > 0

    def die(self):
        pass
        # если обьект уничтожили, или персонажа убили


class Box:
    def __init__(self, surf, xp, type):
        global character
        self.surf = surf
        self.xp = xp
        self.pos = 0, 0
        self.weapon = Weapon(5, 100, 5, character)
        self.die = False
        self.type = type
        self.terretory = []
        self.ammunition = Ammunition(self.surf)
        self.kit = Kit(self.surf)

    def get_coor(self, pos):
        self.pos = pos

    def get_data(self, event):
        self.ammunition.get(event)
        self.kit.get(event)

    def draw(self):
        j = 0
        for i in weapon.get_fire_coor():
            if self.pos[0] <= i[0] <= self.pos[0] + 100 and self.pos[1] <= i[1] <= self.pos[1] + 100:
                hit.play()
                self.die = True
                weapon.hit(j)
            j += 1
        if not self.die:
            self.surf.blit(box, self.pos)
        else:
            if self.type == 1:
                self.ammunition.draw(self.pos)
                self.surf.blit(box_die, self.pos)
            elif self.type == 2:
                self.kit.draw(self.pos)
                self.surf.blit(box_die, self.pos)
            else:
                self.surf.blit(box_die, self.pos)


class Zombie:
    def __init__(self, surf, xp):
        self.surf = surf
        self.xp = xp
        self.j = 0
        self.p = 0
        self.dot = 0
        self.clock = pygame.time.Clock()
        self.pos = 0, 0
        self.die = False
        self.type = type
        self.terretory = []
        self.ammunition = Ammunition(self.surf)
        self.kit = Kit(self.surf)
        self.world_pos = 0, 0
        self.flug = False
        self.zflug = False

    def get_position(self):
        return self.pos

    def get_world_position(self):
        return self.world_pos

    def set_world_position(self, world_pos):
        self.world_pos = world_pos

    def set_position(self, pos):
        self.pos = pos

    def get_data(self, event):
        self.ammunition.get(event)
        self.kit.get(event)

    def check_dead(self):
        if self.xp > 0:
            return False
        else:
            return True

    def update(self, player_pos, dt):
        if not self.die:
            if abs(player_pos[0] - zombie.get_world_position()[0]) > rad_attack:
                if zombie.get_world_position()[0] >= player_pos[0]:
                    dp = (player_pos[0] - zombie.get_world_position()[0]) / abs(
                        player_pos[0] - zombie.get_world_position()[0]) * z_v * dt
                    zombie.set_world_position((zombie.get_world_position()[0] + dp, zombie.get_world_position()[1]))
                    print(dp)
                    self.flug = False
                elif zombie.get_world_position()[0] < player_pos[0]:
                    dp = (player_pos[0] - zombie.get_world_position()[0]) / abs(
                        player_pos[0] - zombie.get_world_position()[0]) * z_v * dt
                    zombie.set_world_position((zombie.get_world_position()[0] + dp, zombie.get_world_position()[1]))
                    self.flug = True
                self.zflug = False
            else:
                character.set_xp(-1)
                self.zflug = True
            self.h = character.get_xp()
            if self.h == 0:  # пытаемся убить героя
                global screen
                rect = pygame.Rect(0, 0, root.winfo_screenwidth(), root.winfo_screenheight())
                pygame.draw.rect(self.surf, (0, 0, 0), rect)  # пытаемся закрасить
                character.die()   # второй вариант из кода

    def draw(self):
        j = 0
        self.dot += self.clock.tick()
        if self.dot >= 70:
            self.j += 1
            self.p += 1
            self.dot = 0
        if self.j > 10:
            self.j = 0
        if self.p > 10:
            self.p = 0
        # self.pos[0] -= 10
        for i in weapon.get_fire_coor():
            if self.pos[0] <= i[0] <= self.pos[0] + 100 and self.pos[1] <= i[1] <= self.pos[1] + 100:
                hit.play()
                self.die = True
                weapon.hit(j)
            j += 1

        if not self.die:
            if self.zflug == False:
                if self.flug == False:
                    self.surf.blit(zombie_go[self.p], self.pos)
                else:
                    self.surf.blit(zombie_go_2[self.p], self.pos)
            else:
                self.surf.blit(zombie_stand1[0], self.pos)
        else:
            self.surf.blit(ded_zombie, (self.pos[0], self.pos[1] + 110))


class Kit:
    def __init__(self, surf):
        self.take = False
        self.surf = surf
        self.pos = (0, 0)
        self.surf = surf

    def get(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                if self.pos[0] - 50 <= character.get_position()[0] + character.get_Camera_coor() <= self.pos[
                    0] + 50 and self.pos != (0, 0):
                    get_ammunition.play()
                    character.set_xp(25)
                    self.take = True

    def draw(self, pos):
        self.pos = pos
        if not self.take:
            self.surf.blit(kit, (pos[0] + 25, pos[1] + 25))


class Ammunition:
    def __init__(self, surf):
        self.take = False
        self.surf = surf
        self.weapon = Weapon
        self.pos = (0, 0)

    def get(self, event):
        if not self.take:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    if self.pos[0] - 50 <= character.get_position()[0] + character.get_Camera_coor() <= self.pos[
                        0] + 50 and self.pos != (0, 0):
                        get_ammunition.play()
                        weapon.add_ammo(30)
                        self.take = True

    def draw(self, pos):
        self.pos = pos
        if not self.take:
            self.surf.blit(ammunition_picture, (pos[0] + 25, pos[1] + 25))


# это либо герой, либо какой-то злодей
class Character:
    def __init__(self, surf):
        self.xp = HERO_HEALTH
        self.Moment = 0
        self.surf = surf
        self.A = False
        self.D = False
        self._coords = (0, DISPLAY_SIZE[1] / 4 * 3)
        self._velocity = (0, 0)
        self._is_falling = False
        self.i = 0
        self.clock = pygame.time.Clock()
        self.flag = False

    def set_xp(self, xp0):
        if self.xp + xp0 >= HERO_HEALTH:
            self.xp = HERO_HEALTH
        else:
            self.xp += xp0

    def die(self):
        global running
        global flag
        font = pygame.font.SysFont("comicsansms", 30)
        text = font.render(f'You died. Сорян', True, (255, 0, 0))
        self.surf.blit(text, (10, 400))
        weapon.set_flag()
        flag = True

    def set_flags(self):
        self.flag = True

    def set_flag(self, num):
        if num == 1:
            self.A = True
            self.D = False
        elif num == 2:
            self.A = False
            self.D = True
        else:
            self.A = False
            self.D = False

    def get_xp(self):
        return self.xp

    def set_velocity(self, vel):
        self._velocity = vel

    def get_velocity(self):
        return self._velocity

    def jump(self):
        if not self._is_falling:
            character.move((0, -1))
            self._velocity = self._velocity[0], self._velocity[1] - JUMP_SPEED
            character.set_flag(0)
            self._is_falling = True

    def move(self, delta_pos):
        if self.get_position()[1] + delta_pos[1] >= DISPLAY_SIZE[1] / 4 * 3:
            self._coords = (self._coords[0] + delta_pos[0], DISPLAY_SIZE[1] / 4 * 3 - 1)
        else:
            if 0 <= self.get_position()[0] + delta_pos[0] <= 14900:
                self._coords = (self._coords[0] + delta_pos[0],
                                self._coords[1] + delta_pos[1])

    def draw(self, fl):
        if not self.flag:
            if fl:
                Hero = hero_stand
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
                        Hero = hero_go1[self.i]
                if DISPLAY_SIZE[0] / 3 >= self.get_position()[0]:
                    self.surf.blit(Hero, self.get_position())
                elif self._coords[0] >= 15000 - DISPLAY_SIZE[0] / 3 * 2:
                    self.surf.blit(Hero, (self.get_position()[0] - 15000 + DISPLAY_SIZE[0], self.get_position()[1]))
                elif self.get_position()[0] >= 15000 - DISPLAY_SIZE[0] * 2 / 3:
                    self.surf.blit(Hero, (DISPLAY_SIZE[0] / 3, self.get_position()[1]))
                else:
                    self.surf.blit(Hero, (DISPLAY_SIZE[0] / 3, self.get_position()[1]))
            else:
                Hero = hero_stand_1
                if not self.D and not self.A:
                    Hero = hero_stand_1
                else:
                    self.Moment += self.clock.tick()
                    if self.Moment >= 70:
                        self.i += 1
                        self.Moment = 0
                    if self.i > 10:
                        self.i = 0
                    if self.D:
                        Hero = hero_go_1[self.i]
                    elif self.A:
                        Hero = hero_go_2[self.i]
                if DISPLAY_SIZE[0] / 3 >= self.get_position()[0]:
                    self.surf.blit(Hero, self.get_position())
                elif self._coords[0] >= 15000 - DISPLAY_SIZE[0] / 3 * 2:
                    self.surf.blit(Hero, (self.get_position()[0] - 15000 + DISPLAY_SIZE[0], self.get_position()[1]))
                elif self.get_position()[0] >= 15000 - DISPLAY_SIZE[0] * 2 / 3:
                    self.surf.blit(Hero, (DISPLAY_SIZE[0] / 3, self.get_position()[1]))
                else:
                    self.surf.blit(Hero, (DISPLAY_SIZE[0] / 3, self.get_position()[1]))
        else:
            self.surf.blit(dead_dude, (self.get_Window_coor(), self.get_position()[1] + 100))
            self.die()

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
            self._is_falling = False
            self._velocity = (self._velocity[0], 0)
        self.move((self._velocity[0] * dt, self._velocity[1] * dt))

    def get_Window_coor(self):
        if DISPLAY_SIZE[0] / 3 >= self._coords[0]:
            return self._coords[0]
        elif self._coords[0] >= 15000 - DISPLAY_SIZE[0] / 3 * 2:
            return DISPLAY_SIZE[0] - (15000 - self._coords[0])
        else:
            return DISPLAY_SIZE[0] / 3


class Plant:
    def __init__(self, pos, surf):
        self.pos = pos
        self.const = pos
        self.surf = surf
        self.dam = 25
        self.t = False
        self.x = 0
        self.y = 0
        self.counter = 0
        self.coord = []
        self.p = False
        self.hp = 100

    def fire(self, coords):
        self.t = True
        self.x = coords[0]
        self.y = coords[1]

    def check(self, coords, i):
        if self.hp > 0:
            self.coords = coords
            self.draw()
            if abs(self.const[0] - coords[0]) < 1000:
                self.fire(coords)
                self.t = True
            fire = weapon.get_fire_coor()
            j = 0
            for i in fire:
                x = self.get_pos()[0]
                y = self.get_pos()[1]
                x1 = i[0]
                y1 = i[1]
                if x < x1 < x + 100 and y - 50 < y1 < y + 250:
                    self.get_dam(weapon.damage)
                    weapon.hit(j)
        else:
            self.coords = coords
            self.draw()

    def get_dam(self, dam):
        self.hp -= dam

    def get_pos(self):
        return self.pos

    def check_dead(self):
        if self.hp > 0:
            return False
        else:
            return True

    def draw(self):
        if self.hp > 0:
            self.surf.blit(sprout, self.get_pos())

            y2 = round(self.coords[1]) - 50
            x2 = round(self.coords[0]) - 10
            y1 = self.const[1] + 709
            x1 = self.const[0]
            f = x2 - x1

            if f == 0:
                angle = math.pi / 2
            else:
                angle = math.atan((y2 - y1) / (x2 - x1))
                angle = math.degrees(-angle)
            if self.counter == 0:
                self.angle = angle
                self.f = f

            if not self.t:
                self.surf.blit(self.rot_center(head, angle), (self.get_pos()[0], self.get_pos()[1] - 95))
                self.counter = 0
            if self.t:
                self.counter += 1
                if f < 0:
                    self.surf.blit(self.rot_center(head_fire, angle), (self.get_pos()[0], self.get_pos()[1] - 95))
                else:
                    self.surf.blit(self.rot_center(head_fire_1, angle), (self.get_pos()[0], self.get_pos()[1] - 95))

                # дальше выстрел
                self.counter += 1
                if self.counter % 370 != 0:
                    if self.f < 0:
                        x = self.pos[0]
                        y = self.pos[1]
                        x += PLANT_FIRE_SPEED * math.sin(
                            (self.angle + 90 + 180 + 5) * math.pi / 180) * self.counter
                        y += PLANT_FIRE_SPEED * math.cos(
                            (
                                    self.angle + 90 + 180 + 5) * math.pi / 180) * self.counter + 50 if self.counter != 1 else PLANT_FIRE_SPEED * math.cos(
                            (self.angle + 90 + 180 + 5) * math.pi / 180) * self.counter
                        self.surf.blit(plant_fire, (x, y))
                    else:
                        x = self.pos[0] + 100
                        y = self.pos[1] + 20
                        x -= PLANT_FIRE_SPEED * math.sin(
                            (self.angle + 90 + 180 - 5) * math.pi / 180) * self.counter
                        y -= PLANT_FIRE_SPEED * math.cos(
                            (self.angle + 90 + 180 - 5) * math.pi / 180) * self.counter
                        self.surf.blit(plant_fire, (x, y))
                    y_char = round(character.get_position()[1])
                    x_char = character.get_Window_coor()
                    if x_char < x < x_char + 50 and y_char < y < y_char + 200 and not self.p:
                        character.set_xp(-self.dam)
                        if character.get_xp() <= 0:
                            character.set_flags()
                        self.counter = 0
                else:
                    self.counter = 0
                    self.p = False
        else:
            self.surf.blit(dead_plant, (self.get_pos()[0], self.get_pos()[1] + 170))

    def get_coor(self, pos):
        self.pos = pos

    def get_fire_coord(self):
        return self.coord

    def rot_center(self, image, angle):
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image


class Weapon:
    def __init__(self, dam, ammo, now, owner):
        self.damage = dam  # 5
        self.capasity = now  # 5
        self.bullets_now = now  # 5
        self.ammo = ammo  # 100  # сколько всего пуль
        self.at_a_time = 0  # сколько пуль вылетает за один выстрел
        self.angle = 0
        self.number_fire = 0
        self.fire_coordinate = []
        self.character = owner  # Character(screen)
        self.x_mouse = 0
        self.y_mouse = 0
        self.ammunition = Ammunition(screen)
        self.flag = False
        # сюда еще можно вставить определение типа оружия, в зависимости от характеристик

    def get_number_fire(self):
        return self.ammo

    def hit(self, number):
        self.number_fire -= 1
        del self.fire_coordinate[number]

    def fire(self, event, coords=False):
        if event.type == pygame.MOUSEMOTION:
            self.x_mouse = event.pos[0]
            self.y_mouse = event.pos[1]
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.ammo != 0:
                    sound_bullet.play()
                    self.ammo -= 1
                    self.number_fire += 1
                    self.fire_coordinate.append(
                        [character.get_Window_coor() + 40, character.get_position()[1] + 48, self.angle, self.f])
                else:
                    no_bullet.play()

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

    def set_flag(self):
        self.flag = True

    def draw(self, surf):
        i = 0
        pl_x = character.get_Window_coor()
        pl_y = character.get_position()[1]
        self.f = self.x_mouse - pl_x
        while i != self.number_fire:
            if self.fire_coordinate[i][0] <= 1.4 * DISPLAY_SIZE[0]:
                if self.fire_coordinate[i][3] < 0:
                    self.fire_coordinate[i][0] += (FIRE_SPEED * dt * math.sin(
                        (self.fire_coordinate[i][2] - 90) * math.pi / 180))
                    self.fire_coordinate[i][1] += (FIRE_SPEED * dt * math.cos(
                        (self.fire_coordinate[i][2] - 90) * math.pi / 180))
                else:
                    self.fire_coordinate[i][0] += (FIRE_SPEED * dt * math.sin(
                        (self.fire_coordinate[i][2] + 90) * math.pi / 180))
                    self.fire_coordinate[i][1] += (FIRE_SPEED * dt * math.cos(
                        (self.fire_coordinate[i][2] + 90) * math.pi / 180))
                i += 1
            else:
                self.number_fire -= 1
                del self.fire_coordinate[i]
        if self.x_mouse != pl_x:
            self.angle = math.atan(-(self.y_mouse - pl_y - 75) / (self.x_mouse - pl_x))
            self.angle = math.degrees(self.angle)
        else:
            self.angle = 90
        if math.ceil(self.angle) == 90:
            self.angle = 88
        if math.ceil(self.angle) == -89:
            self.angle = -88
        if self.fire_coordinate != 0:
            for i in range(self.number_fire):  # отрисова пули
                surf.blit(projectile, (self.fire_coordinate[i][0] + 10, self.fire_coordinate[i][1]))
        if not self.flag:
            if self.f > 0:
                screen.blit(self.rot_center(hand, self.angle), (pl_x - 70, pl_y - 75))
            if self.f < 0:
                screen.blit(self.rot_center(hand_1, self.angle), (pl_x - 46, pl_y - 75))





class GameWorld:
    def __init__(self, surf):
        self.surf = surf
        self.character = Character(surf)
        self.ammunition = Ammunition(screen)
        self.menu = False

    def update(self, pressed_keys, dt):  # ОБРАБОТКА ВСЕХ НАЖАТИЙ НА КЛАВИШИ
        vel = character.get_velocity()
        if pressed_keys[pygame.K_d]:
            # character.move((HERO_SPEED * dt, 0))
            character.set_velocity((HERO_SPEED, vel[1]))
            character.set_flag(2)
        elif pressed_keys[pygame.K_a]:
            # character.move((-HERO_SPEED * dt, 0))
            character.set_velocity((-HERO_SPEED, vel[1]))
            character.set_flag(1)
        else:
            character.set_velocity((0, vel[1]))
            character.set_flag(0)
        if pressed_keys[pygame.K_SPACE]:
            character.jump()
        character.update(dt)

    def draw(self):
        self.surf.blit(bg1, (character.get_Camera_coor(), 0))  # РИСУЕТ

    def get_menu(self):
        return self.menu

    def set_menue(self):
        if not self.menu:
            self.menu = True
        else:
            self.menu = False


class Interface:
    def __init__(self, surf):
        self.surf = surf
        self.character = Character(surf)
        self.dt = 0
        self.max_ = 0
        self.min_ = 10000

    def set_dt(self, dt):  # ДОБАВЛЯЕТ ВРЕМЯ
        self.dt = dt

    def draw(self):
        # //////////////////////////////// ОТОБРАЖЕНИЕ FPS ////////////////////////////////////
        if self.dt != 0:
            f1 = pygame.font.Font(None, 50)
            f2 = pygame.font.Font(None, 25)
            f3 = pygame.font.Font(None, 25)
            if 1000 // dt2 > self.max_:
                self.max_ = 1000 // dt2
            if self.min_ > 1000 // dt2:
                self.min_ = 1000 // dt2
            text1 = f1.render(("FPS: " + str(1000 // dt2)), 1, (255, 255, 255))
            text2 = f2.render(("FPS max: " + str(self.max_)), 1, (255, 255, 255))
            text3 = f3.render(("FPS min: " + str(self.min_)), 1, (255, 255, 255))
            screen.blit(text1, (10, 10))
            screen.blit(text2, (10, 70))
            screen.blit(text3, (10, 105))
        # //////////////////////////////// ОТОБРАЖЕНИЕ XP ////////////////////////////////////
        if character.get_xp() <= HERO_HEALTH / 4:
            pygame.draw.rect(self.surf, (255, 0, 0), (DISPLAY_SIZE[0] - 395 - 20, 20, 82, 62), 0)
        elif character.get_xp() <= HERO_HEALTH / 2:
            pygame.draw.rect(self.surf, (255, 255, 0), (DISPLAY_SIZE[0] - 395 - 20, 20, 164, 62), 0)
        elif character.get_xp() <= HERO_HEALTH / 4 * 3:
            pygame.draw.rect(self.surf, (173, 255, 47), (DISPLAY_SIZE[0] - 395 - 20, 20, 246, 62), 0)
        else:
            pygame.draw.rect(self.surf, (0, 255, 0), (DISPLAY_SIZE[0] - 395 - 20, 20, 326, 62), 0)
        self.surf.blit(intr, (DISPLAY_SIZE[0] - 395 - 20, 20))
        # //////////////////////////////// ОТОБРАЖЕНИЕ ЗАРЯДОВ ////////////////////////////////////
        self.surf.blit(intr_pp, (DISPLAY_SIZE[0] - 80, 102))
        f4 = pygame.font.Font(None, 100)
        text4 = f4.render(str(weapon.get_number_fire()), 1, (255, 255, 255))
        screen.blit(text4, (DISPLAY_SIZE[0] - 220, 102))

    def dead(self):
        global screen
        rect = pygame.Rect(0, 0, root.winfo_screenwidth(), root.winfo_screenheight())
        pygame.draw.rect(self.surf, (0, 0, 0), rect)


# ТУТ НАЧИНАЕТСЯ ВСЕ ЧТО ПРОИСХОДИТ ПРИ ВЫИГРЫШЕ
width = DISPLAY_SIZE[0]
height = DISPLAY_SIZE[1]
screen_rect = (0, 0, width, height)
GRAVITY = 2


class Particle(pygame.sprite.Sprite):
    # сгенерируем частицы разного размера
    star = pygame.image.load("star.png")
    star = pygame.transform.scale(star, (50, 50))
    fire = [star]
    for scale in (5, 10, 20):
        fire.append(pygame.transform.scale(fire[0], (scale, scale)))

    def __init__(self, pos, dx, dy):
        super().__init__(all_sprites)
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()

        # у каждой частицы своя скорость — это вектор
        self.velocity = [dx, dy]
        # и свои координаты
        self.rect.x, self.rect.y = pos

        # гравитация будет одинаковой (значение константы)
        self.gravity = GRAVITY

    def update(self):
        # применяем гравитационный эффект:
        # движение с ускорением под действием гравитации
        self.velocity[1] += self.gravity
        # перемещаем частицу
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        # убиваем, если частица ушла за экран
        if not self.rect.colliderect(screen_rect):
            self.kill()


class Menu:
    def __init__(self, surf):
        self.surf = surf
        self.event = None
        self.esc = False
        self.esc_x1 = 1
        self.esc_y1 = 1
        self.esc_x2 = 2
        self.esc_y2 = 2
        self.esc_x3 = 1
        self.esc_y3 = 1
        self.esc_x4 = 2
        self.esc_y4 = 2
        self.light = False
        self.light2 = False

    def set_event(self, event):
        self.event = event

    def prog(self):
        if event.type == pygame.MOUSEMOTION:
            if self.esc_x1 <= event.pos[0] <= self.esc_x2 and self.esc_y1 <= event.pos[1] <= self.esc_y2:
                self.light = True
            else:
                self.light = False
            if self.esc_x3 <= event.pos[0] <= self.esc_x4 and self.esc_y3 <= event.pos[1] <= self.esc_y4:
                self.light2 = True
            else:
                self.light2 = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.esc_x1 <= event.pos[0] <= self.esc_x2 and self.esc_y1 <= event.pos[1] <= self.esc_y2:
                self.set_esc()
            if self.esc_x3 <= event.pos[0] <= self.esc_x4 and self.esc_y3 <= event.pos[1] <= self.esc_y4:
                game.set_menue()

    def set_esc(self):
        if self.esc:
            self.esc = False
        else:
            self.esc = True

    def get_esc(self):
        return self.esc

    def draw(self):
        # //////////////////////////////// КНОПКА ВЫХОДА ИЗ ИГРЫ ////////////////////////////////////
        self.surf.blit(menu_foto, (0, 0))
        font = pygame.font.Font(None, 200)
        text = font.render("Выход из игры", 1, (255, 0, 0))
        text_x = DISPLAY_SIZE[0] // 2 - text.get_width() // 2
        text_y = DISPLAY_SIZE[1] // 2 - text.get_height() // 2
        text_w = text.get_width()
        text_h = text.get_height()
        self.esc_x1 = text_x - 10
        self.esc_y1 = text_y - 10
        self.esc_x2 = text_x - 10 + text_w + 20
        self.esc_y2 = text_h + 20 + text_y - 10
        if not self.light:
            pygame.draw.rect(self.surf, (255, 0, 0), (text_x - 10, text_y - 10,
                                                      text_w + 20, text_h + 20), 1)
        else:
            pygame.draw.rect(self.surf, (100, 0, 0), (text_x - 10, text_y - 10,
                                                      text_w + 20, text_h + 20))
        self.surf.blit(text, (text_x, text_y))
        # //////////////////////////////// ВРЕМЯ В МЕНЮ ////////////////////////////////////
        timee = time.time() + 75600
        front2 = pygame.font.Font(None, 200)
        text2 = front2.render(str('Время в игре: ' + str(time.ctime(timee - TIME))[11: 19]), 1, (255, 0, 0))
        text_x2 = DISPLAY_SIZE[0] // 2 - text2.get_width() // 2
        text_y2 = DISPLAY_SIZE[1] // 4 - text2.get_height() // 2
        self.surf.blit(text2, (text_x2, text_y2))
        # //////////////////////////////// КНОПКА ВЫХОДА ИЗ МЕНЮ ////////////////////////////////////
        font3 = pygame.font.Font(None, 200)
        text3 = font3.render("Выход из меню", 1, (255, 0, 0))
        text_x3 = DISPLAY_SIZE[0] // 2 - text3.get_width() // 2
        text_y3 = DISPLAY_SIZE[1] // 4 * 3 - text3.get_height() // 2
        text_w3 = text3.get_width()
        text_h3 = text3.get_height()
        self.esc_x3 = text_x3 - 10
        self.esc_y3 = text_y3 - 10
        self.esc_x4 = text_x3 - 10 + text_w3 + 20
        self.esc_y4 = text_h3 + 20 + text_y3 - 10
        if not self.light2:
            pygame.draw.rect(self.surf, (255, 0, 0), (text_x3 - 10, text_y3 - 10,
                                                      text_w3 + 20, text_h3 + 20), 1)
        else:
            pygame.draw.rect(self.surf, (100, 0, 0), (text_x3 - 10, text_y3 - 10,
                                                      text_w3 + 20, text_h3 + 20))
        self.surf.blit(text3, (text_x3, text_y3))

    # //////////////////////////////// КЛАССЫ ////////////////////////////////////


class Titers:
    def __init__(self, surf):
        self.surf = surf
        self.flag = True
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.pos = DISPLAY_SIZE[1]

    def set_dt(self, dt):
        self.dt = dt

    def get_flag(self):
        if time.time() - TIME <= 10:
            self.flag = True
        else:
            self.flag = False
        return self.flag

    def move(self, dt):
        self.pos -= dt / 100
        return self.pos

    def draw(self):
        self.surf.blit(titers_im, (0, 0))
        pygame.font.init()
        front1 = pygame.font.Font(None, 75)
        front2 = pygame.font.Font(None, 75)
        front3 = pygame.font.Font(None, 75)
        front4 = pygame.font.Font(None, 75)
        front5 = pygame.font.Font(None, 75)
        front6 = pygame.font.Font(None, 75)
        front7 = pygame.font.Font(None, 75)
        front8 = pygame.font.Font(None, 75)
        text1 = front1.render('После глобальной войны люди покинули землю,', 1, (255, 0, 0))
        text2 = front2.render('оставив вызженную пустыню, населённую лишь жуткими мутантами.', 1, (255, 0, 0))
        text3 = front3.render('Но некоторые смельчаки возвращаются на свою родную планету.', 1, (255, 0, 0))
        text4 = front4.render('Корабль одного из них потерпел крушение,', 1, (255, 0, 0))
        text5 = front5.render('и Ваша цель - помочь ему добраться до спасательного пункта', 1, (255, 0, 0))
        text6 = front6.render('и вызвать помощь.', 1, (255, 0, 0))
        text7 = front7.render('Враждебное население Новой Земли будет мешать Вам.', 1, (255, 0, 0))
        text8 = front8.render('Убейте всех врагов и спасите Героя.', 1, (255, 0, 0))
        text_x1 = DISPLAY_SIZE[0] // 2 - text1.get_width() // 2
        text_y1 = self.move(self.dt)
        text_x2 = DISPLAY_SIZE[0] // 2 - text2.get_width() // 2
        text_y2 = self.move(self.dt) + 75
        text_x3 = DISPLAY_SIZE[0] // 2 - text3.get_width() // 2
        text_y3 = self.move(self.dt) + 150
        text_x4 = DISPLAY_SIZE[0] // 2 - text4.get_width() // 2
        text_y4 = self.move(self.dt) + 225
        text_x5 = DISPLAY_SIZE[0] // 2 - text5.get_width() // 2
        text_y5 = self.move(self.dt) + 300
        text_x6 = DISPLAY_SIZE[0] // 2 - text6.get_width() // 2
        text_y6 = self.move(self.dt) + 375
        text_x7 = DISPLAY_SIZE[0] // 2 - text7.get_width() // 2
        text_y7 = self.move(self.dt) + 450
        text_x8 = DISPLAY_SIZE[0] // 2 - text8.get_width() // 2
        text_y8 = self.move(self.dt) + 525
        self.surf.blit(text1, (text_x1, text_y1))
        self.surf.blit(text2, (text_x2, text_y2))
        self.surf.blit(text3, (text_x3, text_y3))
        self.surf.blit(text4, (text_x4, text_y4))
        self.surf.blit(text5, (text_x5, text_y5))
        self.surf.blit(text6, (text_x6, text_y6))
        self.surf.blit(text7, (text_x7, text_y7))
        self.surf.blit(text8, (text_x8, text_y8))


def create_particles(position):
    # количество создаваемых частиц
    particle_count = 20
    # возможные скорости
    numbers = range(-5, 6)
    for _ in range(particle_count):
        Particle(position, random.choice(numbers), random.choice(numbers))


# ТУТ ЗАКАНЧИВАЕТСЯ ВСЕ ЧТО ПРОИСХОДИТ ПРИ ВЫИГРЫШЕ

# //////////////////////////////// КЛАССЫ ////////////////////////////////////
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
character = Character(screen)
interface = Interface(screen)
game = GameWorld(screen)
weapon = Weapon(5, 100, 5, character)
start = 800
plant_lst = []
for i in range(5):
    plant_lst.append(Plant([start + 2400 * i, 0], screen))

all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()
running = True

# //////////////////////////////// РАЗНОЕ ////////////////////////////////////
pygame.init()
menu = Menu(screen)
box1 = Box(screen, 10, 1)
box2 = Box(screen, 10, 2)
box3 = Box(screen, 10, 0)
box4 = Box(screen, 10, 1)
box5 = Box(screen, 10, 2)
box6 = Box(screen, 10, 0)
box7 = Box(screen, 10, 1)
box8 = Box(screen, 10, 2)
box9 = Box(screen, 10, 0)
# ///////////////////////ZOMBIE////////////////////////CHECKED
zombie = Zombie(screen, 20)
character = Character(screen)
zombie.set_world_position((8000, character.get_position()[1]))
zombie_die = Zombie(screen, 20)
# ///////////////////////ZOMBIE////////////////////////
# //////////////////////////////// ЧАСЫ ////////////////////////////////////
clock = pygame.time.Clock()
clock2 = pygame.time.Clock()
clock3 = pygame.time.Clock()
clock5 = pygame.time.Clock()
titers = Titers(screen)
flag = False
# //////////////////////////////// ОСНОВНОЙ ЦИКЛ ////////////////////////////////////
i = 1
win = False
D = True
# while D:
#     while running:
#         print(11111)
#         if time.time() - TIME >= 3:
#             print(222)
#             D = False
#         for event in pygame.event.get():
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_ESCAPE:
#                     running = False
#         dt5 = clock5.tick()
#         titers.set_dt(dt5)
#         titers.draw()
#         pygame.display.flip()
dt = clock.tick()
dt2 = clock2.tick()
while running:
    if titers.get_flag():
        dt = clock.tick()
        dt5 = clock5.tick()
        titers.set_dt(dt5)
        titers.draw()
    elif not game.get_menu():
        if not flag:

            # //////////////////////////////// ИГРОВЫЕ ОБЪЕКТЫ ////////////////////////////////////
            #// // // // // // // // // // // / ZOMBIE // // // // // // // // // // // //
            print(dt)
            zombie.update(character.get_position(), dt)
            zombie.set_position(
                (character.get_Camera_coor() + zombie.get_world_position()[0], zombie.get_world_position()[1]))
            #// // // // // // // // // // // / ZOMBIE // // // // // // // // // // // //
            box1.get_coor((character.get_Camera_coor() + 1000, 940))
            box2.get_coor((character.get_Camera_coor() + 2000, 940))
            box3.get_coor((character.get_Camera_coor() + 3000, 940))
            box4.get_coor((character.get_Camera_coor() + 4000, 940))
            box5.get_coor((character.get_Camera_coor() + 5000, 940))
            box6.get_coor((character.get_Camera_coor() + 6000, 940))
            box7.get_coor((character.get_Camera_coor() + 7000, 940))
            box8.get_coor((character.get_Camera_coor() + 9000, 940))
            box9.get_coor((character.get_Camera_coor() + 10000, 940))

            for i in range(len(plant_lst)):
                plant_lst[i].get_coor((character.get_Camera_coor() + start + 2400 * i, root.winfo_screenheight() - 360))
            # //////////////////////////////// ЧАСЫ ////////////////////////////////////
            dt = clock.tick()
            dt2 = clock2.tick()
            # //////////////////////////////// ОБРАБОТКА СОБЫТИЙ ////////////////////////////////////
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game.set_menue()
                if event.type == pygame.MOUSEMOTION:
                    x = event.pos[0]
                    if x >= character.get_Window_coor():
                        fl = True
                    else:
                        fl = False
                box1.get_data(event)
                box2.get_data(event)
                box3.get_data(event)
                box4.get_data(event)
                box5.get_data(event)
                box6.get_data(event)
                box7.get_data(event)
                box8.get_data(event)
                box9.get_data(event)
                zombie.get_data(event)
                weapon.fire(event)
            game.update(pygame.key.get_pressed(), dt)
            character.update(dt)
            # //////////////////////////////// ЗАЛИВКА ЭКРАНА ////////////////////////////////////
            screen.fill((0, 0, 0))
            # //////////////////////////////// ФУНКЦИИ КЛАССОВ ////////////////////////////////////
            interface.set_dt(dt2)
            # //////////////////////////////// ФУНКЦИИ РИСОВАНИЯ ////////////////////////////////////
            game.draw()
            # //////////////////////////////// ОТРИСОВКА КОРОБОК ////////////////////////////////////
            box1.draw()
            box2.draw()
            box3.draw()
            box4.draw()
            box5.draw()
            box6.draw()
            box7.draw()
            box8.draw()
            box9.draw()
            zombie.draw()
            for j in range(len(plant_lst)):
                plant_lst[j].check(character.get_position(), i)
            lst = []
            for j in plant_lst:
                lst.append(j.check_dead())
            if all(lst):
                win = True
                running = False
            character.draw(fl)
            weapon.draw(screen)
            # //////////////////////////////////////////////////////////////////////////////////////
            interface.draw()
            # //////////////////////////////// РАЗНОЕ ////////////////////////////////////
            pygame.display.flip()
            i += 1
        else:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            interface.dead()
            pygame.display.flip()
    else:
        menu.prog()
        dt = clock.tick()
        if menu.get_esc():
            running = False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game.set_menue()
            menu.set_event(event)
        screen.fill((0, 0, 0))
        menu.draw()
    pygame.display.flip()
    # КОГДА ВЫИГРВАЕШЬ, ПРОИСХОДИТ ВОТ ЭТО
if win:
    all_sprites = pygame.sprite.Group()
    clock = pygame.time.Clock()
    running = True
    i = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        if i % 5 == 0:
            create_particles((DISPLAY_SIZE[0] // 4, DISPLAY_SIZE[1] // 2))
            create_particles((DISPLAY_SIZE[0] // 4 * 3, DISPLAY_SIZE[1] // 2))
            create_particles((DISPLAY_SIZE[0] // 6, DISPLAY_SIZE[1] // 3))
            create_particles((DISPLAY_SIZE[0] // 6 * 5, DISPLAY_SIZE[1] // 3))

        all_sprites.update()
        screen.fill((0, 0, 0))
        myfont = pygame.font.Font(None, 100)
        width = DISPLAY_SIZE[0]
        height = DISPLAY_SIZE[1]
        text = myfont.render("You won!", 1, (100, 255, 100))
        text_x = width // 2 - text.get_width() // 2
        text_y = height // 2 - text.get_height() // 2
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y))
        pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 10,
                                               text_w + 20, text_h + 20), 1)
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(50)
        i += 1
pygame.quit()