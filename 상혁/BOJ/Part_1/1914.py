process = []

def hanoi(num, from_idx, to_idx, temp):
  global process
  
  if num == 1:
    process.append([from_idx, to_idx])
    return
  hanoi(num - 1, from_idx, temp, to_idx) 
  process.append([from_idx, to_idx])
  hanoi(num - 1, temp, to_idx, from_idx)


N = int(input())


print(2**N -1)

if N <= 20:
  hanoi(N, 1, 3, 2);
  for i in process:
    print(i[0], i[1])