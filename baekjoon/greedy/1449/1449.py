#greedy

N,L=map(int,input().split())
location=list(map(int,input().split()))

location.sort()
start=location[0]
end=location[0]+L
cnt=1

for i in range(N):
    if start<=location[i]<end:
        continue
    else:
        start=location[i]
        end=location[i]+L
        cnt+=1

print(cnt)
