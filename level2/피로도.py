from itertools import permutations
def solution(k, dungeons):
    answer = 0
    arr = list(permutations(dungeons))
    for route in arr:
        how = 0
        energy = k
        for i in range(len(route)):
            if energy >= route[i][0]:
                energy -= route[i][1]
                how += 1
        answer = max(answer, how)
    return answer
