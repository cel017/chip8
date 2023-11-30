from time import perf_counter as perfCounter
import pygame

from config import INTERVAL
from renderer import EmulatorScreen
from cpu import Chip8CPU


def mainLoop():
    # init emulator render surface and CPU
    emulatorScreen = EmulatorScreen()
    chip8CPU = Chip8CPU(emulatorScreen)
    chip8CPU.loadRom("roms/br8kout.ch8")

    # accumulates time every loop
    timer = INTERVAL
    startTime = perfCounter()

    while chip8CPU.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                chip8CPU.quit()

        endTime = perfCounter()
        timer += endTime-startTime
        startTime = endTime
        
        if timer >= INTERVAL:
            chip8CPU.cycle()
            
            # decrement insead of reset:
            # accumulates extra milliseconds
            timer -= INTERVAL
            # handle unexpected delay
            timer %= INTERVAL

if __name__ == "__main__":
    mainLoop()
    pygame.quit()