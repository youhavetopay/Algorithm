def counterList(board, target):

    count = 0
    for line in board:
        count += line.count(target)
    
    return count

def rotateLeftKey(key):

    rotate_key = []

    for i in range(len(key[0])):
        line = []
        for j in range(len(key)-1, -1, -1):
            line.append(key[j][i])
        rotate_key.append(line)

    return rotate_key

def checkKeyOfLock(key, lock, lock_count):

    count = 0

    for l in key:
        print(l)
    print('--------')
    for l in lock:
        print(l)
    
    print()


    for key_line, lock_line in zip(key, lock):
        for key_val, lock_val in zip(key_line, lock_line):
            if key_val == 1 and lock_val == 0:
                count += 1
            
            if key_val == 1 and lock_val == 1:
                return False

    return count == lock_count


def markKeyOfLock(key, lock, lock_count):

    # 대충 2차원 리스트 슬라이딩 윈도우 하는 코드 ㅋㅋ
    # key의 크기는 lock보다 작거나 같아서 key를 기준으로 하면됨
    # 비교해야하는 key와 lock을 잘라와서 체크하는 방식으로 품

    # 열쇠를 걸쳐서 푸는 경우도 있으니 하나하나 다 체크해야함..


    # 상단
    for y in range(len(key)-1):

        # 상단 왼쪽
        print('상단 왼쪽')
        for j in range(1, len(key[0])):
        
            temp_key = []
            temp_lock = []

            i = -y - 1
            while i < 0:
                now_line_key = key[i][len(key[0]) - j : len(key[0])]
                temp_key.append(now_line_key)
                i += 1
            
            for i in range(0, y+1):
                now_line_lock = lock[i][0:j]
                temp_lock.append(now_line_lock)

            
            if checkKeyOfLock(temp_key, temp_lock, lock_count):
                return True
            
        # 상단 중간
        print('상단 중간')
        for j in range(len(lock[0]) - len(key[0]) + 1):

            temp_key = []
            temp_lock = []

            i = -y - 1
            while i < 0:
                now_line_key = key[i]
                temp_key.append(now_line_key)
                i += 1
            
            for i in range(0, y+1):
                now_line_lock = lock[i][j:j+len(key[0])]
                temp_lock.append(now_line_lock)
            
            if checkKeyOfLock(temp_key, temp_lock, lock_count):
                return True

        # 상단 오른쪽
        print('상단 오른쪽')
        for j in range(1, len(key[0])):

            temp_key = []
            temp_lock = []

            i = -y - 1
            while i < 0:
                now_line_key = key[i][0 : len(key[0]) - j]
                temp_key.append(now_line_key)
                i += 1
            
            for i in range(0, y+1):
                now_line_lock = lock[i][-len(key) + j:]
                temp_lock.append(now_line_lock)
            
            if checkKeyOfLock(temp_key, temp_lock, lock_count):
                return True




    # 가운데
    for y in range(len(lock) - len(key) + 1):

        # 가운데 왼쪽
        print('가운데 왼쪽')
        for j in range(1, len(key[0])):
        
            temp_key = []
            temp_lock = []

            for i in range(len(key)):
                now_line_key = key[i][len(key[0]) - j : len(key[0])]
                temp_key.append(now_line_key)

            for i in range(len(key)):
                now_line_lock = lock[y+i][0:j]
                temp_lock.append(now_line_lock)
            
            if checkKeyOfLock(temp_key, temp_lock, lock_count):
                return True
        
        # 가운데 중간
        print('가운데 중간')
        for j in range(len(lock[0]) - len(key[0]) + 1):
            temp_key = []
            temp_lock = []

            for i in range(len(key)):
                now_line_key = key[i]
                temp_key.append(now_line_key)
            
            for i in range(len(key)):
                now_line_lock = lock[y+i][j:j+len(key[0])]
                temp_lock.append(now_line_lock)
            
            if checkKeyOfLock(temp_key, temp_lock, lock_count):
                return True
        
        # 가운데 오른쪽
        print('가운데 오른쪽')
        for j in range(1, len(key[0])):
            temp_key = []
            temp_lock = []

            for i in range(len(key)):
                now_line_key = key[i][0 : len(key[0]) - j]
                temp_key.append(now_line_key)
            
            for i in range(len(key)):
                now_line_lock = lock[y+i][-len(key) + j:]
                temp_lock.append(now_line_lock)
            
            if checkKeyOfLock(temp_key, temp_lock, lock_count):
                return True

    
    # 하단
    for y in range(1, len(key)):
        
        # 하단 왼쪽
        print('하단 왼쪽')
        for j in range(1, len(key[0])):
        
            temp_key = []
            temp_lock = []

            for i in range(len(key)-y):
                now_line_key = key[i][len(key[0]) - j : len(key[0])]
                temp_key.append(now_line_key)
            
            i = -len(key) + y
            while i < 0:
                now_line_lock = lock[i][0:j]
                temp_lock.append(now_line_lock)
                i += 1
            
            if checkKeyOfLock(temp_key, temp_lock, lock_count):
                return True


        # 하단 중간
        print('하단 중간')
        for j in range(len(lock[0]) - len(key[0]) + 1):
            temp_key = []
            temp_lock = []

            for i in range(len(key)-y):
               now_line_key = key[i]
               temp_key.append(now_line_key)
            
            i = -len(key) + y
            while i < 0:
                now_line_lock = lock[i][j:j+len(key[0])]
                temp_lock.append(now_line_lock)
                i += 1
            
            if checkKeyOfLock(temp_key, temp_lock, lock_count):
                return True
        
        # 하단 오른쪽
        print('하단 오른쪽')
        for j in range(1, len(key[0])):
            temp_key = []
            temp_lock = []

            for i in range(len(key)-y):
               now_line_key = key[i][0 : len(key[0]) - j]
               temp_key.append(now_line_key)
            
            i = -len(key) + y
            while i < 0:
                now_line_lock = lock[i][-len(key) + j:]
                temp_lock.append(now_line_lock)
                i += 1
            
            if checkKeyOfLock(temp_key, temp_lock, lock_count):
                return True

    return False


