def solution(arr):
    answer = []
    i = 0
    while i < len(arr):
        if not len(answer):
            answer.append(arr[i])
        else:
            if answer[len(answer)-1] == arr[i]:
                answer.pop()
            else:
                answer.append(arr[i])
        i+= 1
    if not len(answer):
        return [-1]
    else:
        return answer
