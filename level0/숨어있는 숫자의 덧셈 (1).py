def solution(my_string):
    answer = 0
    for char in my_string:
        if '0'<=char<='9':
            answer += int(char)
    return answer
