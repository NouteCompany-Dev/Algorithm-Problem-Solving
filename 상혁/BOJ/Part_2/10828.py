import sys

n = int(input())

for _ in range(n):
  str = sys.stdin.readline().strip()
  stk = []
  flag = True
  for i in str:
    if i == '(':
      stk.append('(')
    else:
      if len(stk) > 0:
        stk.pop()
      else:
        flag = False
        break
  if len(stk) > 0 : flag = False
  print("YES" if flag else "NO")
