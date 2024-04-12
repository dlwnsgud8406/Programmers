from functools import lru_cache
#
# def solution(queries):
#     answer = []
#     generation_list = [["Rr"]]
#     for i in range(1, 15):
#         temp_list = []
#         for generation in generation_list[i - 1]:
#             if generation == "Rr":
#                 temp_list.extend(["RR", 'Rr', 'Rr', 'rr'])
#             elif generation == "RR":
#                 temp_list.extend(["RR"] * 4)
#             elif generation == "rr":
#                 temp_list.extend(["rr"] * 4)
#
#         generation_list.append(temp_list)
#     for i, j in queries:
#         answer.append(generation_list[i - 1][j - 1])
#     return answer

from functools import lru_cache

@lru_cache(maxsize=None)  # 크기 제한 없이 모든 결과를 캐시
def generate_generation(n):
    if n == 1:
        return [["Rr"]]
    else:
        previous_generation = generate_generation(n - 1)
        temp_list = []
        for generation in previous_generation:
            for genotype in generation:
                if genotype == "Rr":
                    temp_list.extend(["RR", 'Rr', 'Rr', 'rr'])
                elif genotype == "RR":
                    temp_list.extend(["RR"] * 4)
                elif genotype == "rr":
                    temp_list.extend(["rr"] * 4)
        return [temp_list]

def solution(queries):
    answer = []
    for i, j in queries:
        generation_list = generate_generation(i)
        answer.append(generation_list[0][j - 1])
    return answer


print(solution([[3, 5]]))
