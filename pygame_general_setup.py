import pygame
import sys

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((600, 400))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(1)
    
    screen.fill((0, 0, 0))
    screen.display.flip()
    clock.tick(60)