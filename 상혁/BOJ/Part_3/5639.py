import sys

arr = []
sys.setrecursionlimit(10**4)


def search(idx, value):
  if idx > len(arr):
    arr.append([value, [0,0], [0,0]])
    return
  elif arr[idx][0] > value: #left
    if arr[idx][1][1] == 0: # left node 없음
      arr[idx][1] = [len(arr), value]
      arr.append([value, [0,0], [0,0]])
      return
    search(arr[idx][1][0], value)
  elif value > arr[idx][0]: #right
    if arr[idx][2][1] == 0:
      arr[idx][2] = [len(arr), value]
      arr.append([value, [0,0], [0,0]])
      return
    search(arr[idx][2][0], value)

for i in sys.stdin:
  num = int(i)
  if len(arr) == 0:
    arr.append([num, [0,0], [0,0]]) # [node, [left_idx, left_value], [right_idx, right_value]]
    continue
  
  search(0, num)
  
def postorder(idx):
  if arr[idx][1][0] != 0:
    postorder(arr[idx][1][0])
  
  if(arr[idx][2][0] != 0):
    postorder(arr[idx][2][0])
  print(arr[idx][0])

postorder(0)