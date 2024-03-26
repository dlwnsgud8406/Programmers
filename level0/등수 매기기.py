def solution(score):
    answer = []
    arr = []
    for student in score:
        arr.append(sum(student))
    sorted_arr = sorted(arr, reverse=True)

    for i in arr:
        answer.append(sorted_arr.index(i) + 1)
    return answer
