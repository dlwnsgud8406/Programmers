def solution(n, m, section):
    answer = 0
    end = -1  # 이전 섹션의 끝 지점을 기록할 변수
    for start in section:
        if start > end:  # 이전 섹션의 끝 지점보다 현재 섹션의 시작 지점이 뒤에 있으면
            answer += 1  # 새로운 직선을 그어야 함
            end = start + m - 1  # 새로운 직선의 끝 지점 업데이트
        else:
            end = min(end, start + m - 1)  # 겹치는 부분만큼 직선을 그어야 함
    return answer