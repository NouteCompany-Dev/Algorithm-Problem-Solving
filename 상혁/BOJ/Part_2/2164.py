from collections import deque

n = int(input())

queue = deque([i for i in range(1, n+1)])

ans = 0

while queue:
  num = queue.popleft()
  if not queue: 
    ans = num
    break
  queue.rotate(-1)

print(ans)