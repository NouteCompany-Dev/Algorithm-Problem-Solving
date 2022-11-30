import sys

n = int(input())

arr = list(map(int, input().split()))
stk = []
ans = [0] * n

for i in range(n):
  while stk:
    if stk[-1][1] > arr[i]:
      ans[i] = stk[-1][0] +1
      break
    else:
      stk.pop()
  stk.append([i, arr[i]])

print(*ans)
