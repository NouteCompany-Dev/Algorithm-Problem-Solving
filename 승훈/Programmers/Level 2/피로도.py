answer = 0

def dfs(k, cnt, dg):
    global answer
    
    if cnt > answer:
        answer = cnt
        
    for i in range(n):
        if k >= dg[i][0] and not chk[i]:
            chk[i] = 1
            dfs(k - dg[i][1], cnt + 1, dg)
            chk[i] = 0
        
def solution(k, dungeons):
    global n, chk
    
    n = len(dungeons)
    chk = [0] * n
    dfs(k, 0, dungeons)
    
    return answer