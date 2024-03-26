def solution(A,B):
    answer = 0
    length = len(A)
    A.sort()
    B.sort()
    for i in range(length):
        answer = answer + A[0] * B[-1]
        del A[0]
        B.pop()
    print(answer)
    return answer

solution([1, 2], [3, 4])