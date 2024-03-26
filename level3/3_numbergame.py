import heapq

def solution(A, B):
    answer = 0
    A = [-i for i in A]
    B = [-i for i in B]
    heapq.heapify(A)
    heapq.heapify(B)
    while A and B:
        a = heapq.heappop(A)
        b = heapq.heappop(B)
        if -a < -b:
            answer = answer + 1
        else:
            heapq.heappush(B, b)
    return answer

A = [5,1,3,7]
B = [2,2,6,8]
print(solution(A, B))