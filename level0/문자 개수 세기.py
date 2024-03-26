def solution(my_string):
    answer = [0] * 52
    for char in my_string:
        if 'A'<=char<='Z':
            answer[ord(char) % 65] += 1
        elif 'a' <= char <= 'z':
            answer[ord(char) % 97 + 26] += 1
    return answer
