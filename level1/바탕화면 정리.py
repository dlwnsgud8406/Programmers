def solution(wallpaper):
    lux, luy, rdx, rdy = 100, 100, 0, 0

    r = len(wallpaper)
    c = len(wallpaper[0])

    for x in range(r):
        for y in range(c):
            if wallpaper[x][y] == "#":
                lux = min(lux, x)
                luy = min(luy, y)
                rdx = max(rdx, x)
                rdy = max(rdy, y)


    return [lux, luy, rdx + 1, rdy + 1]