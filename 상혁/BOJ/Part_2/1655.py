import sys
import heapq
n = int(sys.stdin.readline().replace("\n", ""))

min_heap = []
max_heap = []

for _ in range(n):
  num =  int(sys.stdin.readline().replace("\n", ""))


  if len(max_heap) == len(min_heap):
    heapq.heappush(max_heap, (-num, num))
  else:
    heapq.heappush(min_heap, num)

  if len(max_heap) > 0 and len(min_heap) > 0 and max_heap[0][1] > min_heap[0]:
    mx = heapq.heappop(max_heap)[1]
    mn = heapq.heappop(min_heap)  
    heapq.heappush(max_heap, (-mn, mn))
    heapq.heappush(min_heap, mx)
      
  print(max_heap[0][1])