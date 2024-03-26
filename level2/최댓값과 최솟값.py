import heapq


def solution(s):
    answer = ''
    get_number = s.split(' ')
    heap_number = []
    for i in range(len(get_number)):
        heapq.heappush(heap_number, int(get_number[i]))
    answer = str(heapq.heappop(heap_number)) + ' '
    for i in range(len(heap_number) - 1):
        heapq.heappop(heap_number)
    answer = answer + str(heapq.heappop(heap_number))

    return answer
