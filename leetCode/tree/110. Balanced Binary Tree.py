# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        '''
            나의 풀이
            이진트리가 밸런스 트리인지 아닌지 검사하는 문제

            밸런스 트리
            모든 노드의 자식 노드의 최대 깊이 차이가 1 이하인 트리

            조금 이상하게 풀었긴 한데
            일단 풀긴 품.ㅋㅋㅋㅋ
            함수가 입력값에 따라 출력값 형태가 달라짐 ㅋㅋㅋ

            dfs 로 계속 내려가면서 깊이를 계산하다가
            왼쪽이랑 오른쪽의 깊이 차이가 2 이상 나면 그때 부터 무조건 Flase 리턴
            괜찮다면 최대 깊이를 반환

        '''

        def findMaxDepth(node, depth):
            if not node:
                return depth - 1
            
            left = findMaxDepth(node.left, depth + 1)
            right = findMaxDepth(node.right, depth + 1)

            if left is False or right is False:
                return False

            if abs(left - right) >= 2:
                return False

            return max(left, right)


        return findMaxDepth(root, 1) is not False
    
    def isBalanced2(self, root: Optional[TreeNode]) -> bool:

        '''
            두번째 나의 풀이

            첫번째 풀이의 함수를 조금 개선함
            입력값에 따라 출력값 형태가 변하지 않도록
            출력값을 최대 값이랑 밸런스트리 여부 값을 반환하도록 함

            근데 시간복잡도가 20ms정도 증가함
            언패킹하는데 시간이 좀 더 걸리는듯??

            영 마음에 들지 않는 코드임... ㅋㅋ
        '''

        def findMaxDepth(node, depth):
            if not node:
                return depth - 1, True
            
            left, flag_left = findMaxDepth(node.left, depth + 1)
            right, flag_right = findMaxDepth(node.right, depth + 1)

            if not flag_left or not flag_right:
                return max(left, right), False

            if abs(left - right) >= 2:
                return max(left, right), False

            return max(left, right), True


        return findMaxDepth(root, 1)[1]
    
    def firstSoul(self, root: Optional[TreeNode]) -> bool:

        '''
            책 풀이

            나의 첫번째 풀이랑 거의 똑같음..

            아.. -1을 던져 주면 되네 ㅋㅋㅋㅋㅋ
        '''

        def check(node):
            if not node:
                return 0
            
            left = check(node.left)
            right = check(node.right)

            if left == -1 or right == -1 or \
                abs(left - right) > 1:
                return -1
            
            return max(left, right) + 1

        return check(root) != -1