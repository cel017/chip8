import pygame


# assigned RAM to the device
MEMORY_TOTAL = 4096

# number of V registers [V0-F]
VX_TOTAL = 16

# instruction delay in secs (loop runs at 60 Hz)
INTERVAL = 1/60

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

# width, height in "pixels" of the virtual device
COLS, ROWS = 64, 32

# colors for the display pixels (chip-8 pixels are on/off)
COLORS = {
    "black": (0, 0, 0),
    "white": (255, 255, 255)
    }