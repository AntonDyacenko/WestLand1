import pygame

pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
screen.fill(pygame.Color("blue"))
running = True
F = False
rad = 10
x = 0
y = 0
mm = 0
coor = 0, 0
v = 50   # пикселей в секунду
clock = pygame.time.Clock()
clock1 = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            x = event.pos[0]
            y = event.pos[1]
            F = True
            mm += 1
    if F:
        #screen.fill(pygame.Color("blue"))
        pygame.draw.circle(screen, pygame.Color("yellow"), (int(x), int(y)), rad)
        x += v * clock.tick() / 1000  # v * t в секундах
        y -= v * clock1.tick() / 1000  # v * t в секундах
    pygame.display.flip()