from collections import deque
def solution(A, B):
    A = deque(list(A))
    B = deque(list(B))
    for i in range(len(A)):
        if A == B:
            return i
        else:
            A.rotate(1)
    return -1

from collections import deque
def solution(A, B):
    A = deque(A)
    arr = []
    answer = 0
    for i in range(len(A)):
        if ''.join(A) == B:
            return i
        A.rotate(1)
    return -1