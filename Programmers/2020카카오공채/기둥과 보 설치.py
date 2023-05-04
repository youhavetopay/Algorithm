BUILD = 1

PILLAR = 0

def checkCanBuildPillar(x, y, board):

    # 기둥의 높이가 board를 초과하는 경우
    if y + 2 >= len(board):
        return False

    # 해당 위치가 바닥일때
    if y == 0:
        return True
    
    # 밑에 기둥이 있을 때
    if board[y][x] == 1:
        return True
    
    # 밑에 보가 있고 해당 부분이 보의 끝부분 일때
    if board[y][x] == 2:
        if x - 1 >= 0 and board[y][x-1] == 0:
            return True
        
        if x + 1 < len(board) and board[y][x+1] == 0:
            return True
    
    # 이외에는 못 지음
    return False

def checkCanBuildLine(x, y, board):

    # 보의 길이가 board를 초과하는 경우
    if x + 2 >= len(board):
        return False
    
    # 한쪽 끝이 기둥인 경우
    if board[y][x] == 1 or board[y][x+2] == 1:
        return True
    
    # 양쪽끝이 보일 경우
    if board[y][x] == 2 and board[y][x+2] == 2:
        return True
    
    return False

def checkCanDeletePiller(x, y, board):

    if y + 3 < len(board):

        # 해당 기둥 위에 기둥 있음
        if board[y+3][x] == 1:
            return False

        # 해당 기둥위에 보가 있고
        # 해당 보 옆에 기둥이 없을 때
        if board[y+3][x] == 2:

            # 오른쪽
            if x + 2 < len(board) and board[y+3][x+2] != 1:
                return False
            
            # 왼쪽
            if x - 2 >= 0 and board[y+3][x-2] != 1:
                return False

    return True

def checkCanDeleteLine(x, y, board):

    # 나의 오른쪽 끝에 기둥이 있는데
    # 그 밑에 기둥이 없을 때
    if x + 2 < len(board) and y + 1 < len(board):

        # 밑에 기둥은 없지만 받혀주는 보가 있을때
        if board[y+1][x+2] == 1 and board[y][x+2] == 2:
            return True
        
        if board[y+1][x+2] == 1 and y - 1 >= 0 and board[y-1][x+2] != 1:
            print(1)
            return False
        

    
    # 나의 왼쪽 끝에 기둥이 있는데
    # 그 밑에 기둥이 없을 때
    if y + 1 < len(board):

        # 밑에 기둥은 없지만 받혀주는 보가 있을 때
        if board[y+1][x] == 1 and x - 1 >= 0 and board[y][x-1] == 2:
            return True

        if board[y+1][x] == 1 and y - 1 >= 0 and board[y-1][x] != 1:
            print(2)
            return False

    # 왼쪽에 보가 있고 
    # 왼쪽 보가 기둥에 안걸쳐 있을때
    if x - 2 >= 0:
        if board[y][x-1] == 2 and board[y-1][x-2] != 1 and board[y-1][x] != 1:
            print(3)
            return False
    
    # 오른쪽에 보가 있고 
    # 오른쪽 보가 기둥에 안걸쳐 있을때
    if x + 4 < len(board):
        if board[y][x+3] == 2 and board[y-1][x+2] != 1 and board[y-1][x+4] != 1:
            print(4)
            return False
    

    return True


