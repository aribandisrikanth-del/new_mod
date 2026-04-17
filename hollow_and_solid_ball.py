import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.circle(screen, (0,125,255), (100, 120), 60, 1)
    pygame.draw.circle(screen, (0, 125, 255), (300, 120), 60, 0)
    pygame.display.flip()