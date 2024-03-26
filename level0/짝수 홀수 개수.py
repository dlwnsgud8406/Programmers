def solution(num_list):
    odd_count = even_count = 0
    for num in num_list:
        if num % 2 == 1:
            odd_count += 1
        else:
            even_count += 1
    return [even_count, odd_count]
