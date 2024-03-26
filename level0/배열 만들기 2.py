def solution(l, r):
    answer = []
    arr1=[[0], [5], [5, 0], [0, 5]]
    for i in range(l, r+1):
        arr = list(map(int, list(set(list(str(i))))))
        if arr in arr1:
            answer.append(i)
    if not len(answer):
        return [-1]
    else:
        return answer
