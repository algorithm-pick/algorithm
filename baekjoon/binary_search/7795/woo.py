import sys

def solution():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        answer = 0
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        b.sort()
        for i in a:
            left = 0
            right = m - 1
            while left <= right:
                mid = (left + right) // 2
                if b[mid] == i:
                    right = mid - 1
                elif b[mid] > i:
                    right = mid - 1
                else:
                    left = mid + 1
            answer += (right + 1)
        print(answer)

solution()
