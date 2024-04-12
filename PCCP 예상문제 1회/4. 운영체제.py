import heapq

def solution(program):
    answer = [0] * 11
    heap = []  # 우선순위 큐
    program.sort(key=lambda x: (x[1], x[0]))  # 호출된 시각과 우선순위를 기준으로 정렬
    time = 0
    while program or heap:
        while program and program[0][1] <= time:
            heapq.heappush(heap, program.pop(0))
        if program and not heap:
            time = program[0][1]
            heapq.heappush(heap, program.pop(0))
        temp = heapq.heappop(heap)
        answer[temp[0]] += (time - temp[1])
        time += temp[2]
    answer[0] = time
    return answer
