from collections import deque

def solution(queue1, queue2):
    answer = 0
    if (sum(queue1) + sum(queue2)) % 2 != 0:
        return -1
    max_count = len(queue1) * 5
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    new_q1 = deque(queue1)
    new_q2 = deque(queue2)
    while True:
            if sum1 == sum2:
                break
            if sum1 == 0 or sum2 == 0:
                return -1
            if sum1 > sum2:
                temp = new_q1.popleft()
                new_q2.append(temp)
                sum1 -= temp
                sum2 += temp
            else:
                temp = new_q2.popleft()
                new_q1.append(temp)
                sum2 -= temp
                sum1 += temp
            answer += 1
            if answer > max_count:
                return -1
    return answer

print(solution([1, 2, 1, 2], [1, 10, 1, 2]))