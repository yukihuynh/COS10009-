# Example file showing a circle moving on screen
import pygame
import time


# Reusable Function to display text
def draw_text(surface, text, size, color, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    surface.blit(text_surface, text_rect)

# Instructions:
# Add a shape_x variable in the following (similar to the cycle one)
# that is initialised to zero then incremented by 10 in update.
# Change the draw/render part of the game loop to draw a shape (circle or square)
# (50 pixels in width and height) with a y coordinate of 30
# and an x coordinate of shape_x.

# initialize creates a window with a width an a height
# and a caption. It also sets up any variables to be used.
# pygame setup
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 400,260
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0.0

# 0. Initialise - variables and resources
# Use pygame.font.SysFont(None, size) for a default system font,
# or pygame.font.Font(file_path, size) for a custom font file (.ttf)
font = pygame.font.SysFont(None, 48) # Default font, size 48
BLACK = (0, 0, 0)
RED = (255,0,0)

cycle_count = 0
shape_x = 0
# Load the background image (place "background.png" in the same directory as your script)
# Use .convert() for optimization
background_image = None
try:
    background_image = pygame.image.load("earth.png").convert()
    # Optional: Scale the image to fit the screen size if it's different
    background_image = pygame.transform.scale(background_image, (400, 260))
except pygame.error as e:
    print(f"Error loading image: {e}")
    # Fallback to a solid color if image fails to load
    background_image = None
    screen.fill((255, 255, 255)) # Fill with white
# Create a count of cycles
cycle_count = 0

# Pygame Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    # 2. Update game state (e.g., move a character)
    cycle_count += 1
    shape_x += 10 
    if shape_x > 480:
        shape_x = 0
    time.sleep(1) # We sleep 1 second just to make the loop slower for this task, don't re-use this in the future.

    # 3. Draw/Render
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    if background_image:
        # Blit the background image at the top-left corner (0, 0)
        screen.blit(background_image, (0, 0))
    else:
        background_image = None 
        screen.fill(BLACK)
    draw_text(screen, f'Cycle count: {cycle_count}', 20, BLACK, 10, 10)

    # 4. Update the display
    # flip() the display to put your work on screen
    pygame.draw.rect(screen, RED, (shape_x, 30, 50, 50) )
    pygame.display.flip()


    dt = clock.tick(60) / 1000

pygame.quit()