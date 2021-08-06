class Node():

    def __init__(self, value):
        self.index = None
        self.value = value
        
        self.color = 'red'
        self.left = None
        self.right = None

class RedBlackTree():

    def __init__(self, node):
        self.rootNode = node
        self.nodeIndex = 1

        # 루트노드는 무조건 검은색
        if self.rootNode.color == 'red':
            self.rootNode.color = 'black'
        
        node.index = 1
    
    # 왼쪽 회전
    def leftRotaion():
        pass
    
    # 오른쪽 회전
    def rightRotaion():
        pass

    # 단순 색 변경
    def recoloring():
        pass
    
    # 구조변경
    def restructing():
        return
    
    # 노드 추가
    def addNode(self, node):
        gpNode = self.rootNode
        gpNodeLoc = ''
        pNode = self.rootNode
        pNodeLoc = ''
        point = self.rootNode

        count = 0

        while point != None:
            if count >= 2:
                gpNode = pNode
      
            if count >= 1:
                pNode = point
                

            if point.value < node.value:
                point = point.right
               
            else:
                point = point.left
            
            count += 1

        if pNode.value < node.value:
            if pNode.color == 'red':

                if gpNode.value < node.value:
                    if gpNode.right == None:
                        pNode.right = node
                        return

                    else:
                        if gpNode.right.color == 'red':
                            self.recoloring()
                        else:
                            self.restructing()
                else:
                    if gpNode.left == None:
                        pNode.left = node
                        return
                        
                    else:
                        if gpNode.left.color == 'red':
                            self.recoloring()
                        else:
                            self.restructing()
                

            if pNode == self.rootNode:
                pNode.right = node
        else:
            if pNode == self.rootNode:
                pNode.left = node

        pass
    
    # 노드 삭제
    def delNode(self, value):
        pass
    