import heapq
def solution(ability, number):
    answer = 0
    heapq.heapify(ability)

    for i in range(number):
        sum_ability = heapq.heappop(ability) + heapq.heappop(ability)
        heapq.heappush(ability, sum_ability)
        heapq.heappush(ability, sum_ability)

    return sum(ability)
