import sys

def solution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    dot = list(map(int, input().split()))
    dot.sort()
    dot.insert(0, 0)
    dot.append(1000000000)
    for _ in range(m):
        line_start, line_end = map(int, input().split())
        left, right = 1, n + 1
        index_start = 0
        index_end = 0
        while left <= right:
            mid = (left + right) // 2
            if dot[mid - 1] < line_start <= dot[mid]:
                index_start = mid
                break
            if dot[mid] > line_start:
                right = mid - 1
            else:
                left = mid + 1
        left, right = 1, n + 1
        while left <= right:
            mid = (left + right) // 2
            if dot[mid - 1] < line_end <= dot[mid]:
                if line_end == dot[mid]:
                    index_end = mid + 1
                else:
                    index_end = mid
                break
            if dot[mid] > line_end:
                right = mid - 1
            else:
                left = mid + 1
        print(index_end - index_start)

solution()