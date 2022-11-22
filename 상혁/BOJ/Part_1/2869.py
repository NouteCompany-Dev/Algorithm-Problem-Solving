
A, B, V = map(int, input().split())


if A >= V:
  print(1)
else: 
  mod = 1 if (V-A) // (A-B) == 0  else ((V-A) // (A-B)) if (V-A) % (A-B) == 0 else ((V-A) // (A-B)) +1
  print( mod + 1)
