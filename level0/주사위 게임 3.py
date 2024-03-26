from collections import Counter
def solution(a, b, c, d):
    dict = sorted(Counter([a,b,c,d]).items(), key = lambda x:(x[1]))
    if len(dict) == 1:
        return 1111 * a
    elif len(dict) == 4:
        return min(dict)[0]
    elif len(dict) == 2:
        if dict[0][1] == 2:
            return (dict[0][0] + dict[1][0]) * (abs(dict[0][0] - dict[1][0]))
        elif dict[0][1] == 1:
            return (10 * dict[1][0] + dict[0][0]) ** 2
    elif len(dict) == 3:
        return dict[0][0] * dict[1][0]
