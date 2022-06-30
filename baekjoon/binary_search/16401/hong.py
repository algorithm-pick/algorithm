import sys

M, N = map(int, sys.stdin.readline().split())
cookies=list(map(int,sys.stdin.readline().split())) 

start=0
end=max(cookies)  
result=0
    
while(start<=end):
    ppl_cnt=0     #사람 수 
    mid=(start+end)//2 #주려는 과자의 길이
    if(mid==0):     #나누어줄 수 없으면 0을 출력
        total=0
        break
    
    for cookie in cookies:  
        if cookie>=mid:
            ppl_cnt+=(cookie//mid) 
                
    if ppl_cnt>=M:    #최대 길이가 아닌 것, ==M 정답 
        start=mid+1
        result=mid
            
    else:       #M명한테 못 나눠주면 end-- 종료 
        end=mid-1
    # print(start)
    # print(end)
    # print("/n")       
print(result) 
    
