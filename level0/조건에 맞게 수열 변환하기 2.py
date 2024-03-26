def solution(arr):
    answer = 0
    while 1:
        temp = []
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                temp.append(arr[i] // 2)
            elif arr[i] < 50 and arr[i] % 2 == 1:
                temp.append(arr[i] * 2 + 1)
            else:
                temp.append(arr[i])
        answer += 1
        if sorted(temp) == sorted(arr):
            return answer-1
        arr = temp
