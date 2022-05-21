def solution():
    n = int(input())
    people = list(map(int, input().split()))
    people.sort()
    answer = people[0]
    for i in range(1, n):
        people[i] = (people[i-1] + people[i])
        answer += people[i]
    print(answer)

solution()