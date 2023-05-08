class Node:
    def __init__(self, idx):
        self.idx = idx
        self.left = None
        self.right = None
        return

def insertNodeTail(tail):

    new_idx = tail.idx + 1
    new = Node(new_idx)
    tail.right = new
    new.left = tail

    return new

def deleteNode(now, head, delete_nodes):

    # 삭제할려는 노드 담아주기
    delete_nodes.append(now)
    new_head = head

    # 연결 해제 시키기
    pre = now.left
    next = now.right
    pre.right = next
    next.left = pre

    # head를 삭제한 경우
    if now == head:
        new_head = next

    # 끝부분을 삭제하는 경우
    if next == head:
        now = pre

    # 중간을 삭제하는 경우
    else:
        now = next
    
    return now, new_head

def insertNodeMiddle(insert_node, head):

    # 기존 연결 정보로 연결 시켜주기
    pre = insert_node.left
    next = insert_node.right

    pre.right = insert_node
    next.left = insert_node

    # 지금 head보다 더 낮은 데이터를 넣은 경우
    # head 갱신하기
    if head.idx > head.left.idx:
        head = head.left

    return head
    


def solution(n, k, cmd):

    '''
        나의 풀이
        데이터를 명령어에 따라 삭제하고 복구 시키는 문제

        나의 접근법
        이중 연결리스트로 구현함
        효율성 부분은 삭제하는 노드만 따로 저장해두고
        연결을 해재 시켜줌 -> 대신 삭제하는 노드는 건들지 않기 -> 기존 연결정보 가지고 있게
        그 후 다시 삽입 할때 기존 연결 정보를 활용해서 바로 넣어주고 head를 업데이트 해주는 방식으로 하니
        금방 해결됨 ㅎㅎ

        2년전 이 문제 진짜 노답이였는데 ...ㅋㅋㅋ
        3시간 걸렸긴 하지만 그래도 내 힘으로 풀어서 기분 좋음 ㅎㅎ
    '''
    # 처음 head 설정
    head = Node(0)
    p = head
    i = 1
    # 데이터 넣어주기
    while i < n:
        p = insertNodeTail(p)
        i += 1
    
    # 이중 원형 연결리스트로 만들기
    p.right = head
    head.left = p
    delete_nodes = []

    # 시작 위치로 이동시키기
    now = head
    while now.idx < k:
        now = now.right

    for order in cmd:

        command = order[0]

        if command == 'U':
            move_count = int(order.split(' ')[1])
            moved = 0
            while moved < move_count:
                now = now.left
                moved += 1
        
        elif command == 'D':
            move_count = int(order.split(' ')[1])
            moved = 0
            while moved < move_count:
                now = now.right
                moved += 1
        
        elif command == 'C':
            now, head = deleteNode(now, head, delete_nodes)
        
        elif command == 'Z':
            head = insertNodeMiddle(delete_nodes.pop(), head)
        
    # 현재 남아있는 데이터를 기준으로 
    # 원래 데이터와의 차이점 구하기
    p = head
    data_idxs = []

    # 현재 남아 있는 데이터 담아주기
    while p:
        data_idxs.append(p.idx)
        p = p.right

        if p == head:
            break
    
    temp = ['X' for _ in range(n)]
    for i in data_idxs:
        temp[i] = 'O'
    
    return ''.join(temp)



print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))


def firstSolu(n, k, cmd):

    '''
        다른 사람 풀이
        https://kjhoon0330.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%91%9C-%ED%8E%B8%EC%A7%91-Python

        이중연결리스트를 dict 자료형으로 나타냄
        그래서 그런지 훨씬 빠른듯?? ㅋㅋ
        그리고 문제를 자세히 읽어보면 표 범위를 벗어나는 이동은 주어지지 않는다고 해서
        굳이 원형 리스트로 만들 필요가 없는듯... ㅋㅋ

        처음에 풀이보고 단순 이중연결리스트라서 뭐지 싶었음.. ㅋㅋㅋㅋㅋㅋㅋ
        앞으로 문제 꼼꼼이 읽어보자..
    '''

    cur = k
    table = { i:[i-1, i+1] for i in range(n)}

    answer = ['O'] * n
    table[0] = [None, 1]
    table[n-1] = [n-2, None]
    stack = []

    for c in cmd:
        if c == "C":
            answer[cur] = 'X'
            prev, next = table[cur]
            stack.append([prev, cur, next])

            if next == None:
                cur = table[cur][0]
            else:
                cur = table[cur][1]
            
            if prev == None:
                table[next][0] = None
            elif next == None:
                table[prev][1] = None
            else:
                table[prev][1] = next
                table[next][0] = prev
            
        
        elif c == 'Z':
            prev, now, next = stack.pop()
            answer[now] = 'O'
            if prev == None:
                table[next][0] = now
            elif next == None:
                table[prev][1] = now
            else:
                table[next][0] = now
                table[prev][1] = now
            
        
        else:

            c1, c2 = c.split(' ')
            c2 = int(c2)

            if c1 == 'D':
                for _ in range(c2):
                    cur = table[cur][1]
            else:
                for _ in range(c2):
                    cur = table[cur][0]
    
    return ''.join(answer)
