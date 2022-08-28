def solution(operations):
    heap = []
    for i in operations:
        com, num = i.split()
        num = int(num)
        if com == "I":
            heap.append(num)
            heap.sort()
        if com == "D" and num == 1 and heap:
            heap.pop()
        if com == "D" and num == -1 and heap:
            heap.pop(0)
    if not heap:
        return [0, 0]
    return [heap[-1], heap[0]]

print(solution(["I 1", "I 2", "I 3", "I 4", "I 5", "I 6", "I 7", "I 8", "I 9", "I 10", "D 1", "D -1", "D 1", "D -1", "I 1", "I 2", "I 3", "I 4", "I 5", "I 6", "I 7", "I 8", "I 9", "I 10", "D 1", "D -1", "D 1", "D -1"]))