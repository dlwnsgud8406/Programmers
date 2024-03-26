def solution(new_id):
    answer = ''
    new_id = list(new_id.lower())
    for i in range(len(new_id)):
        if new_id[i] in '.-_abcdefghijklmnopqrstuvwxyz1234567890':
            answer += new_id[i]
    while '..' in answer:
        answer = answer.replace('..','.')
    answer = list(answer)
    if answer[0] == '.':
        answer[0] = ''
    if answer[len(answer)-1] == '.':
        answer[len(answer)-1] = ''
    answer = list(''.join(answer))
    if len(answer) == 0:
        answer.append('a')
    elif len(answer) >= 16:
        answer = answer[:15]
        if answer[0] == '.':
            answer[0] = ''
        if answer[len(answer)-1] == '.':
            answer[len(answer)-1] = ''
    answer = list(''.join(answer))
    if len(answer) < 3:
        repeat = answer[len(answer)-1]
        while len(answer) < 3:
            answer.append(repeat)
    return ''.join(answer)
