import heapq
def solution(n, k, enemy):
    answer = 0
    heap = []
    for i, v in enumerate(enemy):
        heapq.heappush(heap, v)
        if len(heap) > k:
            n -= heapq.heappop(heap)
        if n < 0:
            return i
    return len(enemy)
