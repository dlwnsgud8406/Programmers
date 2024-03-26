def solution(price, money, count):
    answer = -1
    needed_money = 0
    for i in range(1, count+1):
        needed_money += (i * price)
    if needed_money <= money:
        return 0
    else:
        return needed_money - money
