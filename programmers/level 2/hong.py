def solution(s):
    answer=[]   #쪼갠 문자열의 길이

    if len(s)==1:
        return 1

    for i in range(1,(len(s)//2)+1):    #쪼갤 수 있는 최대 길이: 문자열의 반
        b='' #쪼갰을 때 나오는 문자열 저장
        cnt=1
        tmp=s[:i]

        for j in range(i,len(s),i):
            if tmp==s[j:i+j]:
                cnt+=1
            else:
                if cnt!=1:
                    b=b+str(cnt)+tmp
                else:
                    b=b+tmp
                tmp=s[j:j+i]
                cnt=1

        if cnt!=1:
            b=b+str(cnt)+tmp
        else:
            b=b+tmp

        answer.append(len(b))   #길이 저장

    return min(answer)
