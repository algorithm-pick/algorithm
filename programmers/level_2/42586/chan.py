from collections import deque


def solution(progresses, speeds):
    complete_index = 0
    size = len(progresses)
    last_index = 0
    queue = deque([])
    results = []

    while True:
        # 더하기
        temp = 0
        for i in range(size):
            progresses[i] += progresses[i] + speeds[i] if progresses[i] < 100 else 0
            # 100 이상일 경우 큐에 추가
            if progresses[i] >= 100:
                # 큐에 추가하기 전에, queue의 (첫번째 값 - 1) == i 일 때
                # 차례로 왼쪽 큐부터 전 값 == 다음 값 + 1이 깨질 때 까지 실행
                if not len(queue) == 0 and (queue[0] - 1) == i:
                    while queue[0] == (queue[0] + 1):
                        queue.popleft()
                        temp += 1
                else:
                    queue.append(i)

    # progresses = [progresses[i] + speeds[i] for i in range(size) if progresses[i] < 100]
    # 100 이상일 경우 큐에 추가
    # [stack.append(i) for i in range(size) if progresses[i] >= 100]
