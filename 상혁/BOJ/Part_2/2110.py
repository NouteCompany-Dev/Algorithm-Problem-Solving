n, c = map(int, input().split())

arr = []
ans = 0

for _ in range(n):
  arr.append(int(input()))

def binary():
  global ans
  left = 0
  right = max(arr)
  while left < right:
    mid = (left + right) // 2
    next_idx = 0    
    cnt = 1
    for i in range(len(arr)):
      if i == next_idx:
        for j in range(i+1, len(arr)):
          if arr[j] - arr[i] >= mid:
            cnt += 1
            next_idx = j
            break

    if cnt >= c:
      left = mid +1
      ans = mid
      continue
    right = mid


arr.sort()
binary()
print(ans)