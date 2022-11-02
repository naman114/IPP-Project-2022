from constants import *
from bfs import bfs
from dfs import dfs
from dijkstra import dijkstra
from astar import astar


def scaleUp(side):
    return BLOCKSIZE*side


def scaleDown(side):
    return side//BLOCKSIZE


def createScaledRect(x, y, color):
    rect = pygame.Rect(scaleUp(x),
                       scaleUp(y), BLOCKSIZE, BLOCKSIZE)
    pygame.draw.rect(SCREEN, color, rect)


def createPath(path):
    if len(path) == 0:
        return

    for cell in path:
        createScaledRect(cell[0], cell[1], YELLOW)
        pygame.display.update()
        pygame.time.Clock().tick(60)


def drawGrid():
    for x in range(0, WINDOW_WIDTH, BLOCKSIZE):
        for y in range(0, WINDOW_HEIGHT, BLOCKSIZE):
            rect = pygame.Rect(x, y, BLOCKSIZE, BLOCKSIZE)
            pygame.draw.rect(SCREEN, BLACK, rect, 1)

def main():
    pygame.init()
    SCREEN.fill(WHITE)
    pygame.display.set_caption("PathFinder")

    while True:
        print("Running")
        drawGrid()
        createScaledRect(SOURCE_ROW, SOURCE_COL, GREEN)
        createScaledRect(DEST_ROW, DEST_COL, RED)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x = int(pygame.mouse.get_pos()[0] / BLOCKSIZE) * BLOCKSIZE
                y = int(pygame.mouse.get_pos()[1] / BLOCKSIZE) * BLOCKSIZE

                if pygame.mouse.get_pressed()[0]:
                    pygame.draw.rect(
                        SCREEN, BLACK, (x, y, BLOCKSIZE, BLOCKSIZE), 0)
                    BLOCKED_CELLS[scaleDown(x)][scaleDown(y)] = 1
                    BOMB_CELLS[scaleDown(x)][scaleDown(y)] = 0
                elif pygame.mouse.get_pressed()[2]:
                    pygame.draw.rect(
                        SCREEN, PURPLE, (x, y, BLOCKSIZE, BLOCKSIZE), 0)
                    BLOCKED_CELLS[scaleDown(x)][scaleDown(y)] = 0
                    BOMB_CELLS[scaleDown(x)][scaleDown(y)] = 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    path = bfs()
                elif event.key == pygame.K_b:
                    path = dfs()
                elif event.key == pygame.K_c:
                    path = dijkstra()
                elif event.key == pygame.K_d:
                    path = astar()
                else:
                    pygame.quit()
                    sys.exit()

                createPath(path)

            pygame.display.update()


if __name__ == "__main__":
    main()
