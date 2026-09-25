import pygame
import sys

# ----------------------------
# CONSTANTS
# ----------------------------
WIN_WIDTH = 600
WIN_HEIGHT = 800

TOP_COLOR = (30, 177, 250)
BOTTOM_COLOR = (29, 77, 181)

# ----------------------------
# CLASSES
# ----------------------------
class Track:
    def __init__(self, title, location):
        self.title = title
        self.location = location


class Album:
    def __init__(self, artist, title, year, genre, tracks, artwork):
        self.artist = artist
        self.title = title
        self.year = year
        self.genre = genre
        self.tracks = tracks

        # ✅ SAFE IMAGE LOADING (no crash)
        try:
            self.artwork = pygame.image.load("images/" + artwork)
        except:
            self.artwork = pygame.Surface((200, 200))
            self.artwork.fill((100, 100, 100))


# ----------------------------
# GLOBALS
# ----------------------------
albums = []
selected_album = None
current_track = None
track_font = None


# ----------------------------
def init():
    global track_font

    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("Music Player")

    track_font = pygame.font.SysFont(None, 28)

    return screen


# ----------------------------
# LOAD ALBUMS (MATCHES YOUR FILE)
# ----------------------------
def load_albums():
    global albums

    file = open("albums.txt", "r")

    num_albums = int(file.readline())

    # fallback artwork names (you can replace later)
    artwork_files = [
        "neil.webp",
        # "platters.jpg",
        # "don.jpg",
        # "carly.jpg"
    ]

    for i in range(num_albums):
        artist = file.readline().strip()
        title = file.readline().strip()
        year = file.readline().strip()
        genre = file.readline().strip()

        num_tracks = int(file.readline())
        tracks = []

        for j in range(num_tracks):
            t_title = file.readline().strip()
            t_loc = file.readline().strip()
            tracks.append(Track(t_title, t_loc))

        artwork = artwork_files[i] if i < len(artwork_files) else "default.jpg"

        albums.append(Album(artist, title, year, genre, tracks, artwork))

    file.close()


# ----------------------------
def draw_background(screen):
    screen.fill(TOP_COLOR)
    pygame.draw.rect(screen, BOTTOM_COLOR,
                     (0, WIN_HEIGHT // 2, WIN_WIDTH, WIN_HEIGHT // 2))


# ----------------------------
def draw_albums(screen):
    x = 50
    y = 50
    size = 200
    gap = 20

    for album in albums:
        img = pygame.transform.scale(album.artwork, (size, size))
        screen.blit(img, (x, y))

        x += size + gap
        if x > 350:
            x = 50
            y += size + gap


# ----------------------------
def area_clicked(leftX, topY, rightX, bottomY):
    mx, my = pygame.mouse.get_pos()
    return leftX <= mx <= rightX and topY <= my <= bottomY


# ----------------------------
def play_track(track_index, album):
    try:
        pygame.mixer.music.load(album.tracks[track_index].location)
        pygame.mixer.music.play()
    except:
        print("Error loading sound file")


# ----------------------------
def handle_mouse_click():
    global selected_album, current_track

    x = 50
    y = 50
    size = 200
    gap = 20

    # Album click
    for album in albums:
        if area_clicked(x, y, x + size, y + size):
            selected_album = album
            current_track = None
            return

        x += size + gap
        if x > 350:
            x = 50
            y += size + gap

    # Track click
    if selected_album:
        y_pos = 500
        for i, track in enumerate(selected_album.tracks):
            if area_clicked(50, y_pos, 550, y_pos + 30):
                pygame.mixer.music.stop()
                current_track = i
                play_track(i, selected_album)
                return
            y_pos += 40


# ----------------------------
def draw(screen):
    draw_background(screen)
    draw_albums(screen)

    # Show album info
    if selected_album:
        info = f"{selected_album.title} - {selected_album.artist}"
        text = track_font.render(info, True, (255, 255, 255))
        screen.blit(text, (50, 450))

        # Tracks
        y = 500
        for i, track in enumerate(selected_album.tracks):
            color = (255, 0, 0) if i == current_track else (0, 0, 255)
            text = track_font.render(track.title, True, color)
            screen.blit(text, (50, y))
            y += 40

    # Now Playing
    if current_track is not None:
        text = track_font.render("Now Playing...", True, (255, 255, 0))
        screen.blit(text, (50, 420))

    pygame.display.flip()


# ----------------------------
def update():
    pass


# ----------------------------
def main():
    screen = init()
    clock = pygame.time.Clock()

    load_albums()

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    handle_mouse_click()

        update()
        draw(screen)
        clock.tick(60)


if __name__ == "__main__":
    main()