def solution(dirs):

    '''
        나의 풀이
        좌표평면에서 명령어에 따라 이동을 하는데
        내가 처음가보는 길의 개수를 계산하는 문제

        나의 접근법
        처음엔 BFS느낌으로 하려고 했는데
        이게 도착한 위치를 체크하는게 아니라 이동한 길을 체크하는 거라서
        다시 생각해보니까 그냥 좌표값으로 이동시켜도 될것 같아서 그렇게 함
        그 후 set에다가 원래 위치와 다음에 도착할 점을 넣어줘서 체크했는데 8번부터 실패함

        좀 더 생각하다가 잘 모르곘어서 힌트봤는데 왼쪽에서 오른쪽 간거랑 오른쪽에서 왼쪽으로 간건 하나로 친다고 해서
        정렬해서 넣어봤는데 이게 좌표평면이다 보니 원점근처에서 왔다갔다하면 정렬도 답이 아니였음
        그래서 다시 생각했는데
        그냥 현재 지점에서 다른지점, 다른지점에서 현재지점 의 좌표값이 있는지 visited에서 검사하고
        없으면 걍 넣어주면 되었음 ㅋㅋ

        처음에 좌표평면 보이길래 수학문제구나 라고 생각했지만
        그게 아니여서 좀 가볍게 봤는데
        생각보다 푸는데 오래걸렸음..
    '''

    vectors = {'U' : [0, 1], 'D' : [0, -1], 'R' : [1, 0], 'L' : [-1, 0]}

    visited = set()

    x, y = 0, 0
    for direction in dirs:
        dx, dy = vectors[direction]
        next_x, next_y = x + dx, y + dy

        if -5 <= next_x <= 5 and -5 <= next_y <= 5:
            if (x, y, next_x, next_y) not in visited and (next_x, next_y, x, y) not in visited:
                visited.add((x, y, next_x, next_y))
            
            x, y = next_x, next_y

    return len(visited)

print(solution("LURDLURDLURDLURDRULD"))



def firstSolu(dirs):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/49994/solution_groups?language=python3

        그냥 정방향 역방향 다 넣어주고 마지막엔 길이의 절반
        
        엥?? 나도 이렇게 했었던것 같은데.. 난 실패했던것 같은디..
    '''

    s = set()
    d = {'U' : [0, 1], 'D' : [0, -1], 'R' : [1, 0], 'L' : [-1, 0]}
    x, y = 0, 0

    for i in dirs:
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x, y, nx, ny))
            s.add((nx, ny, x, y))
            x, y = nx, ny
    
    return len(s) // 2