from itertools import combinations

arr = [] 

for _ in range(9):
  arr.append(int(input()))

for i in list(combinations(arr, 7)):
  if sum(i) == 100:
    for num in sorted(i):
      print(num)
    break