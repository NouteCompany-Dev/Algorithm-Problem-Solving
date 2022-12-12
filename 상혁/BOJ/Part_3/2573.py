import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())

board = []
time = 0

def check(y, x):
    cnt = 0
    for i in range(len(dx)):
        ny = y + dy[i]
        nx = x + dx[i]

        if nx >= 0 and ny >= 0 and nx < m and ny < n and board[ny][nx] == 0:
            cnt +=1
    return cnt

def bfs(y, x, visited):
    q = deque([])

    q.append([y,x])
    visited[y][x] = True

    while q:
        front = q.popleft()
        
        for i in range(len(dx)):
            ny = front[0] + dy[i]
            nx = front[1] + dx[i]

            if nx >= 0 and ny >= 0 and nx < m and ny < n and board[ny][nx] != 0 and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append([ny, nx])
    


for i in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))


while True:
    visited = [[False]* m for _ in range(n)]
    next_board = [[0]* m for _ in range(n)]
    bfs_cnt = 0
    for i in range(n):   
        for j in range(m):
            if board[i][j] != 0 and not visited[i][j]:
                bfs_cnt += 1
                if bfs_cnt == 2:
                    break
                bfs(i,j, visited)
                                    
    if bfs_cnt > 1: break # 덩어리가 2개 이상이면 break
    elif bfs_cnt == 0:
        time = 0
        break
    
    for i in range(n):
        for j in range(m):
            if board[i][j] != 0:
                next_board[i][j] =  max(board[i][j] - check(i, j), 0)
    
    board = next_board
    time += 1

print(time)