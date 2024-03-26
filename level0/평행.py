from itertools import permutations
def solution(dots):
    arr = list(permutations(dots, 4))
    for dot in arr:
        if (dot[0][1] - dot[1][1])/(dot[0][0] - dot[1][0]) == (dot[2][1] - dot[3][1]) / (dot[2][0] - dot[3][0]):
            return 1
    return 0
