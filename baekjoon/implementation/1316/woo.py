import sys

def solution():
    input = sys.stdin.readline
    n = int(input())
    answer = 0
    for _ in range(n):
        word = input()
        temp = [word[0]]
        for i in range(1, len(word) - 1):
            if word[i-1] != word[i]:
                temp.append(word[i])
        if len(list(set(temp))) == len(temp):
            answer += 1
    print(answer)

solution()