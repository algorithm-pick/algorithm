def solution(prices):
    answer = []
    length = len(prices)
    for i in range(length):
        count = 0
        for j in range(i+1, length):
            count += 1
            if prices[j] < prices[i]:
                break
        answer.append(count)
    return answer

print(solution([1, 2, 3, 2, 3]))
