N = int(input())
ans = 0
list = [0] * N

def check(num):
  for i in range(num):
    if list[i] == list[num] or abs(list[i] - list[num]) == abs(i-num): 
      return False
      
  return True

def solution(num):
  global ans
  if num == N: 
    ans += 1
    return
  
  for i in range(N):
      list[num] = i
      if check(num): 
        solution(num + 1)

solution(0)
print(ans)