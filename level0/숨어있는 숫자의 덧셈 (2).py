def solution(my_string):
    answer = 0
    number = ''
    for char in my_string:
        if '0'<=char<='9':
            number+= char
        elif len(number):
            answer += int(number)
            number = ''
    if len(number):
        answer += int(number)
    return answer
