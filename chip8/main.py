from time import perf_counter as perfCounter
import pygame

from config import INTERVAL
from renderer import EmulatorScreen
from cpu import CPU


def mainLoop():
    # emulator render surface
    emulatorScreen = EmulatorScreen()

    # accumulates time every loop
    timer = 0
    startTime = perfCounter()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                keysPressed = pygame.key.get_pressed()

        endTime = perfCounter()
        timer += endTime-startTime
        startTime = endTime

        if timer >= INTERVAL:
            ###
            # CPU CYCLE HERE;
            ###
            
            # decrement insead of reset:
            # accumulates extra milliseconds
            print(timer*1000)
            timer -= INTERVAL
            # handle unexpected delay
            timer %= INTERVAL
            pygame.display.flip()

if __name__ == "__main__":
    mainLoop()
    pygame.quit()