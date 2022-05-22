def solution():
    n = int(input())
    road = list(map(int, input().split()))
    fuel = list(map(int, input().split()))
    answer = 0
    min_fuel = fuel[0]
    for i in range(1, n):
        answer += (min_fuel * road[i - 1])
        if fuel[i] < min_fuel:
            min_fuel = fuel[i]
    print(answer)

solution()