# x보다 작은 수

N, X = map(int, input().split())
list = map(int, input().split())

for i in list:
  if i < X: 
    print(i, end=' ')

