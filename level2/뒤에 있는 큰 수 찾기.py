import heapq
def solution(numbers):
    answer = [-1] * len(numbers)
    heap = []
    for i in range(len(numbers)):
        while heap and heap[0][0] < numbers[i]:
            value, index = heapq.heappop(heap)
            answer[index] = numbers[i]
        heapq.heappush(heap, [numbers[i], i])
    return answer
print(solution([1,1,1,1]))
