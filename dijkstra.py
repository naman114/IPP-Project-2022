from constants import *
from queue import PriorityQueue
from utils import paintCell

def dijkstra():
    pq = PriorityQueue()
    pq.put((0, SOURCE_ROW, SOURCE_COL))

    distance = np.full((TOTAL_ROWS, TOTAL_COLS), INF)
    distance[SOURCE_ROW][SOURCE_COL] = 0

    visited = np.zeros((TOTAL_ROWS, TOTAL_COLS), dtype=int)
    visited[SOURCE_ROW][SOURCE_COL] = 1

    parent = []
    for i in range(TOTAL_ROWS):
        parentRow = []
        for j in range(TOTAL_COLS):
            parentRow.append([None, None])
        parent.append(parentRow)

    while not pq.empty():
        currentCell = pq.get()
        weight = currentCell[0]
        row = currentCell[1]
        col = currentCell[2]
        visited[row][col] = 1

        if(row == DEST_ROW and col == DEST_COL):
            break
        
        if (row != SOURCE_ROW or col != SOURCE_COL):
            if not BOMB_CELLS[row][col]:
                paintCell(row, col, BLUE)

        dxy = [-1, 0, 1, 0, -1]

        for i in range(4):
            tx = row + dxy[i]
            ty = col + dxy[i + 1]

            if(not(tx < 0 or tx >= TOTAL_ROWS or ty < 0 or ty >= TOTAL_COLS or visited[tx][ty] or BLOCKED_CELLS[tx][ty])):
                    targetCellWeight = 1
                    if BOMB_CELLS[tx][ty]:
                        targetCellWeight = 10
                    
                    if (distance[tx][ty] > distance[row][col] + targetCellWeight):
                        pq.put((weight + targetCellWeight, tx, ty))
                        distance[tx][ty] = distance[row][col] + targetCellWeight
                        parent[tx][ty] = [row, col]
    
    finalPath = []

    if(parent[DEST_ROW][DEST_COL] != None):
        curX = DEST_ROW
        curY = DEST_COL

        while(curX != SOURCE_ROW or curY != SOURCE_COL):
            a = parent[curX][curY][0]
            b = parent[curX][curY][1]

            curX = a
            curY = b

            finalPath.append([curX, curY])
        
     
    if(len(finalPath) != 0):
        finalPath.pop(-1)
    
    finalPath.reverse()
    return finalPath