def solution(expression):
    answer = 0
    method = [['*', '+', '-'], ['*', '-', '+'], ['+', '-', '*'], ['+', '*', '-'], ['-', '+', '*'], ['-', '*', '+']]
    money = []
    for op in method:
        a = op[0]
        b = op[1]
        temp = []
        for cal in expression.split(a):
            arr = [f"({i})" for i in cal.split(b)]
            temp.append(f'({b.join(arr)})')
        money.append(abs(eval(a.join(temp))))
    return max(money)
