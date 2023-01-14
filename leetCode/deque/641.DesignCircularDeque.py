class ListNode:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None


class MyCircularDeque:

    '''
        나의 풀이
        이중 연결리스트로 Deque 구현함..
        처음엔 배열로 해볼려다가 너무 힘들어서 그냥 포기함 ㅜㅜ
        그래서 책을 봤는데 연결리스트로 구현했길래 
        그냥 똑같이 연결리스트로 구현함

        훨씬 편하네 ㅋㅋㅋㅋㅋㅋㅋㅋㅋ

        책에서는 노드를 연결하는 함수, 삭제하는 함수 따로 만들어서 했음
        그리고 처음에 deque 생성할 때 head랑 tail을 초기화를 해줌

        근데 문제의도는 연결리스트로 구현하는게 아닌 배열로 구현해야 했었음
        책에서도 이렇게 되면 원형 데크의 의미가 없어지기에 
        그냥 연결리스트로 구현이 가능하다 정도의 의미이지 
        이게 정답은 아니라고 함        

    '''

    def __init__(self, k: int):

        self.data_count = 0
        self.max_data_count = k

        self.head = None
        self.tail = None

        return

    def insertFront(self, value: int) -> bool:

        if self.isFull():
            return False

        new_node = ListNode(value)
        self.data_count += 1

        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
            return True
        
        self.head.left = new_node
        new_node.right = self.head
        self.head = new_node


        return True

    def insertLast(self, value: int) -> bool:

        if self.isFull():
            return False
        
        new_node = ListNode(value)
        self.data_count += 1

        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
            return True

        self.tail.right = new_node
        new_node.left = self.tail
        self.tail = new_node

        return True

    def deleteFront(self) -> bool:

        if self.isEmpty():
            return False
        
        self.data_count -= 1
        self.head = self.head.right
        if self.head:
            self.head.left = None
        else:
            self.tail = None
        
        return True

    def deleteLast(self) -> bool:

        if self.isEmpty():
            return False

        self.data_count -= 1
        self.tail = self.tail.left
        if self.tail:
            self.tail.right = None
        else:
            self.head = None
        
        return True

    def getFront(self) -> int:
        if self.head:
            return self.head.data
        return -1

    def getRear(self) -> int:
        if self.tail:
            return self.tail.data
        return -1

    def isEmpty(self) -> bool:
        return self.data_count == 0

    def isFull(self) -> bool:
        return self.data_count == self.max_data_count


# Your MyCircularDeque object will be instantiated and called as such:
obj = MyCircularDeque(8)
param = obj.insertFront(5)

param = obj.deleteLast()

param = obj.getRear()

# param = obj.deleteFront()
# print(obj.deque, param, obj.front, obj.back)
# param = obj.insertLast(3)
# print(obj.deque, param, obj.front, obj.back)
# param = obj.getRear()
# print(obj.deque, param, obj.front, obj.back)
# param = obj.insertLast(7)
# print(obj.deque, param, obj.front, obj.back)
# param = obj.insertFront(7)
# print(obj.deque, param, obj.front, obj.back)
# param = obj.deleteLast()
# print(obj.deque, param, obj.front, obj.back)
# param = obj.insertLast(4)
# print(obj.deque, param, obj.front, obj.back)
# param = obj.isEmpty()
# print(obj.deque, param, obj.front, obj.back)