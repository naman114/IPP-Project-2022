import sys
import pygame
import numpy as np

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
PURPLE= (128,0,128)
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500
INF = 1e5
BLOCKSIZE = 20
SOURCE_ROW = 0
SOURCE_COL = 0
DEST_ROW = 24
DEST_COL = 24
TOTAL_ROWS = WINDOW_HEIGHT//BLOCKSIZE
TOTAL_COLS = WINDOW_WIDTH//BLOCKSIZE
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
blocked_cells = np.zeros((TOTAL_ROWS, TOTAL_COLS), dtype=int)
bomb_cells = np.zeros((TOTAL_ROWS, TOTAL_COLS), dtype=int)
SPEED = 60