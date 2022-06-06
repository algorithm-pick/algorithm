# 11663 : 선분 위의 점
import sys


def binary_search(dots, a, b):  # 이진 탐색
    # 선분에 포함되는 dots의 제일 왼쪽 인덱스 찾기
    start = 0
    end = len(dots)-1
    while start <= end:
        left = (start+end)//2
        if a <= dots[left] <= b:
            end = left-1
        else:
            if dots[left] < a:
                start = left+1
            elif dots[left] > b:
                end = left-1

    # 선분에 포함되는 dots의 제일 오른쪽 인덱스 찾기
    start = 0
    end = len(dots)-1
    while start <= end:
        right = (start+end)//2
        if a <= dots[right] <= b:
            start = right + 1
        else:
            if dots[right] < a:
                start = right + 1
            elif dots[right] > b:
                end = right - 1

    if dots[left] >= a and dots[right] <= b:
        return right-left+1
    if dots[left] < a and dots[right] > b:
        return right-left-1

    return right-left


input = sys.stdin.readline
n, m = map(int, input().split())  # n : 점 수, m : 선분 수
dots = sorted(map(int, input().split()))    # 점 정보
lines = [tuple(map(int, input().split())) for _ in range(m)]    # 선분 정보

for a, b in lines:  # 선분별로 이진탐색
    print(binary_search(dots, a, b))