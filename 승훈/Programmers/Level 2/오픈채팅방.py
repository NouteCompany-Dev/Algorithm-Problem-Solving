def solution(record):
    answer = []
    users = {}
    data = []
    
    for i in record:
        dp = i.split(" ")
        uid = dp[1]
        
        if dp[0] == 'Enter':
            data.append((uid, 'Enter'))
            users[uid] = dp[2]
        
        elif dp[0] == 'Leave':
            data.append((uid, 'Leave'))
            
        else:
            data.append((uid, 'Change'))
            users[uid] = dp[2]
            
    for i in data:
        if i[1] == 'Enter':
            answer.append(users[i[0]] + "님이 들어왔습니다.")
            
        elif i[1] ==  'Leave':
            answer.append(users[i[0]] + "님이 나갔습니다.")

    return answer