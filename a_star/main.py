import pygame
import math
from pkg.grid import Field, Grid
from pkg.config import BLACK, WHITE, BLUE, GREEN, RED, WIDTH, HEIGHT, MARGIN
   
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
    *[(y, 16) for y in range(9, 20)]      # vertical wall at column 18
]
grid.set_obstacles(walls)

# Start and goal
grid.grid[0][0].color = GREEN     # S at (1,1)
grid.grid[19][19].color = RED     # G at (20,20)
grid.goal = grid.grid[19][19]

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


