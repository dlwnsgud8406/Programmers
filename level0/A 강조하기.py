def solution(myString):
    answer = ''
    for char in myString:
        if char.isupper() and char != 'A':
            answer += char.lower()
        elif char in 'a':
            answer += 'A'
        else:
            answer += char
    return answer
