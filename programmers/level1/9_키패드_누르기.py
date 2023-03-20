addr = [ [1,2,3],[4,5,6],[7,8,9],['*',0,'#'] ]
visited = [ [0,0,0],[0,0,0],[0,0,0],[0,0,0] ]

def show():
    for x in visited:
        print(x[0],x[1],x[2])

def bfs():
    show()
    queue = list()
    queue.append([1,1])
    dst = [2,2]
    while True:
        if len(queue)<=0:
            break

        point = queue.pop(0)
        i = point[0];
        j = point[1];
        if i+1 < len(addr) and i+1 <= dst[0]:
            visited[i+1][j] = visited[i][j] + 1
            queue.append([i+1,j])
        if j+1 < len(addr[0]) and j+1 <= dst[1]:
            visited[i][j+1] = visited[i][j] + 1
            queue.append([i,j+1])
        
    show()
    print(visited[dst[0]][dst[1]])

def solution(numbers, hand):
    answer = ''
    addr = dict()
    addr[1] = [0,0]
    addr[2] = [0,1]
    addr[3] = [0,2]
    addr[4] = [1,0]
    addr[5] = [1,1]
    addr[6] = [1,2]
    addr[7] = [2,0]
    addr[8] = [2,1]
    addr[9] = [2,2]
    addr[0] = [3,1]
    leftList = [1,4,7]
    rightList = [3,6,9]
    left = [3,0]
    right = [3,2]
    for x in numbers:
        if x in leftList:
            left = addr[x]  
            answer = answer+"L"
        elif x in rightList:
            right = addr[x]
            answer = answer+"R"
        else:
            leftLen = abs(left[0]-addr[x][0])+abs(left[1]-addr[x][1])
            rightLen = abs(right[0]-addr[x][0])+abs(right[1]-addr[x][1])
            #print(left,leftLen," / ",right,rightLen)
            if leftLen < rightLen : 
                left = addr[x]  
                answer = answer+"L"
            elif leftLen > rightLen : 
                right = addr[x]
                answer = answer+"R"
            else:
                if hand=="right":
                    right = addr[x]
                    answer = answer+"R"
                else:
                    left = addr[x]  
                    answer = answer+"L"
    return answer

print("solution",solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))
print("solution",solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left"))


























