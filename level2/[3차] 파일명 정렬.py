def solution(files):
    answer = []
    array = []
    for file in files:
        num = ''
        name = ''
        flag = False
        for i in range(len(file)):
            if '0' <= file[i] <= '9':
                num += file[i]
                flag = True
            elif flag:
                break
            else:
                name += file[i]
        if flag:
            answer.append((name, int(num), files.index(file)))
    answer = sorted(answer, key = lambda x:(x[0].upper(), x[1], x[2]))
    for arr in answer:
        array.append(files[arr[2]])
    return array

print(solution(["O00321", "O49qcGPHuRLR5FEfoO00321"]))
