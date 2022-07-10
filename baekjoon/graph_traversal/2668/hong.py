N=int(input())
arr=[0]

answer=set()    #집합

for i in range(N):
    arr.append(int(input()))
    
def dfs(first, second, num):
    first.add(num)
    second.add(arr[num])
    if arr[num] in first:   
        if first==second:
            answer.update(first)
            return True
        return False
    return dfs(first,second,arr[num])   #아니면 다음 dfs 실행 
 
for i in range(1,N+1):  #1~7
    if i not in answer:     #i가 answer에 없는 경우에만 
        dfs(set(),set(),i)  
        
print(len(answer))
print(*sorted(list(answer)),sep='\n')      
    


