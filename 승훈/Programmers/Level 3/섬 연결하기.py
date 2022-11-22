def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x : x[2])
    start = set([costs[0][0]])

    while len(start) != n:
        for i in costs:
            if i[0] in start and i[1] in start:
                continue
            if i[0] in start or i[1] in start:
                start.update([i[0], i[1]])
                answer += i[2]
                break
    
    return answer