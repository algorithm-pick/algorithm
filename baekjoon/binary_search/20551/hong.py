import sys
input=sys.stdin.readline
N,M=map(int, input().split())
A=[]
Q=[]
answer=[]

for _ in range(N):
    A.append(int(input()))

for _ in range(M):
    Q.append(int(input()))

A.sort()    #B

for target in Q:   
    start=0
    end=N
    while start<end:
        mid=(start+end)//2
            
        if target<=A[mid]:
            end=mid
        else:
            start=mid+1
    
    if 0<=start<N and A[start]==target:
        answer.append(start)
    else:
        answer.append(-1)
               
for item in answer:
    print(item)   
