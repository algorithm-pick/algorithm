import sys
input = sys.stdin.readline

a, b = input().rstrip(), input().rstrip()
if len(a) == 1:  # 글자가 한글자 일때
    print(0) if a == b else print(-1)   # 두문자가 같다면 0, 아니면 -1
    exit(0)
elif sorted(a) != sorted(b):    # 정렬했는데 두 문자가 다른가?
    print(-1)  # 다르다면 문자위치 바꾼다고 달라질 수 있는게 아님
    exit(0)
else:
    count = 0   # 연산 횟수 최솟값
    idx = len(b)-1  # b의 마지막 인덱스

    for i in range(len(a)-1, -1, -1):
        if a[i] != b[idx]:  # 문자가 다를 때
            count += 1
        else:   # 문자가 같을 때
            idx -= 1
    print(count)
