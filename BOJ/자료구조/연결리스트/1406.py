# 에디터 

# 21년 여름 카카오 인턴 3번이랑 비슷함

import sys

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList(object):
    def __init__(self):
        self.head = None
        self.length = 0
    

    def append(self, node):
        self.length += 1
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node
    
    def getListData(self):
        cur = self.head
        returnStr = ''
        while cur.next != None:
            returnStr += cur.data
            cur = cur.next
        returnStr += cur.data
        return returnStr
    

    def insertData(self, loc, data):
        self.length += 1
        cur_loc = 0
        cur = self.head
        preNode = None
        if loc == 0:
            data.next = cur
        else:
            while cur_loc < loc:
                preNode = cur
                cur = cur.next
                cur_loc += 1
            
            preNode.next = data
            data.next = cur
    
    def deleteData(self, loc):
        self.length -= 1
        cur_loc = 0
        cur = self.head
        preNode = None
        nextNode = cur.next

        if loc == 0:
            self.head = nextNode
        else:
            while cur_loc < loc:
                preNode = cur
                cur = cur.next
                nextNode = cur.next
                cur_loc += 1
            preNode.next = nextNode
        


input = sys.stdin.readline

nowStr = input().strip()

strList = []
linkList = LinkedList()
for i in nowStr:
    linkList.append(Node(i))

orderCount = int(input().strip())
loc = linkList.length

for i in range(orderCount):
    orderStr = input().split()
    
    if orderStr[0] == 'L':
        if loc != 0:
            loc -= 1
    
    elif orderStr[0] == 'D':
        if not(loc >= linkList.length):
            loc += 1
    
    elif orderStr[0] == 'B':
        if loc != 0:
            linkList.deleteData(loc)
            loc -= 1
    
    elif orderStr[0] == 'P':
        linkList.insertData(loc, Node(str(orderStr[1])))
        loc = loc + 1

print(linkList.getListData())