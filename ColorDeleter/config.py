# Constants
SIZE: int = 32
FNT_SIZE: int = int(SIZE * .5)
BORDER_W: int = int(SIZE * .1)
DY: int = int(SIZE * 1.5)
ROWS: int = 25
COLS: int = 20
FORMATS: tuple[str, ...] = '.png', '.bmp', '.ico', '.jpeg'

# Window
WND_WIDTH: int = SIZE * COLS
WND_HEIGHT: int = SIZE * ROWS
WND_SIZE: tuple[int, int, int] = WND_WIDTH, WND_HEIGHT
TITLE: str = 'Color killer'
ICO_PATH: str = 'Assets/Turtle.png'

# Style
FNT_PATH: str = 'Assets/SUSE-Bold.ttf'
BORDER: str = f'border: {BORDER_W}px solid black'
NO_SYMB: str = '~`!@#$%^&*()-=+-?\'\"><,№; \t\n'
