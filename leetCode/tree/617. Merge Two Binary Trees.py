# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        '''
            나의 풀이
            두개의 이진트리의 값들을 합치는 문제

            재귀 돌면서
            root1, root2 값 있으면 root1을 기준으로 더해주고
            자식 노드가 있는지 없는지 조사
            있으면 안으로 들어가고
            
            기준점이 root1이기 때문에 root2의 자식이 없으면 무시
            root1의 자식이 없으면 root1 자식을 root2의 자식으로 변경

            단순히 같은 위치에 있는 노드의 값을 합치는 문제라서
            엄청 어렵진 않았음
        '''

        if root1 and root2:
            root1.val += root2.val
        
            if root1.left and root2.left:
                self.mergeTrees(root1.left, root2.left)
            elif root2.left:
                root1.left = root2.left
            
            if root1.right and root2.right:
                self.mergeTrees(root1.right, root2.right)
            elif root2.right:
                root1.right = root2.right

        elif root2:
            return root2

        return root1
    
    def firstSoul(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        '''
            책 풀이
            똑같은 재귀 탐색으로 품

            대신 어떤 노드를 기준으로 잡고 하는 것이 아닌
            새로운 노드를 만들어서 반환

            훨씬 간단하고 보기 좋은듯 ㅋㅋ

            그리고 반환할 때 or 할 수 있는듯!!
        '''

        if root1 and root2:
            node = TreeNode(root1.val + root2.val)
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)

            return node

        return root1 or root2
