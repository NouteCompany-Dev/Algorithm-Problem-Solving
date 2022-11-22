from itertools import permutations

n = int(input())
ans = 0

arr = list(map(int, input().split()))

for item in permutations(arr):
  temp = 0
  for i in range(len(item)-1):
    temp += abs(item[i] - item[i+1])
  if temp > ans:
    ans = temp

print(ans)