def solution(s):
    n = len(s)

    # 슬라이딩 윈도우의 최대 길이부터 1까지 감소하며 탐색
    for length in range(n, 0, -1):
        # 가능한 모든 시작 위치에 대해
        for start in range(n - length + 1):
            # 윈도우 내의 문자열 추출
            substring = s[start:start + length]
            # 회문인지 확인
            if substring == substring[::-1]:
                return length  # 회문의 길이 반환

    # 여기에 도달했다면, 입력 문자열이 빈 문자열이거나, 함수가 잘못 구현된 경우입니다.
    return 0

    # answer_list = []
    # for j in range(len(s)-1):
    #     for i in range(len(s)-1):
    #         if s[i:len(s)-j] == s[i:len(s)-j][::-1]:
    #             answer_list.append(len(s) - i - j)
    #             break
    #         elif s[j:len(s) - i] == s[j:len(s) - i][::-1]:
    #             answer_list.append(len(s) - i - j)
    #             break
    # if len(answer_list) == 0:
    #     return 1
    # else:
    #     return max(answer_list)
