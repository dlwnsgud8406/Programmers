def solution(str_list):
    answer = []
    count = 0
    flag = True
    for count in range(len(str_list)):
        if str_list[count] == 'l':
            flag = True
            break
        elif str_list[count] == 'r':
            flag = False
            break
    if flag:
        return(str_list[:count])
    else:
        return(str_list[count+1:])
