
def getCnt(data,keymap):
    tot = 0
    for s in data:
        s_cnt = []
        for key in keymap:
            cnt = key.find(s)+1
            if cnt > 0:
                s_cnt.append(cnt)
        if len(s_cnt) <= 0:
            return -1
        else:
            tot += min(s_cnt)
    return tot

def solution(keymap, targets):
    answer = []
    for data in targets:
        answer.append(getCnt(data,keymap))
    return answer


print("solution",solution(["ABACD", "BCEFD"],["AAAAAAA","AABBZZ"]))
print("solution",solution(["ABACD", "BCEFD"],["ABCD","AABB"]))
print("solution",solution(["AA"],["B"]))
print("solution",solution(["AGZ", "BSSS"],["ASA","BGZ"]))
