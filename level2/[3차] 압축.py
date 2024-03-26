def solution(msg):
    arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    answer = []
    count = 0
    string = msg[0]
    while count != len(msg):
        if string in arr:
            if count != len(msg)-1:
                count += 1
            else:
                answer.append(arr.index(string)+1)
                break
            string += msg[count]
        else:
            arr.append(string)
            answer.append(arr.index(string[:-1])+1)
            string = msg[count]
    return answer
