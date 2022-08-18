def solution(prices):
    answer = []

    for i, price in enumerate(prices):
        cnt = 0

        if i < len(prices)-1:
            for others in prices[i+1:]:
                cnt += 1
                if others < price:
                    break
        answer.append(cnt)

    return answer

# def solution(prices):
#    answer = []
#
#    second = len(prices)
#    for i, price in enumerate(prices):
#        flag = 0
#
#        if i < len(prices)-1:
#            for j, others in enumerate(prices[i+1:]):
#                if others < price:
#                    answer.append(j+1)
#                    flag = 1
#                    break
#        if not flag:
#            answer.append(second-i-1)
#
#    return answer
