import sys

n, l = map(int, sys.stdin.readline().split())

result = 0
data = list(map(int, sys.stdin.readline().split()))
data.sort()


is_continue = False
l_pos, pos = 0, 0
# 4 2
# 1 2 100 101
while pos < n - 1:
    # 테이프 길이(l) <= 연속되는 값일 경우
    is_continue = True if (data[pos] + 1) == data[pos + 1] else False
    # 다음글자랑 연속되지 않을 경우
    # 기존 값으로부터 l번 연속되었을 시
    if not is_continue or (l_pos + l - 1) == pos:
        result += 1
        is_continue = False
        l_pos = pos + 1
    # print(pos)
    pos += 1

print(result + 1)
