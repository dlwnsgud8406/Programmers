def solution(keyinput, board):
    max_x = board[0] // 2
    max_y = board[1] // 2
    x = y = 0

    for command in keyinput:
        if 'left' in command:
            if -max_x <= x - 1:
                x -= 1
            else:
                continue

        elif 'right' in command:
            if max_x >= x + 1:
                x += 1
            else:
                continue

        elif 'up' in command:
            if max_y >= y + 1:
                y += 1
            else:
                continue

        elif 'down' in command:
            if -max_y <= y - 1:
                y -= 1
            else:
                continue

    return [x, y]
