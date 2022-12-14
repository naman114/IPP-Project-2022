from constants import *
from utils import *
from bfs import bfs
from dfs import dfs
from dijkstra import dijkstra
from astar import astar

def main():
    pygame.init()
    SCREEN.fill(WHITE)
    pygame.display.set_caption("PathFinder")

    while True:
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
                    blocked_cells[scaleDown(x)][scaleDown(y)] = 1
                    bomb_cells[scaleDown(x)][scaleDown(y)] = 0
                elif pygame.mouse.get_pressed()[2]:
                    pygame.draw.rect(
                        SCREEN, PURPLE, (x, y, BLOCKSIZE, BLOCKSIZE), 0)
                    blocked_cells[scaleDown(x)][scaleDown(y)] = 0
                    bomb_cells[scaleDown(x)][scaleDown(y)] = 1

            if event.type == pygame.KEYDOWN:
                path = []
                if event.key == pygame.K_a:
                    path = bfs()
                    print(blocked_cells)
                elif event.key == pygame.K_b:
                    path = dfs()
                elif event.key == pygame.K_c:
                    path = dijkstra()
                elif event.key == pygame.K_d:
                    path = astar()
                elif event.key == pygame.K_r:
                    SCREEN.fill(WHITE)
                    drawGrid()
                    createScaledRect(SOURCE_ROW, SOURCE_COL, GREEN)
                    createScaledRect(DEST_ROW, DEST_COL, RED)
                    blocked_cells.fill(0)
                    bomb_cells.fill(0)
                else:
                    pygame.quit()
                    sys.exit()

                createPath(path)

            pygame.display.update()


if __name__ == "__main__":
    main()
