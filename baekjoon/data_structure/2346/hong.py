#2346
N=int(input())
balloon=[]
paper=list(map(int,input().split()))
temp=0        #인덱스 
temp2=0       #인덱스+paper에 있는 수 
answer=[]
for i in range(N):
    balloon.append(i+1)
    
while balloon:
    if(len(balloon)==1):
        answer.append(balloon[0])
        balloon.remove(balloon[0])
    else:
        temp2=temp+paper[temp]    

        if temp2>=0:
            if temp2>temp:
                temp2=temp2-1  #temp2=2
        else:
            temp2=(len(balloon)-2)-(abs(temp2)-1)

        
        answer.append(balloon[temp])     
        balloon.remove(balloon[temp])
        paper.remove(paper[temp])

        temp=temp2

        
for j in answer:
    print(j, end=' ')
