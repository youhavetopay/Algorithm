class Node(): # <- 노드
    def __init__(self):
        self.keys = []
        self.keysLen = 0
        self.points = [None, None]

        pass

class Btree(): # <- B 트리

    def __init__(self, maxchild, rootValue):
        self.maxchild = maxchild
        self.minchild = maxchild // 2
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
            # 데이터 찾을때 까지 재귀호출로 밑으로 내려감
            self.searchData(point.points[index + 1], value)


    def addNode(self, node, value):

        index = -1

        for i, v in enumerate(node.keys):
            if v <= value:
                index = i
        # 삽입할려는 리프노드까지 이동
        if node.points[index+1] != None:
            self.addNode(node.points[index+1], value)
            return

        node.keys.insert(index + 1, value)
        node.keysLen += 1
        node.points.append(None)

        # 삽입한 리프노드가 분할해야 한다면 함수 호출
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
            
            # 원래 있던 노드를 새로 복사 <-- 굳이 이렇게 안해도 되는데 일단 냅둠
            leftNode = Node()
            for i in range(findValueIndex): 
                leftNode.keys.append(point.keys[i])
                leftNode.keysLen += 1
            leftNode.points = point.points[:findValueIndex+1]
            
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
            # 부모노드로 이동시킬 위치 찾기
            for i, v in enumerate(pNode.keys):
                if v <= findValue:
                    pNodeIndex = i
            
            # 오른쪽 노드 복사 <-- 위에 방식보다 이게 좀더 좋은듯? 객체를 필요한 만큼만 만들어서
            rightNode = Node()
            for v in range(findValueIndex + 1, point.keysLen):
                rightNode.keys.append(point.keys[v])
                rightNode.keysLen += 1
            rightNode.points = point.points[:findValueIndex+1]

            # 기존에 있던 노드는 왼쪽 값만 남겨두기
            point.keys = point.keys[0:findValueIndex]
            point.keysLen = len(point.keys)
            point.points = point.points[findValueIndex+1:]

            # 부모노드에 분할한 값 삽입
            pNode.keys.insert(pNodeIndex + 1, findValue)
            pNode.keysLen += 1
            pNode.points[pNodeIndex+1] = point
            pNode.points.insert(pNodeIndex + 2, rightNode)

            # 만약 부모노드가 분할이 필요하다면 재귀 호출
            if pNode.keysLen >= self.maxchild:
                self.division(pNode)
                print('2단계 넘음')


    def deleteNode(self, value):
        
        point = self.root
        pNode = self.root

        index = -1
        while value not in point.keys:

            index = -1

            for i, v in enumerate(point.keys):
                if v < value:
                    index = i
            pNode = point
            point = point.points[index+1]
             
        # case 1: 삭제할려는 노드가 리프노드 일때
        if point.points == [None] * (point.keysLen + 1):

            # case 1-1: 현재 삭제할려는 노드의 최소값이 여유가 있을 때
            if point.keysLen - 1 >= self.minchild:

                valueIndex = point.keys.index(value)

                point.keys = point.keys[0:valueIndex] + point.keys[valueIndex+1:]
                point.keysLen -= 1
                point.points = [None] * (point.keysLen + 1)

                return
            
            else: # 현재 삭제할려는 노드의 여유가 없을 때
                # 형제노드의 여유가 있는 노드 찾기
                friendNodeIndex = -1
                for i, tempNode in enumerate(pNode.points):
                    if i != index+1:
                        if i >= index and i <= index+2:
                            if tempNode.keysLen > self.minchild:
                                friendNodeIndex = i
                
                 # case 1-2 : 왼쪽 혹은 오른쪽 형제노드의 여유값이 있을 때
                if friendNodeIndex != -1:

                    friendNode = pNode.points[friendNodeIndex]

                    friendMaxValue = -100000
                    pNodeValue = -1000000

                    point.keys[0] = pNodeValue
                    pNode.keys[0] = friendMaxValue

                    if friendNodeIndex == index:  # 왼쪽노드
                        friendMaxValue = friendNode.keys[-1] # 왼쪽노드의 경우 가장 큰값으로 부모를 대체
                        pNodeValue = pNode.keys[0]
                        friendNode.keys = friendNode.keys[:-1]
                    
                    else:  # 오른쪽 노드
                        friendMaxValue = friendNode.keys[0] # 오른쪽 노드의 경우 가장 작은 값으로 부모를 대체
                        pNodeValue = pNode.keys[-1]
                        friendNode.keys = friendNode.keys[1:]

                    
                    friendNode.keysLen -= 1
                    friendNode.points = [None] * (friendNode.keysLen + 1)

                    return

                
                # case 1-3 : 형제 노드의 여유가 없고 부모노드가 여유 있을 때
                else:
                    pass



myTree = Btree(3, 10)

myTree.addNode(myTree.root, 5)
myTree.addNode(myTree.root,20)
myTree.addNode(myTree.root,21)
myTree.addNode(myTree.root,22)
myTree.addNode(myTree.root,23)
myTree.addNode(myTree.root,24)
myTree.addNode(myTree.root,25)
myTree.addNode(myTree.root,26)
myTree.addNode(myTree.root,27)

# print(myTree.root.points[1].points[2].keys)


print(myTree.root.keys)
for i in range(len(myTree.root.points)):
    print(myTree.root.points[i].keys)


myTree.searchData(myTree.root, 20)
