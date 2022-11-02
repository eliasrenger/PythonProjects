
BOARD_WIDTH = 10
BOARD_HEIGHT = 15
CELL_LENGTH = 15

MENU_HEIGHT = 50
MARGINAL_WIDTH = 10
MARGINAL_HEIGHT = 20
GRID_MARGINAL = 2

RES = (2 * MARGINAL_WIDTH + (CELL_LENGTH + GRID_MARGINAL) * (BOARD_WIDTH + 1) - CELL_LENGTH,
       MENU_HEIGHT + MARGINAL_HEIGHT + (CELL_LENGTH + GRID_MARGINAL) * (BOARD_HEIGHT + 1) - CELL_LENGTH)

TITLE = "Mine Sweeper"

LIGHT_BACKGROUND_CLR = (253, 252, 253)
BACKGROUND_CLR = (185, 185, 185)
DARK_BACKGROUND_CLR = (117, 117, 117)