from itertools import combinations
def solution(numbers):
    arr = list(combinations(numbers, 2))
    answer = []
    for i in range(len(arr)):
        answer.append(arr[i][0] * arr[i][1])
    return max(answer)
