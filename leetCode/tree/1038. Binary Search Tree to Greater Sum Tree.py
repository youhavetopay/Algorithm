# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        '''
            나의 풀이
            이진트리에서 오른쪽, 자신, 왼쪽 순으로 현재까지의 노드의 값을 합하는 문제
            오른쪽 노드는 그대로 -> 왼쪽노드는 전체 합 
            이런느낌 ?.?

            right, center, left 순으로 탐색을 진행하면서
            값을 차근 차근 더해주는 방식으로 구현함

            생각보다 어려웠음
            그래도 다행히 더해지는 순서를 빨리 파악한게
            조금 도움이 되었음

            근데 시간, 공간 복잡도가 하위 30퍼.. ㅋㅋ
            여기서 뭘 어떻게 최적화 해..?? ㅋㅋㅋㅋㅋㅋㅋ
        '''

        def dfs(node, pre_sum):

            if not node:
                return pre_sum
            
            # 오른쪽 자식 부터 더해주기
            right_sum = dfs(node.right, pre_sum)
            
            node.val += right_sum 

            # 왼쪽 자식에는 현재까지 더한 값을 넘겨줌
            left_sum = dfs(node.left, node.val)

            # 왼쪽 자식의 값을 반환
            return left_sum
        
        dfs(root, 0)

        return root
    
    val = 0
    def firstSoul(self, root: TreeNode) -> TreeNode:
        
        '''
            책 풀이

            right - center - left 중위 순회를 이용하여 재귀로 품
            역시나 중첩함수를 사용하는 것이 아닌 재귀를 사용함
            클래스 변수에 현재까지의 누적값을 저장하고
            탐색하는 방식으로 구현함

            아 이게 중위 순회임..??? ㅋㅋㅋㅋ
            left - center - right 가 난 지금까지 중위 순회인 줄 알았는데
            그냥 center의 순서가 전위, 중위, 후위를 정하는거였네 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ

            내가 클래스 변수를 사용하는 습관이 없어서
            자꾸 중첩함수로 푸는데
            클래스 변수를 좀 더 적극적으로 사용하는 연습을 해보는 것이 좋을 듯 함

            시간, 공간 훨씬 좋음 상위 30퍼 정도..??
        '''

        if root:
            self.firstSoul(root.right)

            self.val += root.val
            root.val = self.val

            self.firstSoul(root.left)

        return root