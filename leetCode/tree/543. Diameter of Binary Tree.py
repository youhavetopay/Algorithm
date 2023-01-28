# Definition for a binary tree node.
from typing import Optional
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        '''
            나의 풀이
            이진트리에서 가장 서로 멀리 떨어진 노드 간의 거리를 반환하는 문제

            이거 easy 맞음...??????????
            겁나 어려웠음 ㅋㅋㅋㅋㅋㅋ

            결국 트리 자체에서 해결 못하고
            트리를 그래프로 만들고
            그래프에서 BFS로 최대 깊이를 계산해서 품
        '''

        if root is None:
            return 0

        graph = self.makeGraph(root)

        start_num = list(graph.keys())[-1]

        diameter = -1

        visit_check_board = collections.defaultdict(int)

        queue = collections.deque([start_num])
        visit_check_board[start_num] = 1

        while queue:
            diameter += 1

            for _ in range(len(queue)):

                node = queue.popleft()

                for next in graph[node]:
                    if not visit_check_board[next]:
                        visit_check_board[next] = 1
                        queue.append(next)
    
        return diameter
    
    def makeGraph(self, root):

        queue = collections.deque([[root, 1]])

        graph = collections.defaultdict(list)
        while queue:
            node, node_num = queue.popleft()

            if node_num not in graph:
                graph[node_num] = []

            if node.left:
                graph[node_num].append(node_num*2)
                graph[node_num*2].append(node_num)

                queue.append([node.left, node_num*2])
            
            if node.right:
                graph[node_num].append(node_num*2 + 1)
                graph[node_num*2+1].append(node_num)

                queue.append([node.right, node_num*2+1])

        return graph
    

    longset: int = 0
    
    def firstSoul(self, root: Optional[TreeNode]) -> int:
        
        '''
            책 풀이

            dfs로 left, right의 깊이를 각각 구한 다음
            dfs에서는 left, right 의 깊이 중 더 깊은거에 + 1
            이걸 상태값이라고 함

            길이는 left 깊이 + right 깊이 + 2 로 구함

            대신 중첩함수이기에 longset을 클래스변수로 선언해서
            계속 갱신하는 방식으로 구현

            뜨하...
            나도 처음에 left, right의 최대값을 반환하는 방식으로 해볼려고 했었는데
            길이를 계산하는걸 어떻게 해야할지 몰라서 포기했었음 ㅠㅠㅠ

        '''

        def dfs(node):
            if not node:
                return -1

            # 깊이 구하기
            left = dfs(node.left)
            right = dfs(node.right)

            # 최대 길이 갱신
            self.longset = max(self.longset, left + right + 2)

            # 깊이 반환(상태값??)
            return max(left, right) + 1

        dfs(root)

        return self.longset