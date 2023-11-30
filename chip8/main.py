import sys
import pygame
from pathlib import Path
from time import perf_counter as perfCounter

from cpu import Chip8CPU
from config import INTERVAL
from renderer import EmulatorScreen


def mainLoop(romPath):
    emulatorScreen = EmulatorScreen()
    chip8CPU = Chip8CPU(emulatorScreen)
    chip8CPU.loadRom(romPath)
    
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
            timer %= INTERVAL

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <rom>")
        sys.exit(1)
    mainLoop(Path(sys.argv[1]))
    pygame.quit()