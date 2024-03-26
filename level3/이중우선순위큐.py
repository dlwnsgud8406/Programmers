import heapq


def solution(operations):
    answer = []
    heap = []
    for operation in operations:
        command, number = operation.split(' ')
        if command == 'I':
            heapq.heappush(heap, int(number))
        elif command == 'D':
            if number == '-1':
                try:
                    heapq.heappop(heap)
                except IndexError:
                    pass
            elif number == '1':
                try:
                    heap.pop()
                except IndexError:
                    pass

    if len(heap) == 0:
        return [0, 0]
    else:
        return [max(heap), min(heap)]
