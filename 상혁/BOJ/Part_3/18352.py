from collections import deque

n, m, k, x = map(int, input().split())

arr = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    node_1, node_2 = map(int, input().split())
    arr[node_1].append(node_2)

q = deque([])
q.append([x, 0]) # start, cnt
visited[x] = True

ans = []

while q:
    front = q.popleft()
    node = front[0]
    distance = front[1]
    if distance == k:
        ans.append(node)
        continue
    elif distance > k:
        continue

    for i in arr[node]:
        if not visited[i]:
            visited[i] = True
            q.append([i, distance+1])

if len(ans) == 0 : print(-1)
else:
    ans = sorted(ans)
    for i in ans:
        print(i)
