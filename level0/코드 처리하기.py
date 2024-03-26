def solution(code):
    answer = []
    mode = False
    for i in range(len(code)):
        if code[i] == '1':
            if mode:
                mode = False
            else:
                mode = True
        else:
            if not mode:
                if i % 2 == 0:
                    answer.append(code[i])
            else:
                if i % 2 == 1:
                    answer.append(code[i])
    string = ''.join(answer)
    if not len(string):
        return 'EMPTY'
    else:
        return string
