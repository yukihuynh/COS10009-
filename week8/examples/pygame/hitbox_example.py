import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 400
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hitbox Demo")

clock = pygame.time.Clock()

# Player and enemy hitboxes
player = pygame.Rect(100, 250, 50, 80)
enemy = pygame.Rect(500, 250, 50, 80)

# Attack hitbox
attack_box = pygame.Rect(0, 0, 40, 40)
attacking = False

while True:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                attacking = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                attacking = False

    # Player movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5

    # Update attack box
    if attacking:
        attack_box.midleft = player.midright

    # Collision detection
    hit = False
    if attacking and attack_box.colliderect(enemy):
        hit = True

    # Drawing
    screen.fill((30, 30, 30))

    # Player
    pygame.draw.rect(screen, (0, 200, 255), player)

    # Enemy
    pygame.draw.rect(screen, (255, 80, 80), enemy)

    # Attack hitbox
    if attacking:
        pygame.draw.rect(screen, (255, 255, 0), attack_box)

    # Change enemy color if hit
    if hit:
        pygame.draw.rect(screen, (255, 255, 0), enemy)

    pygame.display.flip()
    clock.tick(FPS)