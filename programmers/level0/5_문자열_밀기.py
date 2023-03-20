def solution(A, B):
    answer = 0
    queue = list(A)
    for i in range(len(A)):
        if A == B:
            return answer
        last = A[-1]
        A = last+A[0:-1]
        answer = answer + 1
    return -1

print("result : ", solution("hello","ohell"))
print("result : ", solution("apple","elppa"))
print("result : ", solution("abc","abc"))


