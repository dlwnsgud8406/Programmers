from collections import deque
def solution(arr):
    arr = deque(arr)
    if arr.count(2) == 0:
        return [-1]
    while arr[0] != 2:
        arr.popleft()
    while arr[-1] != 2:
        arr.pop()
    return list(arr)