import pygame
from random import choice
import generate

RES = WIDTH, HEIGHT = 1920, 1080
TILE = 50
size = 25
cols, rows = size, size

pygame.init()
sc = pygame.display.set_mode(RES)
clock = pygame.time.Clock()


class Cell:
    def __init__(self, x, y, status=None):
        self.x, self.y = x, y
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
        self.visited = True
        self.status = status


    def draw(self):
        x, y = self.x * TILE, self.y * TILE
        if self.visited:
            if self.status == None: color = "black"
            elif self.status == "used": color = "white"
            elif self.status == "lock": color = "red"
            elif self.status == "free": color = "green"
            elif self.status == "empty": color = "black"
            else: color = "gray"
            pygame.draw.rect(sc, pygame.Color(color), (x, y, TILE, TILE))

        if self.walls['top']:
            pygame.draw.line(sc, pygame.Color('darkorange'), (x, y), (x + TILE, y), 3)
        if self.walls['right']:
            pygame.draw.line(sc, pygame.Color('darkorange'), (x + TILE, y), (x + TILE, y + TILE), 3)
        if self.walls['bottom']:
            pygame.draw.line(sc, pygame.Color('darkorange'), (x + TILE, y + TILE), (x , y + TILE), 3)
        if self.walls['left']:
            pygame.draw.line(sc, pygame.Color('darkorange'), (x, y + TILE), (x, y), 3)

def gen():
    global tmp_grid
    field = generate.generation(gen_count=50, size=size, return_html_field=True)
    tmp_grid = []
    for x in range(len(field)):
        for y in range(len(field[x])):
            tmp_grid.append(Cell(x,y, field[x][y][0]))
gen()

while True:
    sc.fill(pygame.Color('darkslategray'))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F5: gen()


    [cell.draw() for cell in tmp_grid]



   

    pygame.display.flip()
    clock.tick(30)


