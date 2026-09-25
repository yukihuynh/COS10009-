import pygame
import sys

DEBUG = len(sys.argv) > 1
if DEBUG:
    print("Debug mode ON")

class Cell:
    def __init__(self):
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.vacant = False
        self.visited = False
        self.on_path = False

    def copy_from(self, other: "Cell"):
        self.north = other.north
        self.south = other.south
        self.east = other.east
        self.west = other.west
        self.vacant = other.vacant
        self.visited = other.visited
        self.on_path = other.on_path


# Initialize Pygame
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Creation")
clock = pygame.time.Clock()

# Colors
GREEN = (0, 255, 0)
YELLOW = (255, 255, 100)
RED = (255, 0, 0)

# Maze parameters
CELL_DIM = 60
x_cell_count = SCREEN_WIDTH // CELL_DIM
y_cell_count = SCREEN_HEIGHT // CELL_DIM

# Create maze grid
maze = []
for col in range(x_cell_count):
    maze.append([])
    for row in range(y_cell_count):
        maze[col].append(Cell())

# -------------------------------------------------
# LINK NEIGHBOURS (FIXED)
# -------------------------------------------------
col = 0 
while col < x_cell_count:
    row = 0 
    while row < y_cell_count:
        cell = maze[col][row]

        if row > 0:
            cell.north = maze[col][row - 1]

        if row < y_cell_count - 1:
            cell.south = maze[col][row + 1]

        if col > 0:
            cell.west = maze[col - 1][row]

        if col < x_cell_count - 1:
            cell.east = maze[col + 1][row]

        row += 1
    col += 1


# -------------------------------------------------
# PRINT MAZE (OPTIONAL DEBUG)
# -------------------------------------------------
def print_maze():
    col = 0
    while col < x_cell_count:
        row = 0
        while row < y_cell_count:
            cell = maze[col][row]
            print(
                f"Cell x:{col}, y:{row} | "
                f"N:{cell.north is not None} "
                f"S:{cell.south is not None} "
                f"E:{cell.east is not None} "
                f"W:{cell.west is not None}"
            )
            row += 1
        print("----")
        col += 1

# print_maze()


# -------------------------------------------------
# RESET BEFORE SEARCH
# -------------------------------------------------
def reset_maze():
    for col in range(x_cell_count):
        for row in range(y_cell_count):
            cell = maze[col][row]
            cell.visited = False
            cell.on_path = False


# -------------------------------------------------
# SEARCH (FULLY IMPLEMENTED)
# -------------------------------------------------
def search(cell_x, cell_y):
    cell = maze[cell_x][cell_y]

    # Can't walk here
    if not cell.vacant or cell.visited:
        return None

    cell.visited = True

    # Reached right side
    if cell_x == x_cell_count - 1:
        return [[cell_x, cell_y]]

    # Explore directions
    directions = [
        (cell.north, cell_x, cell_y - 1),
        (cell.south, cell_x, cell_y + 1),
        (cell.east,  cell_x + 1, cell_y),
        (cell.west,  cell_x - 1, cell_y),
    ]

    for neighbour, nx, ny in directions:
        if neighbour is not None:
            path = search(nx, ny)
            if path is not None:
                return [[cell_x, cell_y]] + path

    return None


# -------------------------------------------------
# MARK PATH
# -------------------------------------------------
def walk(path):
    if path is None:
        return
    for (x, y) in path:
        maze[x][y].on_path = True


# -------------------------------------------------
# MAIN LOOP
# -------------------------------------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            col = mouse_pos[0] // CELL_DIM
            row = mouse_pos[1] // CELL_DIM

            # Left click → toggle path
            if event.button == 1:
                maze[col][row].vacant = not maze[col][row].vacant

            # Right click → search
            elif event.button == 3:
                reset_maze()
                path = search(col, row)
                walk(path)

    # Draw
    screen.fill((0, 204, 0))

    for col in range(x_cell_count):
        for row in range(y_cell_count):
            cell = maze[col][row]

            color = YELLOW if cell.vacant else GREEN
            if cell.on_path:
                color = RED

            pygame.draw.rect(
                screen,
                color,
                (col * CELL_DIM, row * CELL_DIM, CELL_DIM - 1, CELL_DIM - 1)
            )

    pygame.display.flip()
    clock.tick(60)