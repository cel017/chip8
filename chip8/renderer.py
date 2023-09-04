import pygame 
import numpy as np

from config import (COLS, ROWS, COLORS)

class EmulatorScreen():

    def __init__(self, scale=10):
        self.scale = scale
        self.surface = pygame.display.set_mode((COLS*scale, ROWS*scale))
        self.clear()
        pygame.mixer.init(size=32)

    def clear(self):
        self.surface.fill(COLORS["black"])

    def drawPixel(self, pos, color):
        xScaled = pos[0]*self.scale
        yScaled = pos[1]*self.scale

        pygame.draw.rect(self.screen,
                         COLORS[color],
                         (xScaled, yScaled, self.scale, self.scale))
    
    def isPixel(self, pos):
        # returns pixel state
        pxColor = self.surface.get_at((pos[0]*self.scale, pos[1]*self.scale))
        return 0 if pxColor == COLORS["black"] else 1

    def playSound(self):
        buffer = np.sin(2 * np.pi * np.arange(44100) * 220 / 44100).astype(np.float32)
        sound = pygame.mixer.Sound(buffer)
        sound.play(0)
        pygame.time.wait(int(sound.get_length() * 1000))

