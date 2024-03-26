def solution(before, after):
    for char in before:
        if before.count(char) != after.count(char):
            return 0
    return 1

# from collections import Counter
# def solution(before, after):
#     if Counter(before) == Counter(after):
#         return 1
#     else:
#         return 0