T=int(input())
for i in range(T):
    sticker=[]
    N=int(input())
    for k in range(2):
        sticker.append(list(map(int,input().split())))
        
    for j in range(1,N):
        if j==1:
            sticker[0][j] += sticker[1][j - 1]
            sticker[1][j] += sticker[0][j - 1]
    else:
      sticker[0][j] += max(sticker[1][j - 1], sticker[1][j - 2])
      sticker[1][j] += max(sticker[0][j - 1], sticker[0][j - 2])

print(max(sticker[0][n - 1], sticker[1][n - 1]))
