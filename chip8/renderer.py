import pygame 
import numpy as np

from config import (COLS, ROWS, COLORS)

class EmulatorScreen():

    def __init__(self, scale=10):
        self.scale = scale
        self.screenArray = [[False]*(ROWS) for _ in range(COLS)]
        self.surface = pygame.display.set_mode((COLS*scale, ROWS*scale))
        self.clear()
        pygame.mixer.init()

    def clear(self):
        self.screenArray = [[False]*(ROWS) for _ in range(COLS)]
        self.surface.fill(COLORS["black"])

    def drawPixel(self, pos):
        posX = pos[0]%COLS
        posY = pos[1]%ROWS
        self.screenArray[posX][posY] = True

        xScaled = posX*self.scale
        yScaled = posY*self.scale

        pygame.draw.rect(self.surface,
                         COLORS["white"],
                         (xScaled, yScaled, self.scale, self.scale))
    
    def erasePixel(self, pos):
        posX = pos[0]%COLS
        posY = pos[1]%ROWS
        self.screenArray[posX][posY] = False

        xScaled = posX*self.scale
        yScaled = posY*self.scale

        pygame.draw.rect(self.surface,
                        COLORS["black"],
                        (xScaled, yScaled, self.scale, self.scale))

    def isPixel(self, pos):
        # returns pixel state
        return self.screenArray[pos[0]%COLS][pos[1]%ROWS]

    def playSound(self):
        sound = pygame.mixer.Sound((np.sin(2 * np.pi * np.arange(44100) * 220 / 44100) * 32767).astype(np.int16))
        sound.play(-1)
    
    def stopSound(self):
        pygame.mixer.stop()
