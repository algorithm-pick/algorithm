def solution(n, computer):
    answer=0
    visited=[0]*n

    def dfs(index):     #하나의 네트워크
        visited[index]=1
        for j in range(n):
            if index!=j and computer[index][j]: #연결되어 있는데 
                if not visited[j]:  #방문 안했으면 dfs 재귀 호출 
                    dfs(j)
            
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer+=1
    
    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
#
