import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    data = [tuple(map(int, input().split())) for _ in range(n)]
    data.sort()
    count = 1
    temp = data[0][1]

    for i in range(1, n):
        if data[i][1] < temp:
            temp = data[i][1]
            count += 1
    print(count)