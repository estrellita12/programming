
def solution(s, skip, index):
    answer = ''
    alpa = []
    for num in range(97,123):
        if skip.find(chr(num)) < 0:
            alpa.append(chr(num))
    print(alpa)
    for char in s:
        idx = (alpa.index(char) + index)%len(alpa)
        answer += alpa[idx]
    return answer


print("solution",solution("zxvzxqweetretyytuiopi","abcdcfg",5))
print("solution",solution("aukks","wbqd",1))

