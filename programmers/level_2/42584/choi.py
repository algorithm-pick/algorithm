from collections import deque


def solution(prices):
    answer = []
    price = deque(prices)

    while price:
        cnt = 0
        target = price.popleft()

        for i in price:
            cnt += 1
            if i < target:
                break
        answer.append(cnt)

    return answer

# def solution(prices):
#    answer = []
#
#    for i, price in enumerate(prices):
#        cnt = 0
#
#        if i < len(prices)-1:
#            for others in prices[i+1:]:
#                cnt += 1
#                if others < price:
#                    break
#        answer.append(cnt)
#
#    return answer
