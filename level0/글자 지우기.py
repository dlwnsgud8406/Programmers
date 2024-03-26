def solution(my_string, indices):
    answer = ''
    my_string = list(my_string)
    for num in indices:
        my_string[num] = '0'
    answer = ''.join(s for s in my_string).replace('0','')
    return answer
