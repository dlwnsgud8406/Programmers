
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        count = getMyDivisor(i)
        if count % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer

def getMyDivisor(n):

    divisorsList = []

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisorsList.append(i) 
            if ( (i**2) != n) : 
                divisorsList.append(n // i)
    
    return len(divisorsList)