# CHIP8
A standard Chip-8 Emulator written in Python. CPU cycles at 500Hz.

# Dependencies
To run the emulator you will need:
-  ≥ Python 3.6
-  ≥ pygame 2.1.2
-  ≥ numpy 1.22.2
```
pip install numpy pygame
```

# Usage
Run the emulator:
-  Navigate to project root
```
cd path/to/root/folder
```
-  Load a rom into the emulator
```
python chip8/main.py path/to/rom
```

# Controls

Chip-8 Layout:

| 1    | 2    | 3    | 4    |
|------|------|------|------|
| 4    | 5    | 6    | D    |
| 7    | 8    | 9    | E    |
| A    | 0    | B    | F    |


Keyboard Mapping:
| 1    | 2    | 3    | 4    |
|------|------|------|------|
| Q    | W    | E    | R    |
| A    | S    | D    | F    |
| Z    | X    | C    | V    |
