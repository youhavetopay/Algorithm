class Node():
    def __init__(self):
        self.keys = []
        self.keysLen = 0
        self.points = [None, None]

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


        # 분할하고 싶은 위치까지 이동하기
        while findValue not in point.keys:

            index = -1

            for i, v in enumerate(point.keys):
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
            leftNode.points = point.points[:findValueIndex+1]
            print(point.points[:findValueIndex+1])
            print(point.points[findValueIndex+1:])
            rightNode = Node()
            for i in range(findValueIndex+1, len(point.keys)):
                rightNode.keys.append(point.keys[i])
                rightNode.keysLen += 1
            rightNode.points = point.points[findValueIndex+1:]

            # root노드와 연결
            newRoot.points = [leftNode, rightNode]

            # 새로운 root로 설정
            self.root = newRoot

            # 기존 Node 삭제
            del point

        else:
            pNodeIndex = -1

            for i, v in enumerate(pNode.keys):
                if v <= findValue:
                    pNodeIndex = i

            rightNode = Node()
            

            for v in range(findValueIndex + 1, point.keysLen):
                rightNode.keys.append(point.keys[v])
                rightNode.keysLen += 1
            rightNode.points = [None] * (rightNode.keysLen + 1)

            point.keys = point.keys[0:findValueIndex]
            point.keysLen = len(point.keys)
            point.points = [None] * (point.keysLen + 1)

            pNode.keys.insert(pNodeIndex + 1, findValue)
            pNode.keysLen += 1
            pNode.points[pNodeIndex+1] = point
            pNode.points.insert(pNodeIndex + 2, rightNode)

            if pNode.keysLen >= self.maxchild:
                self.division(pNode)
                print('2단계 넘음')

        pass



myTree = Btree(3, 10)

myTree.addNode(myTree.root, myTree.root, 5)
myTree.addNode(myTree.root, myTree.root,20)
myTree.addNode(myTree.root, myTree.root,21)
myTree.addNode(myTree.root, myTree.root,22)
myTree.addNode(myTree.root, myTree.root,23)
myTree.addNode(myTree.root, myTree.root,24)
myTree.addNode(myTree.root, myTree.root,25)
myTree.addNode(myTree.root, myTree.root,26)
myTree.addNode(myTree.root, myTree.root,27)

print(myTree.root.points[1].points[2].keys)


print(myTree.root.keys)
for i in range(len(myTree.root.points)):
    print(myTree.root.points[i].keys)


myTree.searchData(myTree.root, 24)
