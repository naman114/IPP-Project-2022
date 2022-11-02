from constants import *
from utils import paintCell

def bfs():
    bfsQueue = []
    bfsQueue.append([SOURCE_ROW, SOURCE_COL])
    distanceFromSrc = []
    finalPath = []
    inf = 100000

    for i in range(TOTAL_ROWS):
        tempRow = []
        for j in range(TOTAL_COLS):
            tempRow.append(inf)
        distanceFromSrc.append(tempRow)
    distanceFromSrc[SOURCE_ROW][SOURCE_COL] = 0

    while len(bfsQueue) != 0:
        currentCell = bfsQueue.pop(0)
        row = currentCell[0]
        col = currentCell[1]

        if (row == DEST_ROW and col == DEST_COL):
            break
        
        if (row != SOURCE_ROW or col != SOURCE_COL):
            paintCell(row, col, BLUE)

        dxy = [-1, 0, 1, 0, -1]

        for i in range(4):
            tx = row + dxy[i]
            ty = col + dxy[i + 1]

            if not(tx < 0 or tx >= TOTAL_ROWS or ty < 0 or ty >= TOTAL_COLS or distanceFromSrc[tx][ty] != inf or BLOCKED_CELLS[tx][ty] == 1):
                bfsQueue.append([tx, ty])
                distanceFromSrc[tx][ty] = distanceFromSrc[row][col] + 1

    if distanceFromSrc[DEST_ROW][DEST_COL] != inf:
        finalPath = [[DEST_ROW, DEST_COL]]
        curX = DEST_ROW
        curY = DEST_COL

        while (curX != SOURCE_ROW or curY != SOURCE_COL):

            for i in range(4):
                tx = curX + dxy[i]
                ty = curY + dxy[i + 1]

                if not(tx < 0 or tx >= TOTAL_ROWS or ty < 0 or ty >= TOTAL_COLS or distanceFromSrc[tx][ty] != distanceFromSrc[curX][curY] - 1 or BLOCKED_CELLS[tx][ty] == 1):
                    finalPath.append([tx, ty])
                    curX = tx
                    curY = ty
                    break

    finalPath.reverse()

    if(len(finalPath) != 0):
        finalPath.pop(0)
        finalPath.pop(-1)
        
    return finalPath
