# Definition for a binary tree node.
from typing import Optional

import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        '''
            나의 풀이
            이진트리 자식 노드 끼리 바꾸는 문제

            쉬웠음...
            재귀로 계속 내려가면서
            left, right 바꿔주면 됨
        '''

        if root is None:
            return root
        
        def changeLeftRight(node):

            node.left, node.right = node.right, node.left

            if node.left:
                changeLeftRight(node.left)
            
            if node.right:
                changeLeftRight(node.right)

            return

        changeLeftRight(root)

        return root
    
    def firstSoul(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        '''
            첫번째 책 풀이
            나랑 똑같음
            대신 나는 중첩 함수를 사용했는데
            풀이는 풀이 함수를 그대로 사용함

            파이썬 다운 방식 이라고 함 ㅋㅋ
        '''

        if root:
            root.left, root.right = \
                self.invertTree(root.right), self.invertTree(root.left)
            
            return root
            
        return None
    
    def secondSoul(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        '''
            두번째 책 풀이

            반복구조의 BFS를 활용하여 품
            첫번째 풀이는(재귀) Bottom-Up 방식이고 
            두번째 풀이는 Top-Down 방식이라고 함
        '''

        queue = collections.deque([root])

        while queue:

            node = queue.popleft()

            if node:
                node.left, node.right = node.right, node.left

                queue.append(node.left)
                queue.append(node.right)

        return root
    
    def thirdSoul(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        '''
            세번째 책 풀이
            반복 구조의 DFS 구조로 품
            사실상 두번째 풀이에서 popleft를 한걸 pop으로 바꾼거 밖에 없음


        '''

        stack = collections.deque([root])

        while stack:

            node = stack.pop()

            if node:
                node.left, node.right = node.right, node.left

                stack.append(node.left)
                stack.append(node.right)

        return root
    
    def fourthSoul(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        '''
            네번째 책 풀이
            3번째 풀이가 그냥 전위로 한건데 후위로 바꾼 풀이
            똑같다고 함
        '''

        stack = collections.deque([root])

        while stack:

            node = stack.pop()

            if node:

                stack.append(node.left)
                stack.append(node.right)

                node.left, node.right = node.right, node.left

        return root