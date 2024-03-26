def solution(n, works):
    if sum(works) <= n:
        return 0

    while n > 0:
        works.sort(reverse=True)
        max_work = works[0]
        if max_work == 0:
            break
        for i in range(len(works)):
            if works[i] == max_work:
                works[i] -= 1
                n -= 1
                if n == 0:
                    break
    return sum(work**2 for work in works)
