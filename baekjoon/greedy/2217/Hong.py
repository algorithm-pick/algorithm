import sys

k=int(input())     #로프의 개수
arr=[]
ans=[]
for i in range(k):
    arr.append(int(input()))

arr.sort(reverse=True) #오름 차순 정렬 

for i in range(k):
    ans.append(arr[i]*(i+1))
    ''' 
    1 4 6 8 9
    9 8 6 4 1
    9
    8*2
    6*3
    4*4
    1*5
    '''
ans.sort(reverse=True)
print(ans[0])
    #w: 들 수 있는 최대 중량 => 구하고자 하는 것 
               

