# import collections

# # 재귀 깊이 제한이 걸려서 런타임 에러뜸
# # 이거 해줘야 함 ㅋㅋ
# # 하기 싫으면 반복문으로 해야할듯. ㅋㅋㅋ
# import sys
# sys.setrecursionlimit(10000)

# class Node:

#     def __init__(self, index, x):
#         self.left = None
#         self.right = None
#         self.index = index
#         self.x = x
#         return

# def insertNode(root, node):

#     pointer = root

#     while True:

#         if pointer.x < node.x:
#             if pointer.right:
#                 pointer = pointer.right
#             else:
#                 pointer.right = node
#                 break
        
#         if pointer.x > node.x:
#             if pointer.left:
#                 pointer = pointer.left
#             else:
#                 pointer.left = node
#                 break

#     return

# def preorder(node, indexs):

#     indexs.append(node.index)

#     if node.left:
#         preorder(node.left, indexs)
    
#     if node.right:
#         preorder(node.right, indexs)
    
#     return indexs

# def postorder(node, indexs):

#     if node.left:
#         postorder(node.left, indexs)
    
#     if node.right:
#         postorder(node.right, indexs)

#     indexs.append(node.index)
    
#     return indexs



# def solution(nodeinfo):


#     '''
#         나의 풀이
#         2차원 리스트로 이루어진 좌표값에 따라 이진 트리 전위, 후위 순회 결과를 
#         반환하는 문제

#         나의 접근법
#         y값을 기준으로 dict에 담아두고
#         key(= y) 를 기준으로 내림차순으로 정렬 -> y가 가장 높으면 해당 노드는 루트 노드임

#         그 후 root 노드를 만들고 높이 순대로 차례대로 넣어줌 -> 이진트리 만들기
#         만든 다음 전위, 후위 순회 해줘서 품

#         문제를 잘 읽어보고 이진 트리에 대해 잘 알고 있다면 
#         그렇게 어렵지 않은 문제인듯??
#     '''

#     answer = []

#     # 레벨 별로 node 모아두기
#     level_by_node = collections.defaultdict(list)

#     for idx, [x, y] in enumerate(nodeinfo):
#         level_by_node[y].append([idx+1, x])
    
#     print(level_by_node)

#     # 레벨이 높은 순으로 정렬
#     levels = sorted(level_by_node.keys(), reverse=True)
#     print(levels)
    
#     # root 노드
#     root = None

#     # 이진트리 만들어주기
#     for level in levels:

#         # 루트노드가 없을때 만들어주기
#         if root is None:
#             index, x = level_by_node[level][0]
#             root = Node(index, x)
#             continue
        
#         # 노드 삽입
#         for index, x in sorted(level_by_node[level], key=lambda x:x[1]):
#             insertNode(root, Node(index, x))

#     # 전위, 후위 순회 해주기
#     answer.append(preorder(root, []))
#     answer.append(postorder(root, []))

#     return answer






preorder = list()
postorder = list()

def firstSolu(nodeinfo):
    
    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이

        나랑 비슷하게 높이 순으로 정렬해서 푸심
        근데 트리를 만들면서 순회를 같이해서 훨씬 효율적인듯??
    '''

    import sys
    sys.setrecursionlimit(10**6)

    levels = sorted(list({x[1] for x in nodeinfo}), reverse=True)
    nodes = sorted(list(zip(range(1, len(nodeinfo) + 1), nodeinfo)), key=lambda x:(-x[1][1], x[1][0]))

    print(levels)
    print(nodes)
    order(nodes, levels, 0)
    return [preorder, postorder]

def order(nodes, levels, curlevel):
    n = nodes[:]
    cur = n.pop(0)

    preorder.append(cur[0])
    if n:
        for i in range(len(n)):
            if n[i][1][1] == levels[curlevel + 1]:
                if n[i][1][0] < cur[1][0]:
                    order([x for x in n if x[1][0] < cur[1][0]], levels, curlevel + 1)
                else:
                    order([x for x in n if x[1][0] > cur[1][0]], levels, curlevel + 1)
                    break
    
    postorder.append(cur[0])

print(firstSolu([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))