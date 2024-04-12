from collections import defaultdict


def solution(input_string):
    answer = []
    input_string += ' '
    check = defaultdict(bool)
    length = len(input_string)

    for i in range(length - 1):
        if input_string[i] != input_string[i + 1]:
            if not check[input_string[i]]:
                check[input_string[i]] = True
            else:
                answer.append(input_string[i])
    answer = ''.join(sorted(list(set(answer))))
    if not answer:
        return 'N'

    return answer
