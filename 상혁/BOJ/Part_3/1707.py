import sys
from collections import deque

k = int(input())

def bfs(node, arr, visited):

  q = deque([])

  q.append([node, 1])

  while q:
    front = q.popleft()
    nNode = front[0]
    color = front[1]
    visited[nNode] = color
    for i in range(len(arr[nNode])):
      if visited[arr[nNode][i]] == 0:
        if color == 1:
          q.append([arr[nNode][i], 2])
        else:
          q.append([arr[nNode][i], 1])

for _ in range(k):
  v, e = map(int, input().split())
  arr = [[] for _ in range(v+1)]
  visited = [0] * (v+1)
  for _ in range(e):
    node_1, node_2 = map(int, sys.stdin.readline().strip().split())
    arr[node_1].append(node_2)
    arr[node_2].append(node_1)
  
  for i in range(1, v+1):
    if visited[i] == 0:
      bfs(i, arr, visited)
      
  flag = True
  for i in range(1, v+1):
    for j in range(len(arr[i])):
      if visited[i] == visited[arr[i][j]]:
        flag = False
        break
  print("YES" if flag else "NO")
  
