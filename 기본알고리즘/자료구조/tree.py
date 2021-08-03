class Node(): # <-- 노드

   def __init__(self, value) -> None:
       self.index = None
       self.value = value
       self.left = None
       self.right = None


class BinTree(): # <-- 이진 트리

    def __init__(self, rootNode):
        self.rootNode = rootNode
        self.nodeCount = 1
        rootNode.index = 1

    # 전위 순회  C - L - R
    def preOrderStart(self):

        def preOrder(node):
            print([node.index, node.value], end=" ")

            if node.left != None:
                preOrder(node.left)
            if node.right != None:
                preOrder(node.right)

        preOrder(self.rootNode)


    # 중위 순회  L - C - R
    def inOrderStart(self):

        def inOrder(node):
            if node.left != None:
                inOrder(node.left)

            print([node.index, node.value], end=" ")

            if node.right != None:
                inOrder(node.right)

        inOrder(self.rootNode)
    

    # 후위 순회 L - R - C
    def postOrderStart(self):

        def postOrder(node):
            if node.left != None:
                postOrder(node.left)
            
            if node.right != None:
                postOrder(node.right)
            
            print([node.index, node.value], end=" ")
        
        postOrder(self.rootNode)


    # 노드 추가
    def addNode(self, node):
        point = self.rootNode
        preNode = self.rootNode
        
        while point != None:
            preNode = point

            if point.value <= node.value:
                point = point.right
            else:
                point = point.left

        if preNode.value <= node.value:
            preNode.right = node
        else:
            preNode.left = node

        self.nodeCount += 1
        node.index = self.nodeCount
    
    # 노드 삭제 노답 ㅋㅋ
    def deleteNode(self, value:int):
        point = self.rootNode
        preNode = self.rootNode
        print(point.value, value)
        
        while point.value != value:  # value값을 가지는 노드 찾아갈때까지
            preNode = point
            if point.left == None and point.right == None:  # 값을 찾지 못했는데 자식노드가 없을때
                print('1 해당 값 없음')
                return

            if point.right != None and point.value <= value:
                point = point.right
            elif point.left != None and point.value > value:
                point = point.left
            elif (point.left == None and point.value > value) or (point.right == None and point.value <= value):
                # 값을 찾지 못했으나 해당하는 방향에 자식노드가 없을 때
                print('2 해당 값 없음', point.value, point.left, point.right)
                return


        if preNode.left == point: # 삭제할려는 노드가 왼쪽일 때
            # 삭제하는 노드의 자식노드가 없을 때
            if point.left == None and point.right == None:
                preNode.left = None
                del point
                return
            # 삭제하는 노드의 왼쪽 자식노드는 없고 오른쪽은 있을때
            elif point.left == None:
                preNode.left = point.right
                del point
                return
            # 삭제하는 노드의 왼쪽 자식노드는 있고 오른쪽은 없을때
            elif point.rigth == None:
                preNode.left = point.left
                del point
                return
            # 삭제하는 노드의 자식이 양쪽 다 있을 때
            else:
                # 연결하는 기준은 맘대로 해도 상관 없음  
                preFillNode = point
                fillNode = point.left # <-- (나는 왼쪽껄로 함) : 왼쪽 노드의 자식노드중 가장 큰 값을 가지는 노드로 대체

                while fillNode.right != None:
                    preFillNode = fillNode
                    fillNode = fillNode.right
                
                preNode.left = fillNode
                fillNode.right = point.right
                fillNode.left = point.left
                preFillNode.right = None

                del point
                return
                

        else: # 삭제할려는 노드가 오른쪽일 때
            # 삭제하는 노드의 자식노드가 없을 때
            if point.left == None and point.right == None:
                preNode.right = None
                del point
                return
            # 삭제하는 노드의 왼쪽 자식노드는 없고 오른쪽은 있을때
            elif point.left == None:
                preNode.right = point.right
                del point
                return
            # 삭제하는 노드의 왼쪽 자식노드는 있고 오른쪽은 없을때
            elif point.right == None:
                preNode.right = point.left
                del point
                return
            # 삭제하는 노드의 자식이 양쪽 다 있을 때
            else:
                # 연결하는 기준은 맘대로 해도 상관 없음 
                preFillNode = point
                fillNode = point.left # <-- (나는 왼쪽껄로 함)

                while fillNode.right != None:
                    preFillNode = fillNode
                    fillNode = fillNode.right
                
                preNode.right = fillNode
                fillNode.right = point.right
                fillNode.left = point.left
                preFillNode.right = None

                del point
                return


tree = BinTree(Node(50))

tree.addNode(Node(25))
tree.addNode(Node(27))
tree.addNode(Node(51))
tree.addNode(Node(57))



# tree.inOrderStart()
# print()

# tree.postOrderStart()
tree.addNode(Node(78))
tree.addNode(Node(67))
tree.addNode(Node(65))
tree.addNode(Node(88))

tree.addNode(Node(53))
tree.addNode(Node(52))
tree.addNode(Node(56))

print('전위')
tree.preOrderStart()
print()
print()
print('57 값을 가지는 노드 삭제')
tree.deleteNode(57)
print()
print('전위')
tree.preOrderStart()
print()