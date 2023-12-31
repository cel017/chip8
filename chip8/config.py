import pygame


# assigned RAM to the device
MEMORY_TOTAL = 4096

# number of V registers [V0-F]
VX_TOTAL = 16

# instruction delay in secs (~500Hz seems reasonable)
INTERVAL = 1/500

# sound and delay timers (60 Hz)
INTERVAL_SOUND_DELAY = 1/60

# program counter initial offset from memory
PROGRAM_COUNTER_INITIAL = 0x200

'''
chip-8 layout:
1	2	3	C
4	5	6	D
7	8	9	E
A	0	B	F
keyboard map :
1	2	3	4
Q	W	E	R
A	S	D	F
Z	X	C	V

'''
KEY_MAPPINGS = {
    0x1: pygame.K_1,
    0x2: pygame.K_2,
    0x3: pygame.K_3,
    0xC: pygame.K_4,

    0x4: pygame.K_q,
    0x5: pygame.K_w,
    0x6: pygame.K_e,
    0xD: pygame.K_r,

    0x7: pygame.K_a,
    0x8: pygame.K_s,
    0x9: pygame.K_d,
    0xE: pygame.K_f,

    0xA: pygame.K_z,
    0x0: pygame.K_x,
    0xB: pygame.K_c,
    0xF: pygame.K_v,
}

# sprites/font
SPRITES = [
        0xF0, 0x90, 0x90, 0x90, 0xF0, # 0
        0x20, 0x60, 0x20, 0x20, 0x70, # 1
        0xF0, 0x10, 0xF0, 0x80, 0xF0, # 2
        0xF0, 0x10, 0xF0, 0x10, 0xF0, # 3
        0x90, 0x90, 0xF0, 0x10, 0x10, # 4
        0xF0, 0x80, 0xF0, 0x10, 0xF0, # 5
        0xF0, 0x80, 0xF0, 0x90, 0xF0, # 6
        0xF0, 0x10, 0x20, 0x40, 0x40, # 7
        0xF0, 0x90, 0xF0, 0x90, 0xF0, # 8
        0xF0, 0x90, 0xF0, 0x10, 0xF0, # 9
        0xF0, 0x90, 0xF0, 0x90, 0x90, # A
        0xE0, 0x90, 0xE0, 0x90, 0xE0, # B
        0xF0, 0x80, 0x80, 0x80, 0xF0, # C
        0xE0, 0x90, 0x90, 0x90, 0xE0, # D
        0xF0, 0x80, 0xF0, 0x80, 0xF0, # E
        0xF0, 0x80, 0xF0, 0x80, 0x80  # F
        ]

# width, height in "pixels" of the virtual device
COLS, ROWS = 64, 32

# colors for the display pixels (chip-8 pixels are on/off)
COLORS = {
    "black": (0, 0, 0),
    "white": (255, 255, 255)
    }