def solution(command):
    answer = []
    si = sj = 0
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_num = 0
    for com in command:
        if com == 'R':
            direction_num += 1
        elif com == 'L':
            direction_num -= 1
        elif com == 'G':
            si, sj = si + direction[direction_num % 4][0], sj + direction[direction_num % 4][1]
        elif com == 'B':
            si, sj = si - direction[direction_num % 4][0], sj - direction[direction_num % 4][1]

    return [si, sj]
