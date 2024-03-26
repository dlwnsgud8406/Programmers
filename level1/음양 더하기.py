def solution(absolutes, signs):
    answer = 0
    mul = 0
    for i in range(len(absolutes)):
        if signs[i]:
            mul = 1
        elif not signs[i]:
            mul = -1
        answer += (mul * absolutes[i])

    return answer
