# 10815 : 숫자 카드
import sys

input = sys.stdin.readline

n = int(input())
arr_n = set(map(int, input().split()))

m = input()
arr_m = list(map(int, input().split()))

for i in arr_m:
    print(1, end=' ') if i in arr_n else print(0, end=' ')
