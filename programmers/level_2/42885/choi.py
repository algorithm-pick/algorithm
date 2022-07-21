from collections import deque


def solution(people, limit):
    answer = 0
    wait = deque(sorted(people))
    weight_sum = 0

    while wait:
        if weight_sum == 0:
            weight_sum += wait.pop()
            if len(wait) == 0:
                break

        if weight_sum + wait[0] <= limit:
            weight_sum += wait.popleft()

        else:
            weight_sum = 0
            answer += 1

    if weight_sum > 0:
        answer += 1

    return answer
