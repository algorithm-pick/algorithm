from collections import defaultdict
from collections import deque

place = defaultdict(list)
places = defaultdict(deque)


def dfs(start, answer):
    if not places[start]:
        return

    while places[start]:
        target = places[start].popleft()
        answer.append(target)
        dfs(target, answer)


def solution(tickets):
    answer = []

    for pre, nex in tickets:
        place[pre].append(nex)

    for i in place:
        place[i].sort()
        places[i] = deque(place[i])

    answer.append("ICN")
    dfs("ICN", answer)

    return answer
