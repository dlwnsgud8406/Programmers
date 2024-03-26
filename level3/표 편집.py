def solution(n, k, cmd):
    answer = ''
    arr = [str(i) for i in range(n)]
    deleted_arr = []
    cursor = k
    for command in cmd:
        if command == 'C':
            deleted_arr.append([arr.index(arr[cursor]), arr.pop((cursor))])
        elif command == 'Z':
            arr.insert(deleted_arr[len(deleted_arr)-1][0], deleted_arr[len(deleted_arr)-1][1])
            deleted_arr.pop(len(deleted_arr)-1)
        else:
            com, num = map(str, command.split(' '))
            num = int(num)
            if com == 'D':
                cursor += num
            else:
                cursor -= num
    for i in range(n):
        if str(i) in arr:
            answer += 'O'
        else:
            answer += 'X'
    return answer
print(solution(7, 3))