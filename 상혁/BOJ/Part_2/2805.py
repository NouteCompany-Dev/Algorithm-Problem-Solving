def binary():
  global ans
  left = 0
  right = max(arr)
  while left < right:
    mid = (left + right) // 2
    temp = 0
    for item in arr:
        temp += (item - mid) if item > mid else 0
    if temp >= m:
      left = mid + 1
      ans = mid
    else:
      right = mid
      
n, m = map(int, input().split())

arr = list(map(int, input().split()))
ans = 0

binary()

print(ans)