# 에디터 이중연결리스트

# 21년 여름 카카오 인턴 3번이랑 비슷함

import sys
from typing import Counter

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class LinkedList(object):
    def __init__(self):
        self.head = None
        self.cursor = None
    

    def append(self, data):
        
        if self.cursor == None:
            self.head = data
            self.cursor = data
        else:
            self.cursor.right = data
            data.left =  self.cursor
            data.right = None
            self.cursor = data
    
    def getListData(self):
        cur = self.head
        returnStr = ''
        while cur.right != None:
            returnStr += cur.data
            cur = cur.right
        returnStr += cur.data
        return returnStr

    def moveLeftCursor(self):
        if self.cursor.left != None:
            self.cursor = self.cursor.left
        

    def moveRightCursor(self):
        if self.cursor.right != None:
            self.cursor = self.cursor.right

    def insertData(self, data):
        
        if self.cursor.left == None:
            self.head = data
            data.right = self.cursor
            self.cursor.left = data
        else:
            preNode = self.cursor.left
            preNode.right = data
            data.left = preNode
            data.right = self.cursor
            self.cursor.left = data


    
    def deleteData(self):
        if self.cursor.left != None:
            if self.cursor.left.left == None:
                self.head = self.cursor
                self.cursor.left = None
            else:
                preNode = self.cursor.left.left
                preNode.right = self.cursor
                self.cursor.left = preNode

    

input = sys.stdin.readline

nowStr = input().strip()

linkList = LinkedList()
for i in nowStr:
    linkList.append(Node(i))
linkList.append(Node("9"))
orderCount = int(input().strip())


for i in range(orderCount):
    orderStr = input().split()
    
    if orderStr[0] == 'L':
        linkList.moveLeftCursor()
    
    elif orderStr[0] == 'D':
        linkList.moveRightCursor()
    
    elif orderStr[0] == 'B':
        linkList.deleteData()
    
    elif orderStr[0] == 'P':
        linkList.insertData(Node(str(orderStr[1])))
        
    #print(linkList.getListData(), linkList.cursor.data)
    

print(linkList.getListData()[:-1])