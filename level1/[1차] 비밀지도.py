def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        code = bin(arr1[i] | arr2[i])[2:]
        final_code = ''
        length = len(code)
        while length < n:
            final_code += '0'
            length += 1
        final_code += code
        answer.append(final_code.replace('1', '#').replace('0', ' '))
    return answer
