import pygame
import os

pygame.init()

screen = pygame.display.set_mode([512, 512])

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    img = pygame.image.load(os.path.join(os.path.dirname(__file__), 'data/red.png'))

    screen.fill((18, 18, 18))
    screen.blit(img, pygame.Rect(100, 100, 100, 100))
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    pygame.display.flip()

pygame.quit()
