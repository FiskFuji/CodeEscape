import pygame as pg
import pygame.gfxdraw as pgf
import sys
import random as rnd
"""
pg.init()

screen = pg.display.set_mode((400, 400))
clock = pg.time.Clock()


RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 255, 255)

frame = [
    '.............',
    '.....XXX.....',
    '....X...X....',
    '....X....X...',
    '....X........',
    '....X........',
    '....X........',
    '....X....X...',
    '....X...X....',
    '.....XXX.....',
    '.............',
    '....XXXXXX...',
    ]

startX = 200
startY = 200


for line in frame:

    for char in line:

        if char == '.':
            startX += 1
            continue

        elif char == 'X':
            pgf.pixel(screen, startX, startY, RED)
            startX += 1

    startY += 1
    startX = 200
"""

class Particle:

    def __init__(self, color):
        self.dimensions = pg.display.Info()
        self.x = rnd.randint(0, self.dimensions.current_w)
        self.y = rnd.randint(0, self.dimensions.current_h)
        self.color = color
        self.fast = rnd.randint(0, 1)

    def slowMove(self):
        if self.x < 0:
            self.changeY()
            self.x = self.dimensions.current_w
            
        self.x -= 1

    def fastMove(self):
        if self.x < 0:
            self.changeY()
            self.x = self.dimensions.current_w

        self.x -= 2

    def changeY(self):
        self.y += rnd.randint(-4, 4)
        
    def update(self, surface):
        if self.fast:
            self.fastMove()
            
        elif not self.fast:
            self.slowMove()
            
        pgf.pixel(surface, self.x, self.y, self.color)

"""
particles = [Particle(WHITE) for i in range(28)]
particles2 = [Particle(BLUE) for i in range(18)]
particles.extend(particles2)
"""
"""
while 1:

    screen.fill((0, 0, 0))
    clock.tick(60)
    for particle in particles:
        particle.update(screen)
        
    pg.display.update()

    for event in pg.event.get():

        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
                
"""
