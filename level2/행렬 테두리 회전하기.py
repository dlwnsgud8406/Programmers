from heapq import heappush

def solution(rows, columns, queries):
    answer = []
    arr = [[j + i*columns for j in range(1, columns + 1)] for i in range(rows)]
    for query in queries:
        y1, x1, y2, x2 = query
        heap = []

        y1x1 = arr[y1-1][x1-1]
        y1x2 = arr[y1-1][x2-1]
        y2x1 = arr[y2-1][x1-1]
        y2x2 = arr[y2-1][x2-1]

        heappush(heap,y1x1)
        heappush(heap,y1x2)
        heappush(heap,y2x1)
        heappush(heap,y2x2)

        for x in range(x2 - 1, x1 - 1, -1):
            arr[y1-1][x] = arr[y1-1][x-1]
            heappush(heap, arr[y1-1][x])

        for y in range(y2 - 1, y1 - 1, -1):
            arr[y][x2-1] = arr[y-1][x2-1]
            heappush(heap, arr[y][x2-1])

        for x in range(x1 - 1, x2 - 1, 1):
            arr[y2-1][x] = arr[y2-1][x+1]
            heappush(heap, arr[y2-1][x])

        for y in range(y1 - 1, y2 - 1, 1):
            arr[y][x1-1] = arr[y+1][x1-1]
            heappush(heap, arr[y][x1-1])

        arr[y1][x2-1] = y1x2
        arr[y2-1][x2-2] = y2x2
        arr[y2-2][x1-1] = y2x1

        answer.append(heap[0])
    return answer
