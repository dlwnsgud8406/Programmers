def solution(s, n):
    answer = ''
    for char in s:
        if char.isupper():
            answer += chr((ord(char)-ord('A') + n) % 26 + 65)
        elif char.islower():
            answer += chr((ord(char)-ord('a') + n) % 26 + 97)
        else:
            answer += char
            
    return answer