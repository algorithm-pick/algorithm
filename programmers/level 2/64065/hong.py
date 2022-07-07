def solution(s):
    answer=[]
    s=s[2:-2]   #list 
    s=s.split("},{")
    s.sort(key=len) #길이 순서대로 sort 
    
    for i in s:
        data=i.split(",")   #각각 배열에 
        for x in data:
            if int(x) not in answer:
                answer.append(int(x))
    
   
    return answer

    

s="{{2, 1, 3, 4},{2},{2, 1, 3},{2, 1}}"  #str
print(solution(s))
#s: 특정 튜플을 표현하는 집합이 담긴 문자열
#{{2, 1, 3, 4},{2},{2, 1, 3},{2, 1}} str
#['2,1,3,4}, {2}, {2, 1, 3}, {2, 1'] list 
#['2', '2, 1', '2, 1, 3', '2, 1, 3, 4']
