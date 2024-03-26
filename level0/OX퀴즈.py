def solution(quiz):
    answer = []
    for cal in quiz:
        a, b = cal.split(' = ')
        if eval(a) != int(b):
            answer.append('X')
        else:
            answer.append('O')
    return answer
