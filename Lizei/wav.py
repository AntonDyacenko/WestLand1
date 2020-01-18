import pygame

pygame.mixer.init(frequency=22050, size=-16, channels=4)
sound1 = pygame.mixer.Sound('VV.wav')
sound2 = pygame.mixer.Sound('sound2.wav')
chan1 = pygame.mixer.find_channel()
chan2 = pygame.mixer.find_channel()
chan1.queue(sound1)
chan2.queue(sound2)
time.sleep(10)
