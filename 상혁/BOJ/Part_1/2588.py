a = int(input())
b = int(input())

for i in str(b)[::-1]:
  print(int(i) * a)

print(a*b)