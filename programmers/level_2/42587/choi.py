def solution(priorities, location):
    answer = 0
    wait = len(priorities)

    while priorities:
        front = priorities.pop(0)
        location -= 1
        flag = True

        for i in priorities:
            if i > front:
                priorities.append(front)
                flag = False

                if location == -1:
                    location += wait
                break

        if flag:
            answer += 1
            if location == -1:
                return answer
                wait -= 1
