import pygame
pygame.init()
pygame.event.get()
pygame.display.set_mode((100,100))
x=True
while x:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    pygame.display.flip()