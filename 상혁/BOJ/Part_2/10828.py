import sys

n = int(input())

stk = []

for _ in range(n):
  str = sys.stdin.readline().strip()
  if 'push' in str:
    stk.append(int(str.split(' ')[1]))
  elif str == 'top':
    print(-1 if len(stk) == 0 else stk[-1])
  elif str == 'size':
    print(len(stk))
  elif str == 'pop':
    print(stk.pop()) if len(stk) > 0 else print(-1)
  else:
    print(1 if len(stk) == 0 else 0)
  

