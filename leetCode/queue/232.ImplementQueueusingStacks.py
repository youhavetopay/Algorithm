class MyQueue:

    '''
        나의 풀이
        스택 두개로 큐 구현하기
        조금만 생각해보면 풀 수 있는 문제라서 어렵지 않았음..
        역시나 LeetCode에서는 진짜 스택 2개로 풀었는지 검증을 못하기에
        조금은 문제가 그럼.. ㅋ

        메인스택에 값을 담고
        pop 혹은 peek을 할때는 서브스택으로 전부 옮기면
        스택이 뒤집어?? 지기 때문에 서브스택에서 pop해주면 됨
        서브 스택이 비었으면 다시 메인스택에서 옮겨주는 방식으로 구현함
    '''

    def __init__(self):
        self.main_stack = []
        self.sub_stack = []
        return
        

    def push(self, x: int) -> None:
        self.main_stack.append(x)
        return
        

    def pop(self) -> int:

        if self.sub_stack:
            return self.sub_stack.pop()

        if not self.main_stack:
            return

        while self.main_stack:
            self.sub_stack.append(self.main_stack.pop())
        
        return self.sub_stack.pop()
        

    def peek(self) -> int:

        if self.sub_stack:
            return self.sub_stack[-1]

        if not self.main_stack:
            return
        while self.main_stack:
            self.sub_stack.append(self.main_stack.pop())
        
        return self.sub_stack[-1]
        

    def empty(self) -> bool:

        return not self.main_stack and not self.sub_stack
        
class FirstSoul:
    '''
        책 풀이
        나랑 원리는 역시 똑같음ㅎㅎ

        근데 역시나 코드 퀄리티가 좋은듯..?
        중복 코드를 제거함 -> input에서 output으로 이동시키는 과정

        그리고 예외처리를 안하는듯......?
        만약 배열이 텅 비었으면 어쩔려구...ㅋㅋㅋㅋㅋ
    '''

    def __init__(self):
        self.input = []
        self.output = []
        return
        

    def push(self, x: int) -> None:
        self.input.append(x)
        return
        

    def pop(self) -> int:
        self.peek()
        return self.output.pop()
        

    def peek(self) -> int:

        if not self.output:
            while self.input:
                self.output.append(self.input.pop())

        return self.output[-1]
        

    def empty(self) -> bool:

        return self.input == [] and self.output == []

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()