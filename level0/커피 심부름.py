def solution(order):
    answer = 0
    for coffee in order:
        if 'cafelatte' in coffee:
            answer += 5000
        elif 'americano' or 'anything' in coffee:
            answer += 4500

    return answer
