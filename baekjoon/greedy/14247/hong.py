from collections import defaultdict

n=int(input())
height=list(map(int,input().split()))
growing=list(map(int,input().split()))
tree_dict=defaultdict(int)
answer=0

for i in range(n):
    tree_dict[i]=growing[i]

sorted_dict=sorted(tree_dict.items(),key=lambda item:item[1])  #list of tuples
#(index, growing)
#[(4, 1), (0, 2), (2, 3), (3, 4), (1, 7)]

for i in range(n):
    answer+=height[sorted_dict[i][0]]
    height[sorted_dict[i][0]]=0
    for j in range(n):
        height[j]+=growing[j]
        
print(answer)

#1.나무 한그루 당 한번씩 베기
#2.자라는 길이가 적은 것부터 자르기 
