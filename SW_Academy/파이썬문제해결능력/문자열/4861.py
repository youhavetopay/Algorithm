T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    board = []

    for i in range(N):
        # 공백없이 입력 받을때 이렇게 하면 리스트로 하나하나 들어감
        board.append(list(input()))
    answer = []
    
    # 전체에서
    for i in range(N):

        # 회문에 길이에 따른 검사할 덩어리 갯수 만큼
        for a in range(N-M+1):
            
            # 위아래 
            topBottomList = [board[j][i] for j in range(a, M+a)]
            # 일반 리스트
            leftRigthList = board[i][a:M+a]

            count = 0

            if answer == []:
                for j in range(M):
                    if topBottomList[j] == topBottomList[M-1-j]:
                        count += 1

                        # 반대로 했을 때도 같은거니까 반만 검사
                        if count > M//2:
                            answer = topBottomList
                    else:
                        count = 0
                        break
            else:
                break

            if answer == []:
                for j in range(M):
                    if leftRigthList[j] == leftRigthList[M-1-j]:
                        count += 1
                        if count > M//2:
                            answer = leftRigthList
                    else:
                        count =0
                        break
            else:
                break

        if answer != []:
            break
   


    print('#'+str(test_case), end=" ")
    for word in answer:
        print(word, end='')
    print()

    

    
    
    



    