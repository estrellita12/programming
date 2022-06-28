# https://programmers.co.kr/learn/courses/30/lessons/64061
def solution(board, moves):
    # 터진 인형의 갯수
        answer = 0
            # 뽑은 인형을 담을 바구니
    box = list()
    # 인형 게임판의 크기
    size = len(board)

    for k in moves:
        idx = k-1
        for i in range(size):
            if board[i][idx]!=0:
                # 인형을 발견하면 인형을 뽑아 box에 담는다
                box.append(board[i][idx])
                board[i][idx] = 0
                if len(box)>=2:
                    if box[-1]==box[-2]:
                        #del box[-1]
                        #del box[-1]
                        box.pop()
                        box.pop()
                        answer+=2
                break
    return answer
