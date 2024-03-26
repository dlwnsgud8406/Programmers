from collections import deque


def solution(elements):
    answer = 0
    arr = []
    queue = deque(elements)
    arr = list(set(elements))
    for i in range(len(elements)):
        for j in range(len(elements)):
            arr.append(sum(list(queue)[0:i + 1]))
            queue.rotate(-1)

    return len(list(set(arr)))
