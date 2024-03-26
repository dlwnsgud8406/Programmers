def solution(queue1, queue2):
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    standard = (sum1 + sum2) // 2
    temp1 = temp2 = 0
    length = len(queue1)
    while temp1 < 2 * length and temp2 < 2 * length and sum1 != sum2:
        if sum1<standard:
            sum1 += queue2[temp2]
            sum2 -= queue2[temp2]
            queue1.append(queue2[temp2])
            temp2 += 1
        else:
            sum1 -= queue1[temp1]
            sum2 += queue1[temp1]
            queue2.append(queue1[temp1])
            temp1 += 1
    if sum1 != standard:
        return -1
    else: return temp1+temp2
