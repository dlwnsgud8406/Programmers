def solution(chicken):
    answer = 0
    while chicken >= 10:
        ate = chicken//10
        answer += ate
        chicken = chicken % 10 + ate
    return answer
