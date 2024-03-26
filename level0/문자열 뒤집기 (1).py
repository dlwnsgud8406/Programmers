def solution(my_string, s, e):
    answer = ''
    head_word = my_string[:s]
    word = my_string[s:e+1][::-1]
    tail_word = my_string[e+1:]
    return head_word + word + tail_word
