import heapq

def solution(scoville, K):
    answer = 0
    food = []
    for i in scoville:
        heapq.heappush(food, i)
    while food[0] < K:
        if len(food) < 2:
            return -1
        heapq.heappush(food, heapq.heappop(food) + (heapq.heappop(food) * 2))
        answer += 1
    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))