
def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        a1 = str(bin(arr1[i]))[2:]
        a1 = "0"*(n-len(a1))+a1
        a2 = str(bin(arr2[i]))[2:]
        a2 = "0"*(n-len(a2))+a2
        addr = ""
        for j in range(n):
            if a1[j] == "0" and a2[j] == "0" :
                addr = addr+" "
            else:
                addr = addr+"#"
        answer.append(addr)
    return answer

print("solution",solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))

