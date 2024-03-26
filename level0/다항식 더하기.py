def solution(polynomial):
    x_answer = 0
    i_answer = 0
    arr = polynomial.split(' ')
    for cal in arr:
        if '+' in cal:
            pass
        elif 'x' not in cal:
            i_answer += int(cal)
        if 'x' in cal:
            if cal[:-1] == '':
                x_answer += 1
            else:
                x_answer += int(cal[:-1])

    if str(i_answer) == '0':
        i_answer = ''
    else:
        i_answer = str(i_answer)
    if x_answer == 0:
        x_answer = ''
    else:
        if x_answer == 1:
            x_answer = 'x'
        else:
            x_answer = str(x_answer) + 'x'

    if len(x_answer) == len(i_answer) == 0:
        answer = ''
    elif len(x_answer) == 0:
        answer = i_answer
    elif len(i_answer) == 0:
        answer = x_answer
    else:
        answer = x_answer + ' + ' + i_answer

    return answer
