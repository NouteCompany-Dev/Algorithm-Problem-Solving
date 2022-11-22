N = int(input())

for i in range(N):
  List = list(map(int, input().split()))
  num = List[0]
  arr = List[1:]
  avg = (sum(arr)) / num
  print("{:.3f}%".format(round(len(list(filter(lambda value : value > avg, arr))) / num * 100, 3)))
  