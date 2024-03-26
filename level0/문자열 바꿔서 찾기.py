def solution(myString, pat):
    answer = 0
    convert_string = ''
    for char in myString:
        if char == 'A':
            convert_string += 'B'
        else:
            convert_string += 'A'
    return 1 if pat in convert_string else 0
