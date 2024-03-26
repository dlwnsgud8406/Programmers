def solution(arr, k):
    answer = []
    index = 0
    while len(answer) != k:
        try:
            if arr[index] not in answer:
                answer.append(arr[index])
        except IndexError:
            answer.append(-1)
        index += 1
    return answer
