import math

def isPrime(num):
  if num == 1: return False
  sqrtNum = int(math.sqrt(num))+1
  for i in range(2, sqrtNum):
    if num % i == 0: return False
  return True


N = int(input())
L = list(map(int, input().split()))
ans = 0

for i in L:
  if isPrime(i): ans+=1

print(ans)
