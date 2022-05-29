import sys
A=list(sys.stdin.readline().strip())
B=list(sys.stdin.readline().strip())

count=0

if(sorted(A)!=sorted(B)):
    print(-1)
    exit()

curr=len(A)-1
ans=0
if curr==0:
    if A==B:
        print(0)
    else:
        print(-1)

for i in range(len(A)-1,-1,-1):
    if A[i]!=B[curr]:
        ans+=1
    else:
        curr-=1

print(ans)
