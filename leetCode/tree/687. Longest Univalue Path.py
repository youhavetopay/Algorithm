# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        '''
            나의 풀이
            트리에서 노드의 값이 같은 값으로 연속된 노드들 중에서 
            노드끼리 가장 멀리 떨어진 거리를 반환하는 문제

            못품...
            겁나 어렵네 ㅠㅠㅠㅠㅠㅠㅠㅠㅠ

            접근조차 못함..
            543. Diameter of Binary Tree 이 문제에서 좀 더 심화된 문제인데
            저 문제도 제대로 푼게 아니라서
            너무 어려움 ㅠㅠㅠㅠㅠ
        '''

        if root is None:
            return 0

        temp = [0]

        def dfs(node, count):

            if not node.left and not node.right:
                return count

            l1 = 0
            if node.left:
                if node.val == node.left.val:
                    l1 = dfs(node.left, count+1)
                else:
                    return count
            r1 = 0
            if node.right:
                if node.val == node.right.val:
                    r1 = dfs(node.right, count+1)
                else:
                    return count
                

            return max(l1, r1)

        print(dfs(root, 0))    

        return
    
    result : int = 0
    def firstSoul(self, root: Optional[TreeNode]) -> int:

        '''
            책 풀이
            543 문제와 비슷하게 풀어냄
            dfs로 리프노드 까지 내려 간 다음
            아래서부터 계산하면서 올라옴
        '''

        def dfs(node):

            if node is None:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            if node.left and node.left.val == node.val:
                left += 1
            else:
                # 연속되지 않으면 0으로 초기화
                left = 0

            if node.right and node.right.val == node.val:
                right += 1
            else:
                # 연속되지 않으면 0으로 초기화
                right = 0
            
            # 왼쪽값과 오른쪽 값의 합 계산
            self.result = max(self.result, left + right)

            # 왼쪽이랑 오른쪽 중 하나만 올려야 함 -> 나의 부모에서는 내 자식 두개를 동시에 못써서
            return max(left, right)
        
        dfs(root)

        return self.result

obj = Solution()


n1 = TreeNode(val=1)
n2 = TreeNode(val=1)
n3 = TreeNode(val=1)
n4 = TreeNode(val=1)
n5 = TreeNode(val=1)

n1.left = n2
n1.right = n3

n2.left = n4
n2.right = n5

print(obj.longestUnivaluePath(n1))