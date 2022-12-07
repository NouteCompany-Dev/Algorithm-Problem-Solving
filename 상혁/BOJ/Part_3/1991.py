n = int(input())

# 루트 노드는 A
d = {}

for _ in range(n):
  node, left, right = input().split()
  d[node] = [left, right]


def preorder(node):
  print(node, end='')
  
  info = d[node]

  if info[0] != '.':
    preorder(info[0])
  
  if info[1] != '.':
    preorder(info[1])


def inorder(node):
  info = d[node]

  if info[0] != '.':
    inorder(info[0])
    
  print(node, end='')
    
  if info[1] != '.':
    inorder(info[1])



def postorder(node):
  info = d[node]

  if info[0] != '.':
    postorder(info[0])
  if info[1] != '.':
    postorder(info[1])
  print(node, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')

