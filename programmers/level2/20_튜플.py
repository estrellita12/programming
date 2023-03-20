def solution(s):
    answer = []
    s = s[2:-2]
    li = s.split("},{")
    li.sort(key=lambda x : len(x))
    
    for x in li:
        tmp = list(map(int,x.split(",")))
        for y in tmp:
            if y not in answer:
                answer.append(y)

    return answer

print("solution",solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print("solution",solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print("solution",solution("{{20,111},{111}}"))
print("solution",solution("{{123}}"))
print("solution",solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))

