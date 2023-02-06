# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:

    now_idx = 0

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        '''
            나의 풀이
            전위, 중위 순회 값이 배열로 주어지면 
            이걸로 이진트리 만드는 문제

            좀 어려웠음 ㅠㅠ

            분할정복 방식으로 풀었는데
            전위 순회에서 자신의 왼쪽에 있는건 무조건 자기 보다 같거나 높은 위치를 가지고 있음
            그래서 전위 순회 값을 차례대로 탐색을 하는데
            중위 순회의 값에서 왼쪽에 있는건 자신의 왼쪽자식이고
            오른쪽에 있는 건 자신의 오른쪽 자식임

            이러한 원리를 바탕으로 품

            코드가 너무 이상하지만 일단 풀긴 풀었고
            정답을 빨리 보는게 좋을듯 해서 그냥 개선은 안함
        '''

        def makeTree(left, right):
            
            print(left, right, preorder[self.now_idx])

            # 노드 생성
            node = TreeNode(preorder[self.now_idx])

            # 다음 전위순회 값으로 
            self.now_idx += 1

            # 길이 넘었으면 현재 노드 반환
            if self.now_idx >= len(preorder):
                return node
            next_val = preorder[self.now_idx]

            # 다음 노드 값이 현재 노드의 왼쪽에 있는 경우
            if next_val in set(left):
                # 왼쪽에서 다음 노드의 값의 위치를 찾음
                next_val_idx = left.index(next_val)
                next_left = left[:next_val_idx] # 왼쪽의 왼쪽 자식 ㅋㅋ
                next_right = left[next_val_idx+1:] # 왼쪽의 오른쪽 자식

                node.left = makeTree(next_left, next_right)
            
            # left를 넣으면서 now_idx 값이 달라질수 있으니 다시 체크
            # 요부분 마음에 안듬 -> 어떻게 개선하지..??
            if self.now_idx >= len(preorder):
                return node
            next_val = preorder[self.now_idx]

            # 다음 노드 값이 현재 노드의 오른쪽에 있는 경우
            if next_val in set(right):
                next_val_idx = right.index(next_val)
                next_left = right[:next_val_idx]
                next_right = right[next_val_idx+1:]

                node.right = makeTree(next_left, next_right)


            return node


        # 전위순회의 첫번째 값은 무조건 root 노드임
        root_idx = inorder.index(preorder[0])

        return makeTree(inorder[:root_idx], inorder[root_idx+1:])
    
    def firstSoul(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        '''
            책 풀이

            으아...pop이 있었네..

            pop(0)으로 preorder를 빼면서
            분할정복을 함

            크....
            보면서 감탄함 ㅋㅋㅋㅋㅋㅋ
        '''

        if inorder:

            index = inorder.index(preorder.pop(0))

            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder, inorder[0:index])
            node.right = self.buildTree(preorder, inorder[index+1:])

            return node


obj = Solution()
print(obj.buildTree([3,1,2,4], [1,2,3,4]))