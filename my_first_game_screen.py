import pygame
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My first game screen")


BG_COLOR = (58, 58, 58)

penguin_image = pygame.transform.scale(pygame.image.load("bg.png").convert_alpha(), (300, 300))
penguin_rect = penguin_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))

text = pygame.font.Font(None, 36).render("Hello World", True, pygame.Color("black"))
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110))

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        display_surface.fill(BG_COLOR)

        
        display_surface.blit(penguin_image, penguin_rect)
        display_surface.blit(text, text_rect)

        
        pygame.display.flip()
        clock.tick(15)

    pygame.quit()

game_loop()