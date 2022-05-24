N=int(input()) #도시 개수
dist=list(map(int, input().split()))
price=list(map(int, input().split()))
total=0

for i in range(len(dist)):
    if(price[i+1]>price[i]):
        price[i+1]=price[i]

for i in range(len(dist)):
    total+=price[i]*dist[i]

print(total)
