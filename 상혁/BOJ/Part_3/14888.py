from itertools import permutations

n = int(input())

arr = list(map(int, input().split()))

opers = list(map(int, input().split()))
permute = []

for i in range(opers[0]):
  permute.append('+')
for i in range(opers[1]):
  permute.append('-')
for i in range(opers[2]):
  permute.append('*')
for i in range(opers[3]):
  permute.append('/')


mx = -1_000_000_001
mn = 1_000_000_001


permute = set(permutations(permute))


for p in permute:
  temp = arr[0]
  for i in range(len(p)):
    if p[i] == '+':
      temp += arr[i+1]
    elif p[i] == '-':
      temp -= arr[i+1]
    elif p[i] == '*':
      temp *= arr[i+1]
    elif p[i] == '/': 
      temp = int(temp / arr[i+1])
  mx = max(mx, temp)
  mn = min(mn, temp)

print(mx)
print(mn)