import sys

v, e = map(int, input().split())

arr = []

for _ in range(e):
  start, end, weight = map(int, sys.stdin.readline().strip().split())
  arr.append([start,end, weight])  

arr = sorted(arr, key= lambda item : item[2])
ans = 0

parent = [i for i in range(v+1)]

def find(node):
  if node != parent[node]:
    parent[node] = find(parent[node])
  return parent[node]

def union(a,b):
  aParent = find(a)
  bParent = find(b)
  if aParent > bParent: parent[aParent]= bParent
  else: parent[bParent]= aParent

for i in range(len(arr)):
  node_1, node_2, weight = arr[i] # node -1 해줘야함
  if find(node_1) ==find(node_2): continue
  union(node_1, node_2)
  ans += weight  

print(ans)
