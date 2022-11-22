import sys

n = int(sys.stdin.readline())

arr = [0] * (10001)

for _ in range(n):
  arr[int(sys.stdin.readline())] += 1

for i in range(len(arr)):
  num = arr[i];
  if num != 0:
    for _ in range(num):
      print(i)