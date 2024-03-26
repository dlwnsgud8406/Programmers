def solution(sides):
    sides = sorted(sides)
    if sides[0] + sides[1] <= sides[2]:
        return 2
    else: return 1
