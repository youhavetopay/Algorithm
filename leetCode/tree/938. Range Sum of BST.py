# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        '''
            나의 풀이

            이진트리에서 일정 값의 범위의 합을 구하는 문제

            그냥 재귀로 모든 노드를 탐색하면서 
            노드의 값이 일정 범위라면 더해줘서 반환하는 방식으로 품

            그렇게 어렵진 않았음..
        '''
        
        if root is None:
            return 0

        now_val = root.val

        now_sum = 0
        if low <= now_val and now_val <= high:
            now_sum += now_val
        
        now_sum += self.rangeSumBST(root.left, low, high)
        now_sum += self.rangeSumBST(root.right, low, high)

        return now_sum
    
    def firstSoul(self, root: Optional[TreeNode], low: int, high: int) -> int:

        '''
            첫번째 책 풀이

            나랑 동일한 방식으로 품
            대신 코드 길이가 더 짧다는거...??

            범위 체크할 때 저렇게도 할 수 있다는 걸 암 ㅋㅋ
        '''

        if not root:
            return 0

        return (root.val if low <= root.val <= high else 0) + \
            self.rangeSumBST(root.left, low, high) + \
                self.rangeSumBST(root.right, low, high)

    def secondSoul(self, root: Optional[TreeNode], low: int, high: int) -> int:

        '''
            두번째 책 풀이

            첫번째 풀이를 개선한 버전
            모든 노드를 탐색하는 것이 아니라
            이진트리이기 때문에 탐색 범위를 줄이는 방법으로 구현
            보니까 260ms -> 220ms 정도로 줄어듬..

            처음에 나도 이렇게 해야되나 라고 생각을 했었는데
            그냥 완전탐색해도 풀리길래 그냥 냅둠..

            한번 해볼껄 그랬다.. ㅋㅋㅋ
        '''

        def dfs(node):
            if not node:
                return 0
            
            if node.val < low:
                return dfs(node.right)
            elif node.val > high:
                return dfs(node.left)

            return node.val + dfs(node.left) + dfs(node.right)

        return dfs(root)
    
    def thirdSoul(self, root: Optional[TreeNode], low: int, high: int) -> int:

        '''
            세번째 책 풀이

            두번째 풀이를 반복문 구조로 바꾼 버전
            희한하게 시간,공간 복잡도가 조금 줄어듬..

            재귀가 일반 반복문보다 메모리 사용량이 좀더 많나...?????
        '''

        stack, sum = [root], 0

        while stack:

            node = stack.pop()
            if node:
                if node.val > low:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
                
                if low <= node.val <= high:
                    sum += node.val
        
        return sum
    
    def fourthSoul(self, root: Optional[TreeNode], low: int, high: int) -> int:

        '''
            네번째 책 풀이
            DFS 를 BFS로 푼 버전

            원래는 deque를 사용해야 하지만 그냥 귀찮다고 일반 배열로 선언함 ㅋㅋㅋ
            그래도 문제 풀이에는 그렇게 영향을 미치지 않는 듯 함 -> 그냥 풀림 ㅋㅋ

            파이썬에서 pop(0)은 O(n)이기 때문에
            왠만하면 하지 말기 -> deque로 구현하기
        '''

        queue, sum = [root], 0

        while queue:
            node = queue.pop(0)

            if node:
                if node.val > low:
                    queue.append(node.left)
                if node.val < high:
                    queue.append(node.right)
                
                if low <= node.val <= high:
                    sum += node.val
        
        return sum