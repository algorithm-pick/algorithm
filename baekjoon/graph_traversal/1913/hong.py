N=int(input())
K=int(input())

graph=[[0]*N for _ in range (N)]
#print(graph)
dx=[1,0,-1,0]   #아래, 오른, 위, 왼 순서
dy=[0,1,0,-1]

num=N*N
i=0
x,y=0,0
while True:
    graph[x][y]=num
    nx=x+dx[i]
    ny=y+dy[i]

    if nx>=N or ny>=N or graph[nx][ny]!=0 or nx<=-1 or ny<=-1:
        i+=1
        if i==4:
            i=0
        continue

    x,y=nx,ny
    num-=1
    if num==1:
        graph[x][y]=1
        break
k=0
w=0
for i in range(N):
    for j in range(N):
        if graph[i][j]==K:
            k=i+1
            w=j+1
    print(*graph[i])
print(k,w)
