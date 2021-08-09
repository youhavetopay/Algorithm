class Node():
    def __init__(self):
        self.keys = []
        self.keysLen = 0
        self.points = []

        pass

class Btree():

    def __init__(self, maxchild, rootValue):
        self.maxchild = maxchild
        self.root = Node()

        self.root.keys.append(rootValue)
        self.root.points.append(None)
        self.root.points.append(None)
        self.root.keysLen += 1

    def searchData(self, point, value):
        index = -1
        for i, v in enumerate(point.keys):
            if v < value:
                index = i
            elif v == value:
                print(value, '<-- 있음 ')
                return
                
        if point.points[index + 1] == None:
            print(value, '<-- 없음')
        else:
            self.searchData(point.points[index + 1], value)


    def addNode(self, pNode, node, value):

        index = -1

        for i, v in enumerate(node.keys):
            if v <= value:
                index = i

        if node.points[index+1] != None:
            self.addNode(node, node.points[index+1], value)
            return

        node.keys.insert(index + 1, value)
        node.keysLen += 1
        node.points.append(None)

        if node.keysLen >= self.maxchild:
            print('분할해야함', node.keys)
            self.division(node)
        

    def division(self,node):
        findValue = node.keys[len(node.keys)//2]
        findValueIndex = len(node.keys)//2

        point = self.root
        pNode = self.root

        while findValue not in point.keys:

            index = -1

            for i, v in range(point.keys):
                if v < findValue:
                    index = i
        
            pNode = point
            point = point.points[index + 1]
        
        # 분할할려는 노드가 root 노드일 때
        if point == self.root:
            # 새로운 루트 노드 생성
            newRoot = Node()
            newRoot.keys.append(point.keys[findValueIndex])
            newRoot.keysLen += 1
            newRoot.points = [None, None]
            
            leftNode = Node()
            for i in range(findValueIndex):
                leftNode.keys.append(point.keys[i])
                leftNode.keysLen += 1
            leftNode.points = [None] * (leftNode.keysLen+1)

            rightNode = Node()
            for i in range(findValueIndex+1, len(point.keys)):
                rightNode.keys.append(point.keys[i])
                rightNode.keysLen += 1
            rightNode.points = [None] * (rightNode.keysLen+1)

            # root노드와 연결
            newRoot.points = [leftNode, rightNode]

            # 새로운 root로 설정
            self.root = newRoot

            # 기존 Node 삭제
            del point

        else:
            print('adwawddwawd') 

        pass



myTree = Btree(3, 10)

myTree.addNode(myTree.root, myTree.root, 5)
myTree.addNode(myTree.root, myTree.root,20)

print(myTree.root.keys)
print(myTree.root.points[0].keys)
print(myTree.root.points[1].keys)
myTree.searchData(myTree.root, 20)
