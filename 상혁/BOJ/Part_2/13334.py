import sys
import heapq

n = int(input())

arr = []
heap = []
ans = 0

for _ in range(n):
  h, o = sys.stdin.readline().strip().split()
  mx, mn = [h, o] if int(h) > int(o) else [o, h]
  arr.append([int(mn), int(mx)])

d = int(input())

arr = sorted(arr, key = lambda item : int(item[1]))

idx = 0

while idx < n:
  if arr[idx][1] - arr[idx][0] > d:
    idx += 1
    continue
  
  while len(heap) > 0 and arr[idx][1] - heap[0][0] > d:
    heapq.heappop(heap)
  heapq.heappush(heap, (arr[idx][0], arr[idx][1]))

  if len(heap) > ans: ans = len(heap)
  idx += 1


print(ans)