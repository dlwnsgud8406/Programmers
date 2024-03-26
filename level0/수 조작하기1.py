def solution(n, control):
    for char in control:
        if 'w' in char:
            n += 1
        elif 's' in char:
            n -= 1
        elif 'd' in char:
            n += 10
        elif 'a' in char:
            n -= 10
    return n
