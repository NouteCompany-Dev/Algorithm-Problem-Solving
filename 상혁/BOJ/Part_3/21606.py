import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


n = int(input())
inside = input().rstrip()

arr = [[] for _ in range(n)]
ans = 0
visited = [False] * (n)

for _ in range(n-1):
  node_1, node_2 = map(int, input().split())
  arr[node_1 - 1].append(node_2 - 1)
  arr[node_2 - 1].append(node_1 - 1)

def dfs(node):
  res = 0
  visited[node] = True
  for i in arr[node]:
    if not visited[i]:
      if inside[i] == '1':
        res += 1
      else:
        res += dfs(i) 
  return res

for i in range(n):
  # 0 1 2 3 4
  if inside[i] == '1': # 실내인 경우, 산책 시작 가능
    for j in arr[i]:
      ans +=  inside[j] == '1' # 실내 <=> 실내 (중간에 실외 없음)
  else:
    if visited[i]:continue
    cnt = dfs(i)
    ans += cnt * (cnt -1)

print(ans)
