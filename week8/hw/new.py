import pygame
import time

# Reusable Function to display text
def draw_text(surface, text, size, color, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    surface.blit(text_surface, text_rect)


# ----------------------------
# PYGAME SETUP
# ----------------------------
pygame.init()
screen = pygame.display.set_mode((200, 130))
pygame.display.set_caption("Game Cycle Example")

clock = pygame.time.Clock()
running = True
dt = 0.0

# ----------------------------
# INITIALISE
# ----------------------------
font = pygame.font.SysFont(None, 48)
BLACK = (0, 0, 0)

cycle_count = 0
shape_x = 0   # ✅ REQUIRED (start position)

# Load background (optional)
background_image = None
try:
    background_image = pygame.image.load("earth.png").convert()
except pygame.error:
    background_image = None


# ----------------------------
# GAME LOOP
# ----------------------------cd
while running:

    # 1. HANDLE EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. UPDATE GAME STATE
    cycle_count += 1
    shape_x += 10   # ✅ REQUIRED (move shape)

    # Optional: reset when off screen
    if shape_x > 200:
        shape_x = 0

    time.sleep(1)  # slow down (for demo only)

    # 3. DRAW / RENDER
    screen.fill("purple")

    if background_image:
        screen.blit(background_image, (0, 0))

    draw_text(screen, f'Cycle: {cycle_count}', 20, BLACK, 100, 10)

    # ✅ REQUIRED: draw shape at (shape_x, 30)
    pygame.draw.rect(screen, (255, 0, 0), (shape_x, 30, 50, 50))

    # 4. UPDATE DISPLAY
    pygame.display.flip()

    # 5. CONTROL FPS
    dt = clock.tick(60) / 1000


pygame.quit()