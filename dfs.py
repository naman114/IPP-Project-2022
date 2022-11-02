from constants import *
from utils import paintCell

distanceFromSrc = []
flag = False
dxy = [-1, 0, 1, 0, -1]


def pathFinder(row, col, dist):
    global distanceFromSrc, flag
    if (row == DEST_ROW and col == DEST_COL):
        distanceFromSrc[row][col] = dist
        flag = True
        return

    distanceFromSrc[row][col] = dist

    if (row != SOURCE_ROW or col != SOURCE_COL):
        paintCell(row, col, BLUE)

    for i in range(4):
        x = row + dxy[i]
        y = col + dxy[i+1]
        if not(x < 0 or y < 0 or x >= TOTAL_ROWS or y >= TOTAL_COLS or blocked_cells[x][y] == 1 or flag == True or distanceFromSrc[x][y] != INF):
            pathFinder(x, y, dist + 1)


def dfs():
    finalPath = []
    for i in range(TOTAL_ROWS):
        tempRow = []
        for j in range(TOTAL_COLS):
            tempRow.append(INF)
        distanceFromSrc.append(tempRow)
    distanceFromSrc[SOURCE_ROW][SOURCE_COL] = 0

    pathFinder(SOURCE_ROW, SOURCE_COL, 0)

    if flag:
        currX = DEST_ROW
        currY = DEST_COL
        finalPath.append([currX, currY])
        while (currX != SOURCE_ROW or currY != SOURCE_COL):

            for i in range(4):
                tx = currX + dxy[i]
                ty = currY + dxy[i + 1]

                if not(tx < 0 or tx >= TOTAL_ROWS or ty < 0 or ty >= TOTAL_COLS or distanceFromSrc[tx][ty] != distanceFromSrc[currX][currY] - 1 or blocked_cells[tx][ty] == 1):
                    finalPath.append([tx, ty])
                    currX = tx
                    currY = ty
                    break

        finalPath.reverse()
    
    
    if(len(finalPath) != 0):
        finalPath.pop(0)
        finalPath.pop(-1)
        
    return finalPath
