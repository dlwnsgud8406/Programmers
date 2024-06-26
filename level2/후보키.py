from itertools import combinations


def solution(relation):
    row = len(relation)
    col = len(relation[0])

    arr = []
    for i in range(1, col + 1):
        arr.extend(combinations(range(col), i))

    unique = []
    for i in arr:
        tmp = [tuple([item[key] for key in i]) for item in relation]
        if len(set(tmp)) == row:  # 유일성
            put = True
            for x in unique:
                if set(x).issubset(set(i)):  # 최소성
                    put = False
                    break

            if put: unique.append(i)
    return len(unique)
