import pygame 
import numpy as np

from config import (COLS, ROWS, COLORS)

class EmulatorScreen():

    def __init__(self, scale=10):
        self.scale = scale
        self.screenArray = [[False]*(ROWS) for _ in range(COLS)]
        self.surface = pygame.display.set_mode((COLS*scale, ROWS*scale))
        self.clear()
        pygame.mixer.init(size=32)


    def clear(self):
        self.screenArray = [[False]*(ROWS) for _ in range(COLS)]
        self.surface.fill(COLORS["black"])

    def drawPixel(self, pos):
        posX = pos[0]%64
        posY = pos[1]%32
        self.screenArray[posX][posY] = True

        xScaled = posX*self.scale
        yScaled = posY*self.scale

        pygame.draw.rect(self.surface,
                         COLORS["white"],
                         (xScaled, yScaled, self.scale, self.scale))
    
    def erasePixel(self, pos):
        posX = pos[0]%64
        posY = pos[1]%32
        self.screenArray[posX][posY] = False

        xScaled = posX*self.scale
        yScaled = posY*self.scale

        pygame.draw.rect(self.surface,
                        COLORS["black"],
                        (xScaled, yScaled, self.scale, self.scale))

    def isPixel(self, pos):
        # returns pixel state
        return self.screenArray[pos[0]%64][pos[1]%32]

    def playSound(self):
        buffer = np.sin(2 * np.pi * np.arange(44100) * 220 / 44100).astype(np.float32)
        sound = pygame.mixer.Sound(buffer)
        sound.play(0)
        pygame.time.wait(int(sound.get_length() * 1000))

