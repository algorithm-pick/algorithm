from collections import deque

n, k = map(int, input().split())
result = []  # 출력될 결과
deq = deque(range(1, n + 1))  # 1부터 n까지 넣기

while deq:
    deq.rotate(-k)  # 원 순서 돌리기
    result.append(deq.pop())

print("<" + ", ".join(map(str, result)) + ">")
