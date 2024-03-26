def solution(emergency):
    answer = [0] * len(emergency)
    count = 1
    while max(emergency) != 0:
        index = emergency.index(max(emergency))
        answer[index] = count
        emergency[index] = 0
        count += 1
    return answer
