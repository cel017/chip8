import sys
import pygame
from pathlib import Path
from time import perf_counter as perfCounter

from cpu import Chip8CPU
from renderer import EmulatorScreen
from config import INTERVAL, INTERVAL_SOUND_DELAY


def mainLoop(romPath):
    emulatorScreen = EmulatorScreen()
    chip8CPU = Chip8CPU(emulatorScreen)
    chip8CPU.loadRom(romPath)
    
    timer = 0
    timer_sound_delay = 0
    startTime = perfCounter()

    while chip8CPU.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                chip8CPU.quit()

        endTime = perfCounter()
        timer += endTime-startTime
        timer_sound_delay += endTime-startTime
        startTime = endTime

        if timer_sound_delay >= INTERVAL_SOUND_DELAY:
            chip8CPU.updateTimers()
            timer_sound_delay %= INTERVAL_SOUND_DELAY

        if timer >= INTERVAL:
            chip8CPU.cycle()
            timer %= INTERVAL

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <rom>")
        sys.exit(1)
    mainLoop(Path(sys.argv[1]))
    pygame.quit()