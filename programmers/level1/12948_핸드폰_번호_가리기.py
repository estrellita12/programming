def solution(phone_number):
    answer = ''
    strLen = len(phone_number)
    answer = (strLen-4)*'*'
    answer +=  phone_number[strLen-4:strLen]
    return answer

print(solution("01033334444")) # *******4444 
print(solution("027778888")) # *****8888

