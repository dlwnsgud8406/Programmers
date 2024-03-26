def solution(ineq, eq, n, m):
    if eq == '!':
        eq = ''
    return int(eval(str(n) + ineq + eq + str(m)))
