from constants import *
from queue import PriorityQueue
from utils import paintCell

def astar():
    pq = PriorityQueue()
    src_f_cost = 0
    src_h_cost = abs(DEST_ROW - SOURCE_ROW) + abs(DEST_COL - SOURCE_COL)
    pq.put((src_f_cost, src_h_cost, SOURCE_ROW, SOURCE_COL))

    distance = np.full((TOTAL_ROWS, TOTAL_COLS), INF)
    distance[SOURCE_ROW][SOURCE_COL] = 0

    visited = np.zeros((TOTAL_ROWS, TOTAL_COLS), dtype=int)

    parent = []
    for i in range(TOTAL_ROWS):
        parentRow = []
        for j in range(TOTAL_COLS):
            parentRow.append([None, None])
        parent.append(parentRow)

    while not pq.empty():
        currentCell = pq.get()
        cur_f_cost = currentCell[0]
        cur_h_cost = currentCell[1]
        row = currentCell[2]
        col = currentCell[3]

        if(visited[row][col]):
            continue

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
                    g_cost = abs(SOURCE_ROW - tx) + abs(SOURCE_COL - ty)
                    dist_to_nbr = g_cost + 1

                    h_cost = abs(DEST_ROW - tx) + abs(DEST_COL - ty)
                    f_cost = g_cost + h_cost
                    
                    if (distance[tx][ty] > dist_to_nbr):
                        pq.put((f_cost, h_cost, tx, ty))
                        distance[tx][ty] = dist_to_nbr
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
