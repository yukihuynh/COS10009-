from pathlib import Path

import pygame
from dataclasses import dataclass


WIDTH = 800
HEIGHT = 600
FPS = 60
TILE_SIZE = 64
MAX_FALL_SPEED = 14

BASE_DIR = Path(__file__).resolve().parent
CHARACTER_DIR = BASE_DIR / "media" / "character"
TILES_DIR = BASE_DIR / "media" / "tiles"


@dataclass
class GameState:
    player: pygame.Rect
    player_pos: pygame.Vector2
    vel_x: float
    vel_y: float
    on_ground: bool
    facing_right: bool


def _first_existing_path(paths):
    for path in paths:
        if path.exists():
            return path
    return None


def load_animation(folder, name, count):
    frames = []
    for i in range(1, count + 1):
        candidate_paths = [
            folder / f"{name} ({i}).png",
            folder / f"{name.lower()} ({i}).png",
            folder / f"{name.capitalize()} ({i}).png",
        ]
        path = _first_existing_path(candidate_paths)
        if path is None:
            raise FileNotFoundError(
                f"Missing frame {i} for '{name}'. Looked for: "
                + ", ".join(str(p) for p in candidate_paths)
            )
        img = pygame.image.load(str(path)).convert_alpha()
        frames.append(pygame.transform.scale(img, (64, 64)))
    return frames


class AnimationController:
    def __init__(self, animations, animation_speed=150):
        if not animations:
            raise ValueError("AnimationController requires at least one animation state.")
        if "idle" not in animations:
            raise ValueError("AnimationController requires an 'idle' animation state.")
        for state_name, frames in animations.items():
            if not frames:
                raise ValueError(f"Animation state '{state_name}' has no frames.")

        self.animations = animations
        self.state = "idle"
        self.frame_index = 0
        self.image = self.animations[self.state][self.frame_index]
        self.animation_speed = animation_speed  # milliseconds
        self.last_update = pygame.time.get_ticks()

    def set_state(self, new_state):
        if new_state not in self.animations:
            raise ValueError(f"Unknown animation state: {new_state}")
        if new_state != self.state:
            self.state = new_state
            self.frame_index = 0
            self.image = self.animations[self.state][self.frame_index]
            self.last_update = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update >= self.animation_speed:
            self.last_update = now
            frames = self.animations[self.state]
            self.frame_index = (self.frame_index + 1) % len(frames)
            self.image = frames[self.frame_index]

    def get_image(self):
        return self.image


def build_tiles(level_rows):
    tiles = []
    for row_index, row in enumerate(level_rows):
        for col_index, cell in enumerate(row):
            if cell == "X":
                tiles.append(
                    pygame.Rect(
                        col_index * TILE_SIZE,
                        row_index * TILE_SIZE,
                        TILE_SIZE,
                        TILE_SIZE,
                    )
                )
    return tiles


def load_assets():
    idle_frames = load_animation(CHARACTER_DIR, "Idle", 10)
    run_frames = load_animation(CHARACTER_DIR, "Run", 8)
    jump_frames = load_animation(CHARACTER_DIR, "Jump", 12)
    animator = AnimationController(
        {
            "idle": idle_frames,
            "run": run_frames,
            "jump": jump_frames,
        },
        animation_speed=120,
    )

    tile_path = TILES_DIR / "11.png"
    if not tile_path.exists():
        raise FileNotFoundError(f"Missing tile image: {tile_path}")
    tile_img = pygame.image.load(str(tile_path)).convert_alpha()
    tile_img = pygame.transform.scale(tile_img, (TILE_SIZE, TILE_SIZE))
    return animator, tile_img


def create_level():
    level = [
        "........................",
        "........................",
        "........................",
        "........................",
        "..............XX........",
        "..............XX........",
        "...........XXXXXX.......",
        "XXXX....XXXXXXXXXXXX....",
        "XXXXXXXXXXXXXXXXXXXXXXXX",
    ]
    return build_tiles(level)


def create_initial_state():
    player = pygame.Rect(100, 100, 50, 60)
    return GameState(
        player=player,
        player_pos=pygame.Vector2(player.x, player.y),
        vel_x=0.0,
        vel_y=0.0,
        on_ground=False,
        facing_right=True,
    )


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


def apply_horizontal_input(state, keys, speed):
    moving_left = keys[pygame.K_LEFT]
    moving_right = keys[pygame.K_RIGHT]
    state.vel_x = 0.0
    if moving_left and not moving_right:
        state.vel_x = -speed
        state.facing_right = False
    elif moving_right and not moving_left:
        state.vel_x = speed
        state.facing_right = True


def apply_jump_input(state, keys, jump_strength):
    if keys[pygame.K_SPACE] and state.on_ground:
        state.vel_y = jump_strength
        state.on_ground = False


def apply_gravity(state, gravity):
    state.vel_y = min(state.vel_y + gravity, MAX_FALL_SPEED)


def resolve_horizontal_collision(state, tiles):
    state.player_pos.x += state.vel_x
    state.player.x = round(state.player_pos.x)
    for tile in tiles:
        if state.player.colliderect(tile):
            if state.vel_x > 0:
                state.player.right = tile.left
            elif state.vel_x < 0:
                state.player.left = tile.right
            state.player_pos.x = state.player.x


def resolve_vertical_collision(state, tiles):
    state.player_pos.y += state.vel_y
    state.player.y = round(state.player_pos.y)
    state.on_ground = False
    for tile in tiles:
        if state.player.colliderect(tile):
            if state.vel_y > 0:
                state.player.bottom = tile.top
                state.vel_y = 0.0
                state.on_ground = True
            elif state.vel_y < 0:
                state.player.top = tile.bottom
                state.vel_y = 0.0
            state.player_pos.y = state.player.y


def update_physics(state, tiles):
    resolve_horizontal_collision(state, tiles)
    resolve_vertical_collision(state, tiles)


def compute_animation_state(state):
    if not state.on_ground:
        return "jump"
    if state.vel_x != 0:
        return "run"
    return "idle"


def update_animation(animator, state):
    animator.set_state(compute_animation_state(state))
    animator.update()


def update_game(state, tiles, animator, speed, jump_strength, gravity):
    keys = pygame.key.get_pressed()
    apply_horizontal_input(state, keys, speed)
    apply_jump_input(state, keys, jump_strength)
    apply_gravity(state, gravity)
    update_physics(state, tiles)
    update_animation(animator, state)


def draw_background(screen):
    screen.fill((135, 206, 235))


def draw_tiles(screen, tiles, tile_img):
    for tile in tiles:
        screen.blit(tile_img, tile)


def draw_player(screen, state, animator):
    player_image = animator.get_image()
    if not state.facing_right:
        player_image = pygame.transform.flip(player_image, True, False)
    draw_rect = player_image.get_rect(midbottom=state.player.midbottom)
    screen.blit(player_image, draw_rect)


def draw_game(screen, state, tiles, tile_img, animator):
    draw_background(screen)
    draw_tiles(screen, tiles, tile_img)
    draw_player(screen, state, animator)


def show_frame():
    pygame.display.flip()


def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Simple Platformer")
    clock = pygame.time.Clock()

    animator, tile_img = load_assets()
    tiles = create_level()
    state = create_initial_state()

    speed = 5.0
    gravity = 0.5
    jump_strength = -12.0

    running = True
    while running:
        clock.tick(FPS)

        running = handle_events()
        if not running:
            break
        update_game(state, tiles, animator, speed, jump_strength, gravity)
        draw_game(screen, state, tiles, tile_img, animator)
        show_frame()

    pygame.quit()


if __name__ == "__main__":
    main()
