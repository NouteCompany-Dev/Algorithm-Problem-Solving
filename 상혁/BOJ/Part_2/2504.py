import sys

str = sys.stdin.readline().strip()

stk = []
temp = 1
ans = 0

for i in range(len(str)):
  if str[i] == '(':
    stk.append('(')
    temp *= 2
  elif str[i] == '[':
    stk.append('[')
    temp *= 3
  elif str[i] == ')':
    if not stk or stk[-1] == '[':
      ans = 0
      break
    stk.pop()
    ans += temp if str[i-1] == '(' else 0
    temp //= 2
  else:
    if not stk or stk[-1] == '(':
      ans = 0
      break
    stk.pop()
    ans += temp if str[i-1] == '[' else 0
    temp //= 3
  
print(ans if not stk else 0)