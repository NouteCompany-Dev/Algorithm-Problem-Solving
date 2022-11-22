import sys

n = int(sys.stdin.readline())

arr = [0] * n

for i in range(n):
  arr[i] = str(sys.stdin.readline().strip())

for i in list(dict.fromkeys(sorted(sorted(arr), key=len))):
  print(i)
