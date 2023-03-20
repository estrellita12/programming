import re

def solution(new_id):
    answer = '' 

    tmp = new_id.lower() # 1단계
    tmp = re.sub("[^0-9a-z-_.]","",tmp) # 2단계
    tmp = re.sub("\.+",".",tmp) # 3 단계
    tmp = re.sub("(^\.|\.$)","",tmp) # 4 단계
    if len(tmp)<= 0 : # 5단계
        tmp = "a"
    if len(tmp) >= 16:
        tmp = tmp[:15]
        tmp = re.sub("\.$","",tmp)
    if len(tmp)<= 2:
        while True:
            tmp = tmp + tmp[-1]
            if len(tmp) >= 3:
                break;
    answer = tmp
    return answer


print("solution",solution("...!@BaT#*..y.abcdefghijklm"))
print("solution",solution("z-+.^."))
print("solution",solution("=.="))
print("solution",solution("123_.def"))
print("solution",solution("abcdefghijklmn.p"))

