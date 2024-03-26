def solution(num, total):
    answer = [0] * num
    mid = total // num
    if len(answer) % 2 == 0:
        idx = len(answer) // 2 - 1
        answer[idx] = mid
    else:
        idx = len(answer) // 2
        answer[idx] = mid

    for i in range(num):
        answer[i] = mid - idx + i
    return sorted(answer)
