import pygame
import sys

# Initialize Pygame
pygame.init()

# Create a window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mouse Position Example")

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get mouse position
    x, y = pygame.mouse.get_pos()

    # Fill background
    screen.fill((30, 30, 30))

    # Display mouse coordinates
    font = pygame.font.Font(None, )
    text_surface = font.render(f"Mouse Position: ({x}, {y})", True, (255, 255, 255))
    screen.blit(text_surface, (20, 20))

    # Update display
    pygame.display.flip()
