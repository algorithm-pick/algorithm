def solution():
    n, x = map(int, input().split())
    visit = list(map(int, input().split()))
    max_result = sum(visit[:x])
    max_count = 1
    current = sum(visit[:x])
    for i in range(x, n):
        current = current + visit[i] - visit[i-x]
        if current > max_result:
            max_count = 1
            max_result = current
        elif current == max_result:
            max_count += 1
    if max_result == 0:
        print('SAD')
        return
    print(max_result)
    print(max_count)

solution()