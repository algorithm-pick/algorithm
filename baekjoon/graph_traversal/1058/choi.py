from collections import deque

n = int(input())
friends = list(input() for _ in range(n))
graph = [[] for _ in range(n)]

# 문자열 중 Y인 것에 대해서만 graph 만들어줌
for i, friend in enumerate(friends):
    for i2, YN in enumerate(friend):
        if YN == 'Y':
            graph[i].append(i2)

# 각각의 사람에 대해 bfs로 탐색, 큐에 인덱스와 length를 리스트로 넣어줌
# 인덱스는 사람, length는 인접도를 의미 (0이면 자기 자신, 1이면 자기 친구, 2면 친구의 친구)
max = 0
for i in range(n):
    length = 0
    visited = []
    q = deque()

    q.append([i, length])
    while q:
        friend = q.popleft()

        # 2-친구 까지니까 length가 2를 넘어가면 탐색을 중지
        if friend[1] > 2:
            break

        # 큐에서 빼낸 사람의 친구를 다시 큐에 넣어줘야하니까 새롭게 큐에 들어갈 사람은 length가 1씩 증가
        length = friend[1] + 1

        if friend[0] not in visited:
            visited.append(friend[0])
            for j in graph[friend[0]]:
                # 큐에서 빼낸 사람의 친구(j) 와 시작점인 사람과의 거리(length)를 다시 큐에 넣어줌
                q.append([j, length])

    # 2-친구가 가장 많은 사람으로 max값 갱신, 자기 자신은 친구가 아니므로 -1
    if max < len(visited)-1:
        max = len(visited)-1

print(max)
