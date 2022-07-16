from itertools import product

def solution(word) :
    alphabet=['A','E','I','O','U']
    arr=[]
    
    for i in range(1,6):
        arr+=list(map("".join,product(alphabet,repeat=i)))
    
    arr.sort()    
    for i in range(len(arr)):
        if(word==arr[i]):
            return i+1
print(solution('AAAE'))
