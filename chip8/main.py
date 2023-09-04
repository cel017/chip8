from time import perf_counter as perfCounter
import pygame

from config import INTERVAL
from renderer import EmulatorScreen
from cpu import Chip8CPU


def mainLoop():
    # init emulator render surface and CPU
    emulatorScreen = EmulatorScreen()
    chip8CPU = Chip8CPU(emulatorScreen)
    chip8CPU.loadRom()

    # accumulates time every loop
    timer = 0
    startTime = perfCounter()

    while chip8CPU.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                chip8CPU.quit()
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

if __name__ == "__main__":
    mainLoop()
    pygame.quit()