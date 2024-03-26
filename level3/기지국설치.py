import math

def solution(n, stations, w):
    answer = 0
    covered = 0  # 현재까지 덮은 범위를 기록
    lightning = 2 * w + 1  # 번개 범위

    for station in stations:
        left_uncovered = max(0, station - w - 1 - covered)  # 이전까지 덮지 않은 왼쪽 영역
        answer += math.ceil(left_uncovered / lightning)  # 왼쪽 영역을 처리
        covered = station + w  # 현재 역 주변까지 덮은 범위 갱신

    # 마지막 역 이후의 남은 영역 처리
    right_uncovered = max(0, n - covered)
    answer += math.ceil(right_uncovered / lightning)

    return answer