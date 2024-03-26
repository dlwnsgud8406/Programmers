dict = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def solution(s, skip, index):
    answer = ''
    num_skip = []
    num_s = []
    for char in skip:
        num_skip.append(dict.index(char))
    for char in s:
        num_s.append(dict.index(char))
    print(num_skip, num_s)
    for i in range(len(s)):
        for j in range(index):
            num_s[i] += 1
            while num_s[i] % 26 in num_skip:
                num_s[i] += 1
        answer += dict[num_s[i]%26]
    return answer
print(solution('zzzzz', 'a', 1))
