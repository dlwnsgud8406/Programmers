def solution(park, routes):
    i_len, j_len = len(park), len(park[0])
    ci = cj = 0
    for i in range(i_len):
        for j in range(j_len):
            if park[i][j] == 'S':
                ci, cj = i, j

    for route in routes:
        count = 0
        direction, speed = route.split(' ')
        speed = int(speed)
        if direction == 'W':
            if cj - speed < 0:
                pass
            else:
                for i in range(speed):
                    if park[ci][cj - 1] == 'X':
                        cj += count
                        break
                    else:
                        count += 1
                        cj -= 1

        elif direction == 'E':
            if cj + speed >= j_len:
                pass
            else:
                for i in range(speed):
                    if park[ci][cj + 1] == 'X':
                        cj -= count
                        break
                    else:
                        count += 1
                        cj += 1

        elif direction == 'S':
            if ci + speed >= i_len:
                pass
            else:
                for i in range(speed):
                    if park[ci + 1][cj] == 'X':
                        ci -= count
                        break
                    else:
                        count += 1
                        ci += 1

        elif direction == 'N':
            if ci - speed < 0:
                pass
            else:
                for i in range(speed):
                    if park[ci - 1][cj] == 'X':
                        ci += count
                        break
                    else:
                        count += 1
                        ci -= 1

    return [ci, cj]
