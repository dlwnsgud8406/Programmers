def solution(want, number, discount):
    answer = 0
    wanted_number = []
    for i in range(len(want)):
        for j in range(number[i]):
            wanted_number.append(want[i])
    for i in range(len(discount)-9):
        if sorted(wanted_number) == sorted(discount[i:i+10]):
            answer += 1
    return answer
