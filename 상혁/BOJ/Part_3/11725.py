import sys
from collections import deque
 
n = int(input())

parent = [i for i in range(n+1)]
arr = [[] for i in range(n+1)]
queue = deque([])
visited = [False] * (n+1)

for _ in range(n-1):
  a, b = map(int, sys.stdin.readline().strip().split())
  arr[a].append(b)
  arr[b].append(a)

visited[1] = True
for i in range(len(arr[1])):
  queue.append(arr[1][i])
  parent[arr[1][i]] = 1
  
while queue:
  front = queue.popleft()
  if visited[front] : continue
  visited[front] = True
  for i in range(len(arr[front])):
    node = arr[front][i]
    if not visited[node]:
      parent[node] = front
      queue.append(node)

for i in range(2, len(parent)):
  print(parent[i])
