def solution(numbers):
    answer = -1
    st = [i for i in range(10)]
    
    for i in numbers:
        if i in st:
            idx = st.index(i)
            st[idx] = 0
    answer = sum(st)
    return answer


print("solution",solution([1,2,3,4,6,7,8,0]))
print("solution",solution([5,8,4,0,6,7,9]))



