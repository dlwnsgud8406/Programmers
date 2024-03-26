def solution(s):
    answer = 0
    arr = s.split(' ')
    num = []
    for com in arr:
        if com == 'Z':
            num.pop()
        else:
            num.append(int(com))
    return sum(num)
