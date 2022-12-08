from collections import deque

def bfs(m, tree, chk, wire, cnt):
    queue = deque()
    queue.append([m, tree, chk, wire])
    chk[m] = True

    while queue:
        m, tree, chk, wire = queue.popleft()
        cnt += 1

        for i in tree[m]:
            if not ((m == wire[0] and i == wire[1]) or (m == wire[1] and i == wire[0])):
                if not chk[i]:
                    chk[i] = True
                    queue.append([i, tree, chk, wire])
                    
    return cnt

def solution(n, wires):
    answer = 1e9
    tree = [[] for _ in range(n + 1)]

    for i in wires:
        a, b = i
        tree[a].append(b)
        tree[b].append(a)

    for i in wires:
        chk = [False] * (n + 1)
        data = []

        for j in range(1, n + 1):
            if not chk[j]:
                cnt = bfs(j, tree, chk, i, 0)
                data.append(cnt)

        answer = min(answer, abs(data[0] - data[1]))
        
    return answer