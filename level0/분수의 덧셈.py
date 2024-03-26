import math
def solution(numer1, denom1, numer2, denom2):
    son = denom2*numer1 + denom1*numer2
    mother = denom1*denom2
    common = math.gcd(son, mother)
    return [son//common, mother//common]