import pygame
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WIDTH = 22
HEIGHT = 22
MARGIN = 3
     
class Field:
    def __init__(self, x, y, color=WHITE):
        self.x = x
        self.y = y
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen,
                         self.color,
                         [(MARGIN + WIDTH) * self.y + MARGIN,
                          (MARGIN + HEIGHT) * self.x + MARGIN,
                          WIDTH,
                          HEIGHT])

class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[Field(x, y) for y in range(cols)] for x in range(rows)]

    def draw(self, screen):
        for row in self.grid:
            for field in row:
                draw_x = field.y
                draw_y = self.rows - 1 - field.x  # flip vertically
                pygame.draw.rect(screen,
                                 field.color,
                                 [(MARGIN + WIDTH) * draw_x + MARGIN,
                                  (MARGIN + HEIGHT) * draw_y + MARGIN,
                                  WIDTH,
                                  HEIGHT])

    def set_obstacles(self, positions):
        for y, x in positions:
            self.grid[y][x].color = BLACK

    
pygame.init()
size = (500, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
done = False
clock = pygame.time.Clock()
grid = Grid(20, 20)

walls = [
    *[(y, 9) for y in range(0, 10)],      # vertical wall at column 10
    *[(9, x) for x in range(4, 10)],      # horizontal wall at row 10
    *[(y, 16) for y in range(9, 20)]     # vertical wall at column 18
]
grid.set_obstacles(walls)

# Start and goal
grid.grid[0][0].color = GREEN     # S at (1,1)
grid.grid[19][19].color = RED     # G at (20,20)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

            # ---
        # The code here ist called once per clock tick
        # Let your algorithm loop here
            # ---
        screen.fill(BLACK)
        grid.draw(screen)

        pygame.display.flip()
        clock.tick(60)
pygame.quit()
