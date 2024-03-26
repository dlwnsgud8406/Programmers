from itertools import combinations
def solution(numbers):
    answer = []
    arr = list(combinations(numbers, 2))
    for i in range(len(arr)):
        answer.append(sum(arr[i]))
    answer = sorted(list(set(answer)))
    return answer
