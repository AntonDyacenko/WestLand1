import pygame

pygame.init()
size = width, height = 201, 201
screen = pygame.display.set_mode(size)
screen.fill(pygame.Color("blue"))
running = True
F = False
rad = 0
coor = 0, 0
v = 10   # пикселей в секунду
clock = pygame.time.Clock()
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            coor = event.pos
            rad = 0
            F = True
    pygame.draw.circle(screen, (255, 255, 255), (100, 100), 10)
    pygame.draw.polygon(screen, (255, 255, 255), [(100, 100), (82, 32), (118, 32)], 0)
    pygame.draw.polygon(screen, (255, 255, 255), [(100, 100), (39, 135), (65, 161)], 0)
    pygame.draw.polygon(screen, (255, 255, 255), [(100, 100), (161, 135), (135, 161)], 0)

    rad += v * clock.tick() / 1000 # v * t в секундах
    pygame.display.flip()