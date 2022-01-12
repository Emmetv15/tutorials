## base window 

import pygame
from spriteandmovement import *
pygame.init()

screen = pygame.display.set_mode([512, 512])

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys=pygame.key.get_pressed()
    if keys[K_LEFT]:
        location-=1
        if location==-1:
            location=0
    if keys[K_RIGHT]:
        location+=1
        if location==5:
            location=4

    screen.fill((18, 18, 18))
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    pygame.display.flip()

pygame.quit()
