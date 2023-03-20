def solution(n):
    answer = 0
    flag = True
    data = n
    while flag:
        data = data + 1
        cnt1 = bin(n).count("1")
        cnt2 = bin(data).count("1")
        #print(cnt1,cnt2,data)
        if cnt1 == cnt2:
            answer = data
            break
    return answer


print("solution",solution(78))
print("solution",solution(15))



