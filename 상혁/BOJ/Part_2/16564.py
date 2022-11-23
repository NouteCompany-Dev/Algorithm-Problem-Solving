n, k = map(int, input().split())
arr = []
ans = 0
for _ in range(n):
  arr.append(int(input()))

arr.sort()

def binary():
  global ans
  left = 1
  right = arr[-1] + k
  while left <= right:
    mid = (left + right) // 2
    temp = 0
    for i in arr:
      if mid >= i:
        temp += (mid - i)
      else: break
    if temp <= k:
      left = mid + 1
      ans = mid
      continue
    right = mid - 1

binary()
print(ans)