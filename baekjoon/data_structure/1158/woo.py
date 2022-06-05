from collections import deque

def solution():
    n, k = map(int, input().split())
    queue = deque([i for i in range(1, n+1)])
    answer = []
    for _ in range(n-k+1):
        for _ in range(k-1):
            temp = queue.popleft()
            queue.append(temp)
        temp = queue.popleft()
        answer.append(temp)
    for _ in range(k-1):
        temp = queue.popleft()
        answer.append(temp)
    print("<" + ", ".join([str(answer[i]) for i in range(n)]) + ">")

solution()