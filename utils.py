from constants import *

def scaleUp(side):
    return BLOCKSIZE*side


def scaleDown(side):
    return side//BLOCKSIZE


def createScaledRect(x, y, color):
    rect = pygame.Rect(scaleUp(x),
                       scaleUp(y), BLOCKSIZE, BLOCKSIZE)
    pygame.draw.rect(SCREEN, color, rect)

def paintCell(x, y, color):
    createScaledRect(x, y, color)
    pygame.display.update()
    pygame.time.Clock().tick(SPEED)

def createPath(path):
    if len(path) == 0:
        return

    for cell in path:
        paintCell(cell[0], cell[1], YELLOW)


def drawGrid():
    for x in range(0, WINDOW_WIDTH, BLOCKSIZE):
        for y in range(0, WINDOW_HEIGHT, BLOCKSIZE):
            rect = pygame.Rect(x, y, BLOCKSIZE, BLOCKSIZE)
            pygame.draw.rect(SCREEN, BLACK, rect, 1)