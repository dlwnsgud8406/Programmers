from itertools import product
dic = ['aya', 'ye', 'woo', 'ma']

def solution(babbling):
    answer = 0
    available = []
    for i in range(1, 7):
        for com in list(product(dic, repeat = i)):
            string = ''
            before_word = ''
            for word in com:
                if before_word != word:
                    string += word
                before_word = word
            available.append(string)
    for word in babbling:
        if word in available:
            answer += 1

    return answer
