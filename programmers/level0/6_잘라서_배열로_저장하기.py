def solution(my_str, n):
    answer = []
    for i in range(len(my_str)):
        sub = my_str[:n]
        my_str = my_str[n:]
        answer.append(sub)
        if len(my_str) <= 0 :
            return answer
    return answer


print("result",solution("abc1Addfggg4556b",6))
print("result",solution("abcdef123",3))
