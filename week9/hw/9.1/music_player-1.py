import pygame
import sys

# Constants
WIN_WIDTH = 600
WIN_HEIGHT = 800

TOP_COLOR = (30, 177, 250)
BOTTOM_COLOR = (29, 77, 181)

# Genre dictionary (replaces Ruby module)
GENRE = {
    "POP": 1,
    "CLASSIC": 2,
    "JAZZ": 3,
    "ROCK": 4
}

# Initialization
def init():
    global track_font

    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("Music Player")

    track_font = pygame.font.SysFont(None, 24)

    return screen

# Put your record definitions here

# Load albums and tracks
def load_albums():
    # Put in your code here to load albums and tracks
    pass


# Draw the artwork on the screen for all the albums
def draw_albums(screen, albums):
    # complete this code
    pass

# Detects if a 'mouse sensitive' area has been clicked on
# returns True or False

def area_clicked(leftX, topY, rightX, bottomY):
    # complete this code
    pass


# Takes a String title and an Integer ypos
# You may want to use the following
def display_track(screen, title, ypos):
    screen.blit(track_font.render(title, True, (0, 0, 0)), (50, ypos))


# Takes a track index and an album and plays the Track
def play_track(track, album):
    # complete the missing code
    song_location = album["tracks"][track].location
    pygame.mixer.music.load(song_location)
    pygame.mixer.music.play()


# Draw a coloured background using TOP_COLOR and BOTTOM_COLOR
def draw_background(screen):
    # complete this code
    pass

# Update
def update():
    pass

# Draws the album images and the track list
def draw(screen):
    # Complete the missing code
    draw_background(screen)

    pygame.display.flip()


# Mouse Click Handling
def handle_mouse_click():
    # What should happen here?
    pass


def main():
    # Initialise
    screen = init()
    clock = pygame.time.Clock()

    load_albums()

    # Main Loop
    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    handle_mouse_click()

        # Update Logic
        update()
        # Draw
        draw(screen)
        # Clock tick
        clock.tick(60)


if __name__ == "__main__":
    main()