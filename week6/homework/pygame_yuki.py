"""
This program demonstrates how to draw various shapes using the Pygame library.
It includes examples of drawing rectangles, polygons, circles, ellipses, lines, and arcs
with different colors and styles.
Please ensure you have Pygame installed in your Python environment to run this code.
Install pygame using `pip install pygame` if you haven't already.

Play around with the parameters of each shape to see how they affect the drawing!
When you are ready create your own Pygame program to draw a picture of your choice using different shapes.

Documentation reference:
https://www.pygame.org/docs/ref/draw.html 
"""
import pygame
from math import pi as PI
import sys
# Initialize Pygame
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Shapes")
clock = pygame.time.Clock()

"""
Define colors as constants for better readability.
Colors are defined using RGB values.
"""
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
SEA_GREEN = (46, 139, 87)
PURPLE = (128, 0, 128)
MAROON = (128, 0, 0)
WINE_RED = (128, 0, 32)
SKY_BLUE = (135, 206, 235)
ORANGE = (255, 165, 0)
BLACK = (30,30,30)


size = 25 
# Draw a rectangle
squares = [
(340,200),(360,200),(420,200),(440,200),
(320,220),(380,220),(400,220),(460,220),
(300,240),(380,240),(400,240),(480,240),
(300,260),(480,260),
(320,280),(460,280),
(340,300),(440,300),
(360,320),(420,320),
(400,340),(380,340)
]
# Draw all squares
font = pygame.font.Font(None, 24)
# Pygame main loop - For now this just handles quitting the window
running = True
while running:
    # Fill the background with white
    screen.fill(WHITE)
    # Draw heart
    for x, y in squares:
        pygame.draw.rect(screen, RED, (x, y, size, size))

    # Mouse position
    mx, my = pygame.mouse.get_pos()
    text_surface = font.render(f"Mouse Position: ({mx}, {my})", True, BLACK)
    screen.blit(text_surface, (10, 570))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()# Call this function to update the display after drawing
    clock.tick(60)

pygame.quit()
sys.exit() #wait until next frame (at 60 FPS)