import sys

def solution(brown,yellow): 
    #yellow=x*y
    #brown=2(x+y)+4

    x=0
    sum=(brown-4)//2

    for i in range(sum):
        if i*(sum-i)==yellow:
            x=max(i,sum-i)
            break

    answer=[x+2,sum-x+2]
    return answer
    
brown=int(sys.stdin.readline())
yellow=int(sys.stdin.readline())
print(solution(brown,yellow))
