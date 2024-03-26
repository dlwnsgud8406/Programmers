def solution(number, limit, power):
    attack = []
    
    for i in range(1, number+1):
        arm = getMyDivisor(i)
        if arm > limit:
            attack.append(power)
        else:
            attack.append(arm)
    
    return sum(attack)

def getMyDivisor(n):

    divisorsList = []

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisorsList.append(i) 
            if ( (i**2) != n) : 
                divisorsList.append(n // i)

    divisorsList.sort()
    
    return len(divisorsList)