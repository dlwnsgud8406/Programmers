def solution(s):
    count = 0
    del_zero = 0
    length = 0
    before_length = 0
    while(len(s) != 1):
        before_length = len(s)
        s = s.replace('0','')
        length = len(s)
        del_zero = before_length-length + del_zero
        s = str(bin(length)[2:])
        count += 1
    return [count, del_zero]
