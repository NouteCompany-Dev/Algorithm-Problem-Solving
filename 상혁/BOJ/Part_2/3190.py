from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())

board = [[0] * (n + 1) for _ in range(n + 1)]

k = int(input())

for _ in range(k):
  y, x = map(int, input().split())
  board[y][x] = 1

c = int(input())
info = []

for _ in range(c):
  c, l = (input().split())
  info.append([int(c), l])

def bfs():
  queue = deque([[1, 1]])
  direction = 'R'
  time = 0

  while queue:
    front = queue[-1] 
    
    for item in info:
      if time == item[0]:
        if item[1] == 'L':
          #  왼쪽 90도
          if direction == 'R': direction = 'U'
          elif direction == 'D': direction = 'R'
          elif direction == 'U': direction = 'L'
          else: direction = 'D'
        elif item[1] == 'D':
          # 오른쪽 90도 
          if direction == 'R': direction = 'D'
          elif direction == 'D': direction = 'L'
          elif direction == 'U': direction = 'R'
          else: direction = 'U'
    ny = front[0]
    nx = front[1]

    if direction == 'R': nx +=  1
    elif direction == 'D': ny += 1
    elif direction == 'U': ny -=1
    else: nx -= 1

    time += 1

    if [ny, nx] in queue  or ny <= 0 or nx <= 0 or ny > n or nx > n:
      return time
      
    queue.append([ny, nx])
    if board[ny][nx] == 0:
      queue.popleft()
      continue
    board[ny][nx] = 0

  return time

print(bfs())