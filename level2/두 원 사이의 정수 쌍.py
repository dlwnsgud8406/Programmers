import math


def solution(r1, r2):
    count = 0
    for x in range(-r2, r2 + 1):
        if x + r1 < 0 or x - r1 > 0:
            y2_max = (r2 ** 2 - x ** 2) ** (1 / 2)
            y2_min = -y2_max

            count += math.floor(y2_max) - math.ceil(y2_min) + 1
        elif x == r1 or x == -r1:
            y2_max = (r2 ** 2 - x ** 2) ** (1 / 2)
            y2_min = -y2_max

            count += math.floor(y2_max) - math.ceil(y2_min) + 1
        else:
            y2_max = (r2 ** 2 - x ** 2) ** (1 / 2)
            y2_min = -y2_max
            y1_max = (r1 ** 2 - x ** 2) ** (1 / 2)
            y1_min = -y1_max

            count += (math.floor(y2_max) - math.ceil(y1_max) + 1) + (math.floor(y1_min) - math.ceil(y2_min) + 1)

    return count
