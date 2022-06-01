# 21921 : 블로그
import sys

input = sys.stdin.readline

n, x = map(int, input().split())
visit_log = list(map(int, input().split()))  # 방문자 수

if max(visit_log) == 0:  # 최대 방문자 수가 0일 때
    print('SAD')  # SAD 출력 후 바로 종료
    exit(0)

prefix_log = [visit_log[0]]  # prefix_log에 누적합 계산
for i in range(1, n):
    prefix_log.append(prefix_log[-1] + visit_log[i])

max_visit = prefix_log[x - 1]  # 최대 방문자 수
count = 1  # 기간이 몇개 있는지

for i in range(x, n):
    temp = prefix_log[i] - prefix_log[i - x]
    if temp > max_visit:  # temp가 기존 최대 방문자 수보다 높다면
        max_visit = temp  # 최대 방문자 수 temp로 갱신
        count = 1
    elif temp == max_visit:  # temp가 기존 최대 방문자 수와 같다면
        count += 1  # 기간 1 증가

print(max_visit)
print(count)
