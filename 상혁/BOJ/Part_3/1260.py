from collections import deque

n, m, v = map(int, input().split())

board = [[] for _ in range(n+1)]

visited = [False] * (n+1)

for _ in range(m):
  n1, n2 = map(int, input().split())
  board[n1].append(n2)
  board[n2].append(n1)
  
for i in range(n+1):
  board[i] = sorted(board[i])

def dfs(node):
  print(node, end=' ')
  visited[node] = True
  for i in board[node]:
    if visited[i] == False:
      dfs(i)

def bfs(node):
  queue = deque([])
  queue.append(node)
  visited[node] = True

  while queue:
    node = queue.popleft()
    print(node, end =' ')
    for i in board[node]:
      if visited[i] == False:
        visited[i] = True
        queue.append(i)


dfs(v)
visited = [False] * (n+1)
print()
bfs(v)
