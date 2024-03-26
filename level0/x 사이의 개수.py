def solution(myString):
    answer = []
    count = 0
    for char in myString:
        if char != 'x':
            count += 1
        elif char =='x':
            answer.append(count)
            count = 0
    answer.append(count)
    return answer
