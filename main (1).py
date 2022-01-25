import pygame
from pygame.draw import *

pygame.init()
FPS = 30
screen = pygame.display.set_mode((670, 940))
surface = pygame.Surface((670, 940), pygame.SRCALPHA)

rect(screen, (200, 200, 200), (0, 0, 670, 600))
rect(screen, (47, 79, 79), (0, 600, 670, 940))

line(screen, (255, 255, 255), (0, 600),(670, 600), 5)

rect(screen, (240, 240, 240, ), (520, 15, 140, 600))
pygame.draw.ellipse(surface, (220, 255, 220, 100), (300, -20, 600, 150))
rect(screen, (141, 238, 238, ), (440, 160, 140, 570))
rect(screen, (105, 105, 105, ), (15, 15, 140, 600))
rect(screen, (105, 139, 105, ), (180, 50, 140, 600))
rect(screen, (150, 150, 150), (100, 100, 140, 600))

ellipse(screen, (150, 150, 150), (-50, 750, 1000, 400))

ellipse(screen, (0, 0, 128), (210, 830, 65, 10))
rect(screen, (0, 191, 255, ), (230, 800, 280, 55))
rect(screen, (0, 191, 255, ), (290, 765, 130, 40))
ellipse(screen, (0, 0, 128), (250, 830, 65, 45))
ellipse(screen, (0, 0, 128), (430, 830, 65, 45))
rect(screen, (240, 240, 255, ), (300, 770, 50, 30))
rect(screen, (240, 240, 255, ), (360, 770, 50, 30))
pygame.draw.ellipse(surface, (220, 255, 220, 100), (50, 790, 150, 55))
pygame.draw.ellipse(surface, (220, 255, 220, 100), (50, 730, 150, 55))
pygame.draw.ellipse(surface, (220, 255, 220, 100), (-50, 650, 150, 55))
pygame.draw.ellipse(surface, (220, 255, 220, 100), (130, 200, 600, 150))
pygame.draw.ellipse(surface, (220, 255, 220, 100), (-100, 50, 600, 150))
pygame.draw.ellipse(surface, (220, 255, 220, 100), (-150, 400, 600, 150))
screen.blit(surface, (0,0))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()