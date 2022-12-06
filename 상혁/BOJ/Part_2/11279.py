import sys
import heapq

n = int(input())
heap = []

for _ in range(n):
  num = int(sys.stdin.readline())
  if num == 0:
    print(0 if len(heap) == 0 else heapq.heappop(heap)[1])
    continue
  heapq.heappush(heap, (-num, num))
