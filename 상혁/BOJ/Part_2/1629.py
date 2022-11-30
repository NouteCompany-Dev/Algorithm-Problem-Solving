a, b, c = map(int, input().split())

def divideAndConquer(target, mul):
    if mul == 1:
      return target % c
    
    temp = divideAndConquer(target, mul // 2)

    if mul % 2 == 0:
      return temp * temp % c
    else:
      return temp * temp * a % c

print(divideAndConquer(a, b))
