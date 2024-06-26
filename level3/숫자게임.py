from collections import deque
def solution(A, B):
    answer = 0
    A.sort()
    A = deque(A)
    B.sort()
    B = deque(B)
    while B:
        if A[0] < B[0]:
            answer += 1
            A.popleft()
            B.popleft()
        else:
            B.popleft()
    return answer