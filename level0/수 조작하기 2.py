def solution(log):
    answer = ''
    for i in range(len(log) - 1):
        if log[i] - log[i + 1] == -1:
            answer += 'w'
        elif log[i] - log[i + 1] == 1:
            answer += 's'
        elif log[i] - log[i + 1] == 10:
            answer += 'a'
        if log[i] - log[i + 1] == -10:
            answer += 'd'

    return answer
