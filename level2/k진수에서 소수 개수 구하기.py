def solution(n, k):
    answer = 0
    converted_by_k = convert(n, k)
    primes = converted_by_k.split('0')
    print(primes)
    # primes.remove('')

    # for prime in primes:
    #     if check_prime_number(int(prime)) and int(prime) > 1:
    #         answer += 1

    return answer


def convert(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]


def check_prime_number(n):
    for i in range(2, n):
        if n % i == 0:
            return False  # 소수가 아님
    return True  # 소수임

print(solution(1000000, 10))
