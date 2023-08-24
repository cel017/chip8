from config import *


class CPU:
    '''
    ---CHIP-8 CPU Class---
    References :
        https://en.wikipedia.org/wiki/CHIP-8
        http://devernay.free.fr/hacks/chip8/C8TECH10.HTM#0.0
        https://github.com/mattmikolay/chip-8/wiki/Mastering-CHIP%E2%80%908
    '''
    def __init__(self, screen):
        # 8-bit(1)  : timers 
        self.timerDelay = 0
        self.timerSound = 0
        
        # 16-bit(1) : program counter
        self.pc = PROGRAM_COUNTER_INITIAL
        
        # 8-bit(16) : general purpose registers (V0-VF)
        self.vReg = bytearray(16)
        
        # 16-bit(1) : index (stores memory address)
        self.index = 0
        
        # 16-bit(16) : stack
        self.stack = []

        # 4096 bytes : assigned memory
        self.memory  = bytearray(MAX_MEMORY)

    def cycle(self):
        # combine 8-bit operands to get
        # 16-bit opcode: {op1}{op2}
        op1 = self.memory[self.pc] << 8
        op2 = self.memory[self.pc+1]
        opcode = op1+op2

        self.execInstruction(opcode)

    def execInstruction(self, opcode):
        self.pc+=2
        return


    def reset(self):
        return

    def loadRom(self, filename):
        start = PROGRAM_COUNTER_INITIAL
        with open(filename, 'rb') as rom:
            for i, line in enumerate(rom.read()):
                self.memory[start+i] = line

    def updateTimers(self):
        # timers are active when != 0
        if timer_sound: timer_sound -= 1
        if timer_delay: timer_delay -= 1

