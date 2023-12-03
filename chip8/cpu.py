from config import *
from random import randint

class Chip8CPU:
    '''
    CHIP-8 CPU Class
    References :
        https://en.wikipedia.org/wiki/CHIP-8
        http://devernay.free.fr/hacks/chip8/C8TECH10.HTM#0.0
        https://github.com/mattmikolay/chip-8/wiki/Mastering-CHIP%E2%80%908
    '''
    def __init__(self, screen):
        self.screen = screen
        self.reset()
        self.loadSprites()
        self.running = False

    def reset(self):
        # 8-bit(1)  : timers 
        self.timerDelay = 0
        self.timerSound = 0
        
        # 16-bit(1) : program counter
        self.pc = PROGRAM_COUNTER_INITIAL
        
        # 8-bit(16) : general purpose registers (V0-VF)
        self.vReg = bytearray(VX_TOTAL)
        
        # 16-bit(1) : index (stores memory address)
        self.index = 0
        
        # 16-bit(16) : stack
        self.stack = []

        # 4096 bytes : assigned memory
        self.memory  = bytearray(MEMORY_TOTAL)
    
    def loadRom(self, filename):
        start = PROGRAM_COUNTER_INITIAL
        with open(filename, 'rb') as rom:
            for i, line in enumerate(rom.read()):
                self.memory[start+i] = line
        self.running = True

    def loadSprites(self):
        # load font sprites
        for i in range(len(SPRITES)):
            self.memory[i] = SPRITES[i]

    def updateTimers(self):
        # timers are active when != 0
        if self.timerSound: 
            self.timerSound -= 1
            if self.timerSound == 0:
                self.screen.stopSound()
        if self.timerDelay:
            self.timerDelay -= 1

    def quit(self):
        self.reset()
        self.running = False

    def cycle(self):
        # combine 8-bit operands to get
        # 16-bit opcode: {op1}{op2}
        op1 = self.memory[self.pc] << 8
        op2 = self.memory[self.pc+1]
        opcode = op1|op2

        self.execInstruction(opcode)
        
        # play sound
        if self.timerSound > 0:
            self.screen.playSound()
        
    def execInstruction(self, opcode):
        self.pc+=2

        nnn = opcode & 0x0FFF
        x = (opcode & 0x0F00) >> 8
        y = (opcode & 0x00F0) >> 4
        kk = opcode & 0x00FF

        match (opcode>>12):
            case 0:
                match opcode:
                    case 0x00E0:
                        return self._00E0()
                    case 0x00EE:
                        return self._00EE()
            case 1:
                return self._1nnn(nnn)
            case 2:
                return self._2nnn(nnn)
            case 3:
                return self._3xkk(x, kk)
            case 4:
                return self._4xkk(x, kk)
            case 5:
                return self._5xy0(x, y)
            case 6:
                return self._6xkk(x, kk)
            case 7:
                return self._7xkk(x, kk)
            case 8:
                match (opcode & 0xF):
                    case 0:
                        return self._8xy0(x, y)
                    case 1:
                        return self._8xy1(x, y)
                    case 2:
                        return self._8xy2(x, y)
                    case 3:
                        return self._8xy3(x, y)
                    case 4:
                        return self._8xy4(x, y)
                    case 5:
                        return self._8xy5(x, y)
                    case 6:
                        return self._8xy6(x, y)
                    case 7:
                        return self._8xy7(x, y)
                    case 0xE:
                        return self._8xyE(x, y)
            case 9:
                return self._9xy0(x, y)
            case 0xA:
                return self._Annn(nnn)
            case 0xB:
                return self._Bnnn(nnn)
            case 0xC:
                return self._Cxkk(x, kk)
            case 0xD:
                return self._Dxyn(x, y, opcode & 0xF)
            case 0xE:
                match (opcode & 0xFF):
                    case 0x9E:
                        return self._Ex9E(x)
                    case 0xA1:
                        return self._ExA1(x)
            case 0xF:
                match (opcode & 0xFF):
                    case 0x07:
                        return self._Fx07(x)
                    case 0x0A:
                        return self._Fx0A(x)
                    case 0x15:
                        return self._Fx15(x)
                    case 0x18:
                        return self._Fx18(x)
                    case 0x1E:
                        return self._Fx1E(x)
                    case 0x29:
                        return self._Fx29(x)
                    case 0x33:
                        return self._Fx33(x)
                    case 0x55:
                        return self._Fx55(x)
                    case 0x65:
                        return self._Fx65(x)

            case _:
                return self.unknownOpcode()
    
    def unknownOpcode(self):
        pass
    
    def _00E0(self):
        # Clear the display.
        self.screen.clear()
    
    def _00EE(self):
        # Return from a subroutine.
        self.pc = self.stack.pop()

    def _1nnn(self, nnn):
        # Jump to location nnn.
        self.pc = nnn

    def _2nnn(self, nnn):
        # Call subroutine at nnn.
        self.stack.append(self.pc)
        self.pc = nnn
    
    def _3xkk(self, x, kk):
        # Skip next instruction if Vx = kk.
        if self.vReg[x] == kk:
            self.pc+=2
    
    def _4xkk(self, x, kk):
        # Skip next instruction if Vx != kk.
        if self.vReg[x] != kk:
            self.pc+=2

    def _5xy0(self, x, y):
        # Skip next instruction if Vx = Vy.
        if self.vReg[x] == self.vReg[y]:
            self.pc+=2

    def _6xkk(self, x, kk):
        # Set Vx = kk.
        self.vReg[x] = kk

    def _7xkk(self, x, kk):
        # Set Vx = Vx + kk.
        self.vReg[x] = (self.vReg[x] + kk) % 256
    
    def _8xy0(self, x, y):
        # Set Vx = Vy.
        self.vReg[x] = self.vReg[y]
    
    def _8xy1(self, x, y):
        # Set Vx = Vx OR Vy.
        self.vReg[x] = self.vReg[x] | self.vReg[y]
    
    def _8xy2(self, x, y):
        # Set Vx = Vx AND Vy.
        self.vReg[x] = self.vReg[x] & self.vReg[y]
    
    def _8xy3(self, x, y):
        # Set Vx = Vx XOR Vy.
        self.vReg[x] = self.vReg[x] ^ self.vReg[y]

    def _8xy4(self, x , y):
        # Set Vx = Vx + Vy, set VF = carry.
        sum = self.vReg[x] + self.vReg[y]
        if sum > 255:
            self.vReg[x] = sum-256
            self.vReg[0xF] = 1
        else:
            self.vReg[x] = sum
            self.vReg[0xF] = 0
    
    def _8xy5(self, x, y):
        # Set Vx = Vx - Vy, set VF = NOT borrow.
        if self.vReg[x] < self.vReg[y]:
            self.vReg[x] -= (self.vReg[y]-256)
            self.vReg[0xF] = 0
        else:
            self.vReg[x] -= self.vReg[y]
            self.vReg[0xF] = 1

    def _8xy6(self, x, y):
        # Set Vx = Vx SHR 1.
        lsb = self.vReg[x] & 0x1
        self.vReg[x] >>= 1
        self.vReg[0xF] = lsb
    
    def _8xy7(self, x , y):
        # Set Vx = Vy - Vx, set VF = NOT borrow.
        if self.vReg[x] > self.vReg[y]:
            self.vReg[x] = 256+(self.vReg[y]-self.vReg[x])
            self.vReg[0xF] = 0
        else:
            self.vReg[x] = self.vReg[y] - self.vReg[x]
            self.vReg[0xF] = 1

    def _8xyE(self, x, y):
        # Set Vx = Vx SHL 1.
        msb = (self.vReg[x] & 0x80) >> 7
        self.vReg[x] = (self.vReg[x] << 1) % 256
        self.vReg[0xF] = msb

    def _9xy0(self, x, y):
        # Skip next instruction if Vx != Vy.
        if self.vReg[x] != self.vReg[y]:
            self.pc+=2
            
    def _Annn(self, nnn):
        # Set I = nnn.
        self.index = nnn
    
    def _Bnnn(self, nnn):
        # Jump to location nnn + V0.
        self.pc = nnn + self.vReg[0]

    def _Cxkk(self, x, kk):
        # Set Vx = random byte AND kk.
        self.vReg[x] = randint(0, 255) & kk
    
    def _Dxyn(self, x, y, n):
        # Display n-byte sprite starting at memory location I at (Vx, Vy), set VF = collision.
        self.vReg[0xF] = 0
        for row in range(n):
            sprite = self.memory[self.index+row]
            for col in range(8):
                if (sprite & 0x80):
                    pos = (self.vReg[x]+col, self.vReg[y]+row)
                    if self.screen.isPixel(pos):
                        self.vReg[0xF] = 1
                        self.screen.erasePixel(pos)
                    else:
                        self.screen.drawPixel(pos)
                sprite <<= 1

        pygame.display.update()

    def _Ex9E(self, x):
        # Skip next instruction if key with the value of Vx is pressed.
        if pygame.key.get_pressed()[KEY_MAPPINGS[self.vReg[x]]]:
            self.pc += 2

    def _ExA1(self, x):
        # Skip next instruction if key with the value of Vx is not pressed.
        if not pygame.key.get_pressed()[KEY_MAPPINGS[self.vReg[x]]]:
            self.pc += 2

    def _Fx07(self, x):
        # Set Vx = delay timer value.]
        self.vReg[x] = self.timerDelay
    
    def _Fx0A(self, x):
        # Wait for a key press, store the value of the key in Vx.
        pressed = False
        while not pressed:
            event = pygame.event.wait()
            if event.type == pygame.KEYDOWN:
                keysPressed = pygame.key.get_pressed()
                for val, key in KEY_MAPPINGS.items():
                    if keysPressed[key]:
                        self.vReg[x] = val
                        pressed = True
                        break
    
    def _Fx15(self, x):
        # Set delay timer = Vx.
        self.timerDelay = self.vReg[x]
    
    def _Fx18(self, x):
        # Set sound timer = Vx.
        self.timerSound = self.vReg[x]
    
    def _Fx1E(self, x):
        # Set I = I + Vx.
        self.index += self.vReg[x]
    
    def _Fx29(self, x):
        # Set I = location of sprite for digit Vx.
        self.index = self.vReg[x]*5
    
    def _Fx33(self, x):
        # Store BCD representation of Vx in memory locations I, I+1, and I+2.
        vx = self.vReg[x]
        self.memory[self.index] = vx//100
        self.memory[self.index+1] = (vx//10)%10
        self.memory[self.index+2] = vx%10

    def _Fx55(self, x):
        # Store registers V0 through Vx in memory starting at location I.
        for i in range(self.index, self.index+x+1):
            self.memory[i] = self.vReg[i-self.index]
    
    def _Fx65(self, x):
        # Read registers V0 through Vx from memory starting at location I.
        for i in range(0, x+1):
            self.vReg[i] = self.memory[self.index + i]
    
    def __repr__(self):
        return f"Vx: {self.vReg}\nIndex: {self.index}\nStack: {self.stack}\nPC: {self.pc}"