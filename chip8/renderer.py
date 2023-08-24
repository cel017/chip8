import pygame 

from config import (COLS, ROWS, COLORS)

class EmulatorScreen():

    def __init__(self, scale=10):
        self.scale = scale
        self.surface = pygame.display.set_mode((COLS*scale, ROWS*scale))

        self.clear()

    def clear(self):
        self.surface.fill(COLORS["white"])

    def drawPixel(self, pos, color):
        xScaled = pos[0]*self.scale
        yScaled = pos[1]*self.scale

        draw.rect(self.screen,
                  COLORS[color],
                  (xScaled, yScaled, self.scale, self.scale))
    def flip(self):
        pygame.display.flip()