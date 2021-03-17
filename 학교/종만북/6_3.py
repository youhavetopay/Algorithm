# c = int(input())

# nList = []

# mList = []

# answers = []

# tempList = []
# for i in range(c):
#     nList.append(list(map(int, input().split(' '))))
#     mList.append(list(map(int, input().split(' '))))
    
    
#     for x in range(0, nList[i][1]*2, 2):
#         tempList.append(mList[i][x:x+2])

# print(tempList)

# ans = 0
# N , M = 0, 0
# areFriends = [[False for _ in range(10)] for _ in range(10)]
# havePair = [False for _ in range(10)]

# def counting(n):
#     global ans
#     finished = True
#     frist = -1
#     for i in range(N):
#         if not havePair[i]:
#             finished = False
#             frist = i
#             break
    
#     if finished:
#         ans +=1
        
#         return
    
#     for j in range(frist+1, N):
#         if (not havePair[frist]) and (not havePair[j]) and areFriends[frist][j]:
#             havePair[frist] = True
#             havePair[j] = True
#             counting(n+1)
#             havePair[frist] = False
#             havePair[j] = False
    
#     return

# tc = int(input())

# for t in range(1, tc+1):
#     mList = []
#     ans = 0
    
#     areFriends = [[False for _ in range(10)] for _ in range(10)]
#     havePair = [False for _ in range(10)]
    
#     N, M = map(int, input().split())
#     tempList = list(map(int, input().split()))
#     for i in range(M):
#         a = tempList[2*i]
#         b = tempList[2*i+1]
#         areFriends[a][b] = True
#         areFriends[b][a] = True
    
#     counting(0)

#     print(ans)

    
c = int(input())
answers = []

divFriendList= []

for i in range(c):
    n, m = map(int, input().split())

    friendList = list(map(int, input().split()))
    
    answer = 0

    divFriendList = [friendList[x*2 : x*2+2] for x in range(m)]

    print(divFriendList)
    # convList = []
    # checkList = [-1 for _ in range(int(n/2))]
    # remember = -1
    # for x in range(m):
    #     if divFriendList[x][0] not in convList and divFriendList[x][1] not in convList:
    #         convList.append(divFriendList[x][0])
    #         convList.append(divFriendList[x][1])
    #         for y in range(int(n/2)):
    #             if checkList[y] == -1:
    #                 checkList[y] = x
    #                 remember = y

    #     if len(convList) >= int(n/2):
    #         answer+=1
    #         del convList[-1]
    #         del convList[-1]

        # for y in range(x+1, 9):
        #     if (divFriendList[y][0] not in checkList) and (divFriendList[y][1] not in checkList):
        #         checkList.append(divFriendList[y][0])
        #         checkList.append(divFriendList[y][1])
                
        #         for z in range(y+1, 10):
        #             print(checkList, divFriendList[z][0], divFriendList[z][1])
        #             if (divFriendList[z][0] not in checkList) and (divFriendList[z][1] not in checkList):
        #                 answer += 1
                
        #         del checkList[-1]
        #         del checkList[-1]
    
    answers.append(answer)

print(answers)
