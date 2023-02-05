# Definition for a binary tree node.
from typing import Optional
import sys

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        '''
            나의 풀이
            이진트리에서 두 노드의 값 차이가 최소가 되는 값 반환하는 문제

            중위탐색을 하면 이진트리이기에 값들이 정렬됨
            탐색한 값을 반복문으로 인접한 값들의 차이를 구함

            시간복잡도 걸릴 줄 알았는데
            안걸려서 쉽게 품..???ㅋㅋㅋ
        '''

        datas = []

        def dfs(node):

            if not node:
                return

            dfs(node.left)
            datas.append(node.val)
            dfs(node.right)

        dfs(root)

        min_answer = float('inf')
        for i in range(1, len(datas)):
            min_answer = min(min_answer, datas[i] - datas[i-1])

        return min_answer
    
    prev = -sys.maxsize
    result = sys.maxsize

    def firstSoul(self, root: Optional[TreeNode]) -> int:

        '''
            첫번째 책 풀이
            나랑 비슷하게 품
            똑같이 중위 순회를 하면서 
            이전에 탐색한 값이랑 현재 노드의 값의 차이를 비교하여 구함

            나랑 차이점이라면 
            바로바로 차이를 계산하는 점..??
            이거 때문에 나랑 공간복잡도 차이가 남
            최소 차이 값만 반환하면 되기에 굳이 모든 값을 저장할 필요가 없기 때문
        '''

        if root.left:
            self.firstSoul(root.left)

        self.result = min(self.result, root.val - self.prev)

        self.prev = root.val

        if root.right:
            self.firstSoul(root.right)
        

        return self.result
    
    def secondSoul(self, root: Optional[TreeNode]) -> int:
        
        '''
            두번째 책 풀이
            첫번째 풀이의 반복문 버전

            생각해보니 나는 한번도 반복문으로 트리의 순회를 구현해본적이 없어서
            코드를 보니까 신기했음..
        '''
        
        prev = -sys.maxsize
        result = sys.maxsize

        stack = []
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()

            result = min(result, node.val - prev)
            prev = node.val

            node = node.right

        return result