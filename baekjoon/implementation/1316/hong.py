N = int(input())


group_word=0

for i in range(N):
    word=input()
    count = 0
    for index in range(len(word)-1):
        if word[index]!=word[index+1]:
            new_word=word[index+1:]
            if new_word.count(word[index])>0: #뒤 문자열에 현재 글자가 있으면
                count+=1

    if count==0:
        group_word+=1

print(group_word)
