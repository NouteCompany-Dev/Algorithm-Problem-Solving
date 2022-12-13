from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input())))

q = deque([])
visited = [[False] * m for _ in range(n)]

q.append([0,0,1]) # y, x, cnt
visited[0][0] = True
ans = 0

while q:
    front = q.popleft()

    if front[0] == n-1 and front[1] == m-1:
        ans = front[2]
        break

    for i in range(4):
        ny = front[0] + dy[i]
        nx = front[1] + dx[i]
        cnt = front[2] + 1
        if ny >= 0 and nx >= 0 and ny < n and nx < m and not visited[ny][nx] and board[ny][nx] == 1:
            visited[ny][nx] = 1
            q.append([ny,nx,cnt])

print(ans)