def solution(n, build_frame):

    '''
        나의 풀이(못품 ㅠㅠ)

        기둥과 보를 규칙에 따라 설치하고 삭제할 때
        최종적으로 남아있는 구조물의 정보를 반환하는 문제

        나의 접근법
        못풀어서 큰 의미는 없지만... ㅠㅠ
        그냥 규칙대로 구현하는 방식으로 체크함
        2차원 리스트를 N+1 * 2의 크기로 만들고
        해당 위치에서 그려나감

        규칙에 따라 기둥은 1, 보는 2로 표현을 하는데
        삭제 시나리오가 너무 생각해야하는게 많은듯...
        내가 떠올리지 못한 시나리오가 있거나 생성 규칙에도 빈틈이 있을 수 있는듯..
        너무 확인해야하는 케이스가 너무 많아서 그런지 너무 복잡함.. ㅠㅠㅠ
    '''

    board = [[0] * ((n+1)*2) for _ in range((n+1)*2)]

    build_structs = []

    for x, y, a, b in build_frame:
        x *= 2
        y *= 2
        if b == BUILD:
            if a == PILLAR:
                if checkCanBuildPillar(x, y, board):
                    board[y][x] = 1
                    board[y+1][x] = 1
                    board[y+2][x] = 1
                    build_structs.append([x//2, y//2, a])
            elif checkCanBuildLine(x, y, board):
                if board[y][x] == 0:
                    board[y][x] = 2
                if board[y][x+1] == 0:
                    board[y][x+1] = 2
                if board[y][x+2] == 0:
                    board[y][x+2] = 2

                build_structs.append([x//2, y//2, a])
        else:

            if a == PILLAR:
                if checkCanDeletePiller(x, y, board):
                    if x - 1 >= 0 and x + 1 < len(board):
                        if board[y][x-1] == 2 and board[y][x+1] == 2:
                            board[y][x] = 2
                        else:
                            board[y][x] = 0

                        if board[y+1][x-1] == 2 and board[y+1][x+1] == 2:
                            board[y+1][x] = 2
                        else:
                            board[y+1][x] = 0

                        if board[y+2][x-1] == 2 and board[y+2][x+1] == 2:
                            board[y+2][x] = 2
                        else:
                            board[y+2][x] = 0
                    else:
                        board[y][x] = 0
                        board[y+1][x] = 0
                        board[y+2][x] = 0

                    if [x//2, y//2, a] in build_structs:
                        build_structs.pop(build_structs.index([x//2, y//2, a]))
            elif checkCanDeleteLine(x, y, board):
                if  board[y][x] == 2:
                    if x - 1 >= 0 and board[y][x-1] == 2:
                        board[y][x] = 2
                    else:
                        board[y][x] = 0
                if board[y][x+1] == 2:
                    board[y][x+1] = 0
                if board[y][x+2] == 2:
                    if x + 3 < len(board) and board[y][x+3] == 2:
                        board[y][x+2] = 2
                    else:
                        board[y][x+2] = 0
                
                if [x//2, y//2, a] in build_structs:
                    build_structs.pop(build_structs.index([x//2, y//2, a]))


    for l in reversed(board):
        print(l)

    print()

    build_structs.sort(key=lambda x:(x[0], x[1], x[2]))

    return build_structs

print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))


def impossible(result):
    COL, ROW = 0, 1
    for x, y, a in result:

        # 기둥
        if a == COL:
            # y는 0이 아니고
            # y-1 부분에 기둥이 없고
            # 보가 밑에 없으면 안됨
            if y != 0 and (x, y-1, COL) not in result and \
            (x-1, y, ROW) not in result and (x, y, ROW) not in result:
                return True
        
        # 보
        else: 
            # 자신의 왼쪽 끝에 받혀주는 기둥이 없고
            # 자신의 오른쪽 끝에 받혀주는 기둥이 없고
            # 양쪽 끝에 보가 없으면 안됨
            if (x, y-1, COL) not in result and (x+1, y-1, COL) not in result and \
            not ((x-1, y, ROW) in result and (x+1, y, ROW) in result):
                return True
        
    return False

def firstSolu(n, build_frame):

    '''
        다른 사람 풀이
        https://velog.io/@tjdud0123/%EA%B8%B0%EB%91%A5%EA%B3%BC-%EB%B3%B4-%EC%84%A4%EC%B9%98-2020-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EA%B3%B5%EC%B1%84-python

        간단해서...너무 허무함..ㅠㅠㅠㅠㅠㅠ

        set에 담거나 제거 하면서 현재 저장한 것들에 대해
        유효성을 판별하는 방식으로 품

        굳이 2차원 리스트에 해당 모양을 구현할 필요가 없다는 사실이 너무,,,......허무함..ㅠㅠ
    '''

    result = set()

    # 하나 하나 해보면서 전체의 유효성을 검사
    # 불가능 하다면 해당 작업 되돌리기
    for x, y, a, build in build_frame:
        item = (x, y, a)

        if build:
            result.add(item)
            if impossible(result):
                result.remove(item)
        elif item in result:
            result.remove(item)
            if impossible(result):
                result.add(item)

    answer = map(list, result)

    return sorted(answer, key = lambda x : (x[0], x[1], x[2]))