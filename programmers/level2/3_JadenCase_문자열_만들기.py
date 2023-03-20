def solution(s):
    answer = ''
    li = s.split(" ")
    #li = list(filter(lambda s : len(s)>0,li))
    res = list()
    for s in li:
        if len(s) > 1:
            tmp = s[0].upper()+s.lower()[1:]
        else:
            tmp = s.upper()
            
        res.append(tmp)
    answer = " ".join( s for s in res )
    return answer


print("solution",solution("aa"))
print("solution",solution("a 3d  3d"))
print("solution",solution("a   aaa"))
print("solution",solution("3people unFollowed me"))