def solution(key, lock):

    '''
        나의 풀이 (..... 4시간 걸림..)
        2차원 리스트 이리저리 이동시키고 돌려가면서
        자물쇠에 맞는 열쇠인지 체크하는 문제

        나의 접근법...ㅋㅋㅋ
        열쇠를 반전은 못시키고 회전이랑 이동만 가능해서
        회전시키면서 슬라이딩 윈도우 기법으로 하는 방법으로 함
        대충 이미지 처리에서 윈도우 기법??? 정도로 생각하면 될듯.. ㅋㅋ

        와...진짜 이거 원리는 아는데 이걸 구현하려고 하니까
        진~~~~~~짜 겁나 어려웠음.. ㅠㅠ
        새삼 numpy랑 openCV 가 그리워지는 순간이였음 ㅋㅋㅋㅋㅋ
        근데 이게 맞나 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
    '''

    # 1의 개수 구하기
    key_count = counterList(key, 1)
    # 0의 개수 구하기
    lock_count = counterList(lock, 0)

    # 채워야 하는 구멍이 열쇠의 돌기 부분이 더 많을 때
    # 다 못채우니 False
    if lock_count > key_count:
        return False

    
    rotated_key = []
    
    # 90도 회전시키면서 슬라이딩 윈도우 하기 ㅋㅋ
    for i in range(4):
        if not rotated_key:
            rotated_key = rotateLeftKey(key)
        else:
            rotated_key = rotateLeftKey(rotated_key)

        for l in rotated_key:
            print(l)

        print()

        # 한번이라도 성공하면 
        # 해당 열쇠로 자물쇠를 열 수 있음
        if markKeyOfLock(rotated_key, lock, lock_count):
            return True
        

    return False

# print(solution(
#     [
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]
#     ],


#     [
#         [1, 2, 3, 4],
#         [5, 6, 7, 8],
#         [9, 10, 11, 12],
#         [13, 14, 15, 16]
#     ]))
# [7, 4, 1]
# [8, 5, 2]
# [9, 6, 3]

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))



def check_match(lock, key):
    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] + key[i][j] != 1:
                return False
    
    return True

def firstSolu(key, lock):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이

        나랑 거의 비슷하게 푼듯....?? ㅋㅋ
    '''

    m = len(key[0])
    n = len(lock[0])

    new_key_0 = [[0] * n for _ in range(n)]
    new_key_1 = [[0] * n for _ in range(n)]
    new_key_2 = [[0] * n for _ in range(n)]
    new_key_3 = [[0] * n for _ in range(n)]

    for i in range(m):
        for j in range(m):
            new_key_0[i][j] = key[i][j]
            new_key_1[j][m-i-1] = key[i][j]
            new_key_2[m-i-1][m-j-1] = key[i][j]
            new_key_3[m-j-1][j] = key[i][j]

    for key in [new_key_0, new_key_1, new_key_2, new_key_3]:
        for i in range(n):
            for j in range(n):
                left_up_key = [row[i:] + [0]*i for row in key[j:]] + [[0]*n]*j
                if check_match(lock, left_up_key):
                    return True
                
                left_down_key = [[0]*n]*(n-j-1) + [row[i:] + [0]*i for row in key[:j+1]]
                if check_match(lock, left_down_key):
                    return True

                right_up_key = [[0]*i + row[:n-i] for row in key[j:]] + [[0]*n]*j
                if check_match(lock, right_up_key):
                    return True
                
                right_down_key = [[0]*n]*(n-j-1) + [[0]*i + row[:n-i] for row in key[:j+1]]
                if check_match(lock, right_down_key):
                    return True
        
    return False