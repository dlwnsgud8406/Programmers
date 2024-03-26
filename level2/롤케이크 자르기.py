def solution(topping):
    answer = 0
    cheolsoo = {}
    brother = {}
    for cake in topping:
        if cake in cheolsoo:
            cheolsoo[cake] += 1
        else:
            cheolsoo[cake] = 1

    for cake in topping:
        if len(brother) == len(cheolsoo):
            answer += 1
        if cake not in brother:
            brother[cake] = 1

        cheolsoo[cake] -= 1
        if cheolsoo[cake] == 0:
            del cheolsoo[cake]

    return answer
