def solution(clothes):
    answer = 1
    clothes_type = {}

    for name, kind in clothes:
        if kind not in clothes_type:
            clothes_type[kind] = 2
        else:
            clothes_type[kind] = clothes_type[kind] + 1

    for num in clothes_type.values():
        answer = answer * num

    return answer - 1
