def solution(s1, s2):
    answer = 0
    for word in s1:
        if s2.count(word):
            answer += 1

    return answer
