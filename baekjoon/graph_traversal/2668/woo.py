import sys

def solution():
    input = sys.stdin.readline
    n = int(input())
    first = []
    second = []
    for i in range(1, n + 1):
        first.append(i)
        second.append(int(input()))
    while first:
        if set(first) == set(second):
            break
        for i in first:
            if i in second:
                continue
            del second[first.index(i)]
            first.remove(i)
    print(len(second))
    second.sort()
    for i in second:
        print(i)

solution()
