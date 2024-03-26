def solution(prices):
    answer = []
    for i in range(len(prices)):
        answer.append(len(prices)-i-1)
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                answer.pop()
                answer.append(j - i)
                break
    return answer