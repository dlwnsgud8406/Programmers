from itertools import permutations


def solution(ability):
    answer = 0
    students = len(ability)
    sports = len(ability[0])
    arr = permutations([i for i in range(students)], sports)

    for i in arr:
        temp = 0
        idx = 0
        for j in i:
            temp += ability[j][idx]
            idx += 1
        answer = max(answer, temp)

    return answer
