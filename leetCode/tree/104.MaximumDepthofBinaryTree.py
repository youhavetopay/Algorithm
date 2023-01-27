# Definition for a binary tree node.
from typing import Optional
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        '''
            나의 풀이
            트리의 최대 깊이를 구하는 문제

            그냥 재귀로 탐색해서 품
            꽤 쉬운 문제였는데 조금조금 실수가 있어서 푸는데 
            약간..? 오래걸림 ㅋㅋㅋ
        '''

        def findMaxDepth(node, depth):
            
            left_depth = 0
            right_depth = 0

            if not node:
                return depth-1

            if node.left:
                left_depth = findMaxDepth(node.left, depth+1)
            
            if node.right:
                right_depth = findMaxDepth(node.right, depth+1)

            return max(depth, left_depth, right_depth)

        return findMaxDepth(root, 1)
    
    def firstSoul(self, root: Optional[TreeNode]) -> int:

        '''
            책 풀이
            BFS로 구현함 -> 반복문으로 queue 사용

            같은 깊이의 노드를 계속 빼면서 자식 노드를 계속 넣어주는 방식으로
            구현함
            시간, 공간복잡도 모두 위에 풀이보다 효율적임 ㄷㄷ

            지금까지 트리 탐색할 때는 계속 재귀로 했었는데
            BFS로 하는 방식도 고려해보면 좋을듯 함
        '''

        if root is None:
            return 0

        queue = collections.deque([root])
        depth = 0

        while queue:

            depth += 1

            for _ in range(len(queue)):
                cur_root = queue.popleft()

                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)
        

        return depth

