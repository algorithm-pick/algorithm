import sys

def solution():
    input = sys.stdin.readline 
    n, m = map(int, input().split())
    a = [int(input()) for _ in range(n)]
    a.sort()
    for _ in range(m):
        d = int(input())
        left = 0
        right = n - 1
        answer = -1
        while left <= right:
            mid = (left + right) // 2
            if a[mid] == d:
                answer = mid
                right = mid - 1
            elif a[mid] > d:
                right = mid - 1
            else:
                left = mid + 1
        print(answer)

solution()

# import sys

# def solution():
#     input = sys.stdin.readline 
#     n, m = map(int, input().split())
#     a = [int(input()) for _ in range(n)]
#     a.sort()
#     for _ in range(m):
#         d = int(input())
#         try:
#             print(a.index(d))
#         except:
#             print(-1)

# solution()