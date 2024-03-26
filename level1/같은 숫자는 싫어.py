def solution(arr):
    answer = []
    for num in arr:
        if len(answer) == 0:
            answer.append(num)
        if num != answer[-1]:
            answer.append(num)
    return answer

def solution(arr):
    answer = []
    standard = 10
    for num in arr:
        if standard == num:
            pass
        else:
            standard = num
            answer.append(num)
    return answer
