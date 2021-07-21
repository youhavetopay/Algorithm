# add Two Numbers

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        oneNum = ''
        twoNum = ''
        
        cur = l1
        
        while cur != None:
            oneNum += str(cur.val)
            cur = cur.next
            
        cur = l2
        while cur != None:
            twoNum += str(cur.val)
            cur = cur.next
        
        # 문자로 이루어진 리스트 뒤집기
        plusNum = ''.join(reversed(list(str(int(''.join(reversed(list(oneNum)))) + int(''.join(reversed(list(twoNum))))))))
        
    
        preNode = None
        head = None
        for i in plusNum:
            node = ListNode(i, None)
            if preNode == None:
                preNode = node
                head = node
            else:
                preNode.next = node
                preNode = node
        
        return head
                