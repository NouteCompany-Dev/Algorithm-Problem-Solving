from collections import deque

n, k = map(int, input().split())

queue = deque([i for i in range(1, n+1)])

ans = []
tmp = 1
idx = 0

while queue:
  if idx >= len(queue): idx = 0
  if tmp == k:
    ans.append(queue[idx])
    del queue[idx]
    tmp  = 1
    continue
  tmp += 1
  idx += 1
  
print('<', end='')
print(', '.join(str(e) for e in ans), end='')
print('>')