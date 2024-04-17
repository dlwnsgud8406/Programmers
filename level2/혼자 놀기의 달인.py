from heapq import heappop,heappush
def solution(cards):
    answer = 0
    visited = [False for _ in range(len(cards))]
    lst = []
    for i in range (len(cards)):
        if visited[i]: continue
        visited[i] = True
        cur,linked = i,1
        while cards[cur] -1 != i:
            cur = cards[cur]-1
            visited[cur] = True
            linked +=1
        heappush(lst,linked*-1)
    if len(lst) < 2:
        answer = 0
    else:
        answer = heappop(lst) * heappop(lst)
    return answer
