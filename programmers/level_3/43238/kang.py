# 입국심사
# https://programmers.co.kr/learn/courses/30/lessons/43238
def solution(n, times):
    answer = 0
    left, right = 1, max(times) * n  # right에 최대시간 넣기
    while left <= right:
        mid = (left + right) // 2
        people = 0
        for t in times:
            people += mid // t
            if people >= n:
                break
        if people >= n:
            answer = mid
            right = mid - 1
        elif people < n:
            left = mid + 1
    return answer
