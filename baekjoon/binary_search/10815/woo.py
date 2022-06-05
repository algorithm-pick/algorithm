def solution():
    n = int(input())
    have = list(map(int, input().split()))
    m = int(input())
    find = list(map(int, input().split()))
    for i in find:
        if i in have:
            print(1, end=' ')
        else:
            print(0, end=' ')

def solution():
    n = int(input())
    have = list(map(int, input().split()))
    have.sort()
    m = int(input())
    find = list(map(int, input().split()))
    for i in find:
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) / 2
            if have[mid] == i:
                print(1, end = ' ')
                break
            if have[mid] > i:
                right = mid - 1
            else:
                left = mid + 1
        if left > right:
            print(0, end = ' ')

solution()