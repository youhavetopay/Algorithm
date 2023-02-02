# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:

    root = None

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        '''
            나의 풀이
            정렬된 배열로 밸런스 이진 트리 만드는 문제

            이진탐색??을 응용해서?? 품 ㅋㅋ
            배열을 절반으로 나눈 다음
            중앙값이 현재 노드의 값으로 하고
            중앙값보다 작은 왼쪽 배열은 왼쪽 자식
            중앙값보다 큰 오른쪽 배열은 오른쪽 자식

            이렇게 해서 재귀로 품

            시간, 공간복잡도가 상당하지만...
            그래도 풀긴 품 ㅋㅋ
        '''

        def makeTree(new_nums, pre_node, left_yn):
            
            if len(new_nums) == 0:
                return

            
            mid = len(new_nums) // 2
            print(new_nums, mid)

            new_node = TreeNode(new_nums[mid])

            if pre_node == None:
                self.root = new_node
            
            else:

                if left_yn:
                    pre_node.left = new_node
                else:
                    pre_node.right = new_node
            
            left_nums = new_nums[:mid]
            if len(left_nums) != len(new_nums):
                makeTree(left_nums, new_node, True)

            right_nums = new_nums[mid+1:]
            if len(right_nums) != len(new_nums):
                makeTree(right_nums, new_node, False)

            
        makeTree(nums, self.root, True)


        return self.root
    
    def firstSoul(self, nums: List[int]) -> Optional[TreeNode]:

        '''
            책 풀이
            나랑 비슷하게 이진탐색원리를 기본으로 구현함
            대신 코드는 훨씬 깔끔함 ㅋㅋㅋ

            처음에 이렇게 문제를 푸는 메서드를 사용하는 방법을 생각했는데
            root를 어떻게 반환하고 자식을 어떻게 할당해야하는지 모르겠어서

            그냥 따로 중접함수도 만들고 맴버변수도 만들었는데
            다음부터는 좀 더 깊게 생각해보는 것이 좋을 듯 함!!
        '''

        if not nums:
            return None
        
        mid = len(nums) // 2

        node = TreeNode(nums[mid])
        node.left = self.firstSoul(nums[:mid])
        node.right = self.firstSoul(nums[mid+1:])

        return node


obj = Solution()
print(obj.sortedArrayToBST([1,2,3,4,5,6]))