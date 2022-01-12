## code required to draw an object and move it 
import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0

pygame.init()

screen = pygame.display.set_mode([512, 512])

running = True
xoffset = 0
yoffset = 0
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xoffset -= 10
            if event.key == pygame.K_RIGHT:
                xoffset += 10
            if event.key == pygame.K_UP:
                yoffset -= 10
            if event.key == pygame.K_DOWN:
                yoffset += 10


    screen.fill((18, 18, 18))
    pygame.draw.circle(screen, (0, 0, 255), (250+xoffset, 250+yoffset), 75)
    pygame.display.flip()

pygame.quit()