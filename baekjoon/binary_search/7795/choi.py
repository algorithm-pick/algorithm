from collections import deque
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort()

    ans = 0
    cnt = len(B)
    for i in A:
        if cnt == 0:
            break

        for j in B[::-1]:
            if i <= j:
                B.pop()
                cnt -= 1
            else:
                break

            if cnt == 0:
                break

        ans += cnt
    print(ans)
