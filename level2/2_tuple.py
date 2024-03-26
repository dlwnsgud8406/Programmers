import math

def solution(s):
    answer = []
    max = 0
    index = 0
    tuple_list = []
    s = s[1:len(s)-1]
    s = s[1:len(s)-1]
    tuple_list = s.split('},{')
    for i in range(len(tuple_list)):
        if len(tuple_list[i]) > max:
            index = i
    # print(tuple_list[index].split(','))
    answer = tuple_list[index].split(',')
    print(answer)
    return answer

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
# s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
# s = "{{20,111},{111}}"
# s = "{{123}}"
# s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"

solution(s)