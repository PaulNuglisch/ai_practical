from pkg.config import BLACK, WHITE, BLUE, GREEN, RED, WIDTH, HEIGHT, MARGIN
import math
import pygame

class Field:
    def __init__(self, x, y, color=WHITE):
        self.x = x
        self.y = y
        self.color = color
        self.g = float('inf')
        self.h = 0
        self.f = float('inf')
        self.parent = None

    def draw(self, screen):
        pygame.draw.rect(screen,
                         self.color,
                         [(MARGIN + WIDTH) * self.y + MARGIN,
                          (MARGIN + HEIGHT) * self.x + MARGIN,
                          WIDTH,
                          HEIGHT])
    
    def __lt__(self, other):
        return self.f < other.f

class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[Field(x, y) for y in range(cols)] for x in range(rows)]
        self.goal = None

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
    
    def calcH(self, field):
        return math.sqrt((field.x - self.goal.x)^2 + (field.y - self.goal.y)^2)
