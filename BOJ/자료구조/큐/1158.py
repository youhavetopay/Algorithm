# 요세푸스 문제
import sys


class Node():
    def __init__(self, value):
        self.data = value
        self.next = None
        

class LinkedList():
    def __init__(self):
        self.head = None
        self.cursor = self.head
        self.deleteList = []
    
    def newNode(self, data):
        if self.head == None:
            self.head = data
            data.next = self.head
        
        else:
            cursor = self.head

            while cursor.next != self.head:
                cursor = cursor.next

            cursor.next = data
            data.next = self.head
    
    def deleteNode(self, loc):
        cur_loc = 1
        if self.cursor == None:
            self.cursor = self.head
            cur_loc += 1
        
        else:
            preNode = self.head

            while preNode.next != self.cursor:
                preNode = preNode.next

            while cur_loc < loc:
                preNode = self.cursor
                self.cursor = self.cursor.next
                cur_loc += 1

            if self.cursor.next == self.cursor:
                self.deleteList.append(self.cursor.data)
                
            elif self.cursor.next == self.head:
                preNode.next = self.head
                self.deleteList.append(self.cursor.data)
                self.cursor = self.head
                
            else:
                preNode.next = self.cursor.next
                self.deleteList.append(self.cursor.data)
                self.cursor = self.cursor.next
                
        


input = sys.stdin.readline

totalCount, step = map(int, input().strip().split())

list1 = LinkedList()

for i in range(1, totalCount+1):
    list1.newNode(Node(i))

while len(list1.deleteList) < totalCount:
    list1.deleteNode(step)
answers = '<'
for i in list1.deleteList:
    answers = answers + str(i) +', '
answers = answers[:-2] + '>'
print(answers)


# 이게 답임 ㅋㅋ
# n, m = map(int, input().split())
# l = list(range(1, n + 1))
# r = []
# index = 0

# while l:
#     index = (index + m - 1) % len(l) <-- 후...
#     r.append(str(l.pop(index)))

# print('<', ', '.join(r), '>', sep='')
    