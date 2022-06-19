#42586
import math
def solution(progresses, speeds):
    answer=[]
    days=[]
    cnt=0

    for i in range(len(progresses)):
        days.append(math.ceil((100-progresses[i])/speeds[i]))
        print(days[i])

    temp = days[0]

    for i in range(len(progresses)):
        if(days[i]<=temp):
            cnt+=1
        else:
            temp=days[i]
            answer.append(cnt)
            cnt=1
        if (i == len(progresses) - 1):
            answer.append(cnt)


    return answer

progresses=[93,30,55,60,40,65]
speeds=[1,30,5,10,60,7]

print(solution(progresses,speeds))
