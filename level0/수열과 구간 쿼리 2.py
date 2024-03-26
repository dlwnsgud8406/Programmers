def solution(arr, queries):
    answer = []
    for q in queries:
        array = []
        for i in range(q[0], q[1]+1):
            if arr[i] > q[2]:
                array.append(arr[i])
        if not len(array):
            answer.append(-1)
        else:
            answer.append(min(array))
    return answer
