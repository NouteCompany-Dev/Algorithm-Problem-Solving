N = int(input())

for i in range(N):
  str = input()
  score = 0
  temp = 0
  for j in str:
    if j == 'O':
      temp += 1
      score += temp
    else:
      temp = 0
  print(score)