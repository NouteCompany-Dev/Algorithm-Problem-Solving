def Factorial(num):
  if num == 0: return 1
  return num * Factorial(num-1)

N = int(input())
print(Factorial(N))