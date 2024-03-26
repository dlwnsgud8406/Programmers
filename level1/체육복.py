def solution(n, lost, reserve):
    lost, reserve = set(lost) - set(reserve), set(reserve) - set(lost)
    for num in lost:
        if num - 1 in reserve:
            reserve.remove(num - 1)
        elif num + 1 in reserve:
            reserve.remove(num + 1)
        else:
            n -= 1
    return n
