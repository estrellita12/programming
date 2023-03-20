def solution(s):
    answer = 0
    st = dict()
    st['zero'] = 0
    st['one'] = 1
    st['two'] = 2
    st['three'] = 3
    st['four'] = 4
    st['five'] = 5
    st['six'] = 6
    st['seven'] = 7
    st['eight'] = 8
    st['nine'] = 9
    for key in st.keys():
        s = s.replace(key,str(st[key]))
    answer = int(s)
    return answer

print("solution",solution("one4seveneight"))
print("solution",solution("23four5six7"))
print("solution",solution("2three45sixseven"))
print("solution",solution("123"))
