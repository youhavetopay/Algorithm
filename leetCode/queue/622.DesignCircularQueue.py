class MyCircularQueue:

    '''
        나의 풀이
        원형 큐 구현하기

        처음에 배열 사이즈대로 만들고
        값은 front에 넣고 뺼때는 back에서 빼면 됨

        front(인덱스) % 배열 사이즈 로 하면 
        front 계속 순회함 그렇게 구현함

        책 풀이도 비슷한 방식이라서 큰 차이점은 없어서 
        책 풀이는 패스!!
        
    '''


    def __init__(self, k: int):
        self.queue = [None] * k
        self.queue_size = k
        self.front = 0
        self.back = 0
        return
        

    def enQueue(self, value: int) -> bool:

        if self.isFull():
            return False

        self.queue[self.front] = value
        self.front = (self.front + 1) % self.queue_size

        return True
        

    def deQueue(self) -> bool:

        if self.isEmpty():
            return False
        
        self.queue[self.back] = None
        self.back = (self.back + 1) % self.queue_size

        return True
        

    def Front(self) -> int:

        if self.isEmpty():
            return -1

        return self.queue[self.back]
        

    def Rear(self) -> int:

        if self.isEmpty():
            return -1

        return self.queue[self.front-1]
        

    def isEmpty(self) -> bool:
        return self.front == self.back and self.queue[self.front] == None
        

    def isFull(self) -> bool:
        return self.front == self.back and self.queue[self.front] != None
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()