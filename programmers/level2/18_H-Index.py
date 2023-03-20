
def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    print(citations)

    end = len(citations)
    if max(citations) < len(citations):
        end = max(citations)

    for h1 in range(end,0,-1):
        h2 = 0
        for j in range(len(citations)):
            if citations[j] >= h1:
                h2 = j+1
            else:
                break;
        h3 = len(citations) - j
        if h2 >= h1:
            #print(h1,"번 이상 인용된 논문이",h2,"편 이상이고 나머지 논문이",h3,"번 이하 인용되었다")
            answer = h1
            break; 
    
    return answer

print("solution",solution([350,452,877]))
print("solution",solution([4,7,7,6,5,5,3,0,0]))
#print("solution",solution([4,4,4,4,4,4,4,4,1,1,1]))
#print("solution",solution([1,1,1,1,1]))
#print("solution",solution([3,4]))
#print("solution",solution([3, 0, 6, 1, 5]))
#print("solution",solution([3, 0, 6, 1, 5,3]))
#print("solution",solution([3, 0, 6, 0,0,0,0,0,0]))
