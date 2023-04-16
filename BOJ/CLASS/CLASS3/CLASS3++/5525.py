# 5525 IOIOI

'''
    나의 풀이
    I, O 으로 이루어진 문자열에서 I, O로 반복된 문자가 몇개 있는지 체크하는 문제

    나의 접근법
    처음에 단순히 슬라이싱 해서 하나하나 체크하는 방식으로 했는데
    부분 통과 됨
    도저히 어떻게 해야하는지 모르겠어서 질문 게시판에 가보니까
    IOIOIOI(n=3) 안에는 IOIOI(n=2)가 2개 있고 IOI(n=1) 가 3개 있다는 힌트를 알게됨

    그래서 스택을 활용해서
    IOIOI...이런식으로 계속 담다가
    잘못된 문자가 나온다면 스택에 담겨있는 문자를 체크하는 방식으로 풀게됨

    좀 많이 어려웠음..
    힌트 없었으면 못풀었을듯..,

'''


import sys
input = sys.stdin.readline

# N = int(input())
# M = int(input())
# S = input().strip()

N = 2
M = 7
S = 'IOIOIOI'

answer = 0

stack = []
for i in range(M):
    # 스택에 값이 있을 때
    if stack:
        # 스택의 마지막 문자랑 다를떄만 넣어주기
        if stack[-1] != S[i]:
            stack.append(S[i])
        else:
            # 마지막 문자가 I가 아니라면 빼주기
            if stack[-1] != 'I':
                stack.pop()
            
            # 최소 길이 3이상이어야 체크 가능함
            if len(stack) >= 3:
                # 스택에 담긴 문자의 n을 구하기
                now_n = (len(stack) - 3) // 2 + 1

                # 목표 N보다 클때 계산해서 넣어주기
                if now_n >= N:
                    answer += now_n - N + 1   

            # 스택 비우고
            # 새로운 문자 넣어주기
            stack = []
            stack.append(S[i])
    # 없을때
    else:
        # 문자는 I로 시작해야 하므로 I만 담음
        if S[i] == 'I':
            stack.append(S[i])
        
if stack:
    if stack[-1] != 'I':
        stack.pop()

    if len(stack) >= 3:
        now_n = (len(stack) - 3) // 2 + 1
        if now_n >= N:
            answer += now_n - N + 1

print(answer)




'''
    다른 사람 풀이
    https://black-hair.tistory.com/135

    조금씩 확인하면서 연속된 개수를 찾고 index를 2번 올리고
    연속된 개수가 목표 N라면 정답 개수를 올려주는 방식으로 품

    오.. 깔끔해서 보기 좋은듯.. ㅋㅋㅋ
    처음엔 이것도 슬라이싱 하는데 오래걸리지 않나..?? 라고 생각했었는데
    이거는 M * 3이고 예전에 풀이는 N * M 이라서 훨씬 느림 ㅋㅋ
'''


N = int(input())
M = int(input())
S = input()

answer, i, count = 0, 0, 0

while i < (M - 1):
    if S[i:i+3] == 'IOI':
        i += 2
        count += 1
        if count == N:
            answer += 1
            count -= 1
    else:
        i += 1
        count = 0

print(answer)