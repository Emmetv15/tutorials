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
    pygame.key.set_repeat(50,50)
    for event in pygame.event.get():
        keys=pygame.key_pressed()
        pygame.key
        if (event.type == pygame.QUIT):
            bProgramLoop = False
        if keys[pygame.K_LEFT]:
            xoffset-=1
            print("left")
        if keys[pygame.K_RIGHT]:
            print("right")
            xoffset+=1
        if keys[pygame.K_UP]:
            print("up")
            yoffset-=1
        if keys[pygame.K_DOWN]:
            print("down")
            yoffset+=1


    screen.fill((18, 18, 18))
    pygame.draw.circle(screen, (0, 0, 255), (250+xoffset, 250+yoffset), 75)
    pygame.display.flip()

pygame.quit()