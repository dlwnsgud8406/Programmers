def solution(dirs):
    arr = []
    answer = 0
    before = 0
    x = y = 5
    for dir in dirs:
        if dir == 'U' and y > 0:
            before = y
            y -= 1
            if sorted(([y, x], [before, x])) not in arr:
                arr.append(sorted(([y, x], [before, x])))
                answer += 1
        elif dir == 'L' and x > 0:
            before = x
            x -= 1
            if sorted(([y, x], [y, before])) not in arr:
                arr.append(sorted(([y, x], [y, before])))
                answer += 1
        elif dir == 'R' and x < 10:
            before = x
            x += 1
            if sorted(([y, x], [y, before])) not in arr:
                arr.append(sorted(([y, x], [y, before])))
                answer += 1
        elif dir == 'D' and y < 10:
            before = y
            y += 1
            if sorted(([y, x], [before, x])) not in arr:
                arr.append(sorted(([y, x], [before, x])))
                answer += 1

    return answer