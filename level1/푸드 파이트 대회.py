def solution(food):
    string1 = ''
    for i in range(len(food)):
        num = food[i] // 2
        for j in range(num):
            string1 += str(i)
    answer = string1 + '0' + string1[::-1]

    return answer
