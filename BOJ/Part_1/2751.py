n = int(input())

arr = []

for _ in range(n):
  num = int(input())
  arr.append(num)

l = sorted(arr)

for i in l:
  print(i)