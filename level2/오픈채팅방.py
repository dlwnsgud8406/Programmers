def solution(record):
    uid_answer = []
    answer = []
    hash_map = {}
    for rec in record:
        arr = rec.split(' ')
        if arr[0] == 'Enter':
            hash_map[arr[1]] = arr[2]
            uid_answer.append(arr[1] + ' Enter')
        elif arr[0] == 'Leave':
            uid_answer.append(arr[1] + ' Leave')
        elif arr[0] == 'Change':
            hash_map[arr[1]] = arr[2]
    for uid in uid_answer:
        uid, command = uid.split(' ')
        if command == 'Enter':
            answer.append(hash_map[uid] + "님이 들어왔습니다.")
        elif command == 'Leave':
            answer.append(hash_map[uid] + "님이 나갔습니다.")

    return answer
# 초고속 풀이법
def solution(record):
    answer = []
    dict = {}
    for log in record:
        command = log.split(' ')
        if 'Enter' in log:
            answer.append([command[1], "님이 들어왔습니다."])
            dict[command[1]] = command[2]
        elif 'Leave' in log:
            answer.append([command[1], "님이 나갔습니다."])
        else:
            dict[command[1]] = command[2]
    return(list(map(lambda x : dict[x[0]]+x[1], answer)))
