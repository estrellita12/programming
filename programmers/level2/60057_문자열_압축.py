def solution(s):
    length = len(s)
    limit = int(length/2) + 1
    arr = list()
    for k in range(1,limit):
        #print(str(k)+"번째 단위")
        compress = ""
        pre = ""
        cnt = 1
        for i in range(0,length,k):
            tmp = (s[i:i+k])
            #print(tmp+"/"+pre)
            if pre!="" :
                if tmp == pre:
                    cnt=cnt+1
                else:
                    if cnt==1 :
                        compress = compress+pre
                    else:
                        compress = compress+str(cnt)+pre
                    cnt = 1
            pre = tmp
        if cnt==1 :
            compress = compress+pre
        else:
            compress = compress+str(cnt)+pre
        arr.append(compress)
        
    answer = len(s)
    for j in arr:
        if answer > len(j) :
            answer = len(j)

    return answer


print(solution("aabbaccc")) #7
print(solution("ababcdcdababcdcd")) #9
print(solution("abcabcdede")) #8
print(solution("abcabcabcabcdededededede")) #14
print(solution("xababcdcdababcdcd")) #17
print(solution("aabaabaabaabaabaabdasfasd"))

