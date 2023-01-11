class MyStack:

    '''
        나의 풀이
        근데 이게 큐가 맞나..? ㅋㅋㅋ

        어찌보면 우선순위 큐...? ㅋㅋㅋㅋㅋㅋ
        근데 공간낭비가 있음

        어쨌든 이건 통과는 했지만
        문제가 원하던 구조는 아닌듯함..
    '''


    def __init__(self):
        self.queue = []
        self.data_count = 0

        return
        

    def push(self, x: int) -> None:
        # push할때 인덱스 번호도 같이 넣어줌
        self.queue.append([self.data_count+1, x])
        self.data_count += 1

        return
        

    def pop(self) -> int:

        pop_data = None
        for idx, data in enumerate(self.queue):

            # 배열을 순회하면서 데이터를 찾았다면 
            # 해당 데이터를 None으로 만들어줌 -> 안쓰는 공간이 생김 ㅋ
            if data and data[0] == self.data_count:
                pop_data = data
                self.queue[idx] = None

        if pop_data:
            self.data_count -= 1
            return pop_data[1]

        return None

    def top(self) -> int:

        top_data = None
        for idx, data in enumerate(self.queue):

            # 찾을 때도 마찬가지로 인덱스로 찾음
            if data and data[0] == self.data_count:
                top_data = data

        if top_data:
            return top_data[1]

        return top_data

    def empty(self) -> bool:

        if self.data_count > 0:
            return False

        return True




from collections import deque

class FirstSoul:

    '''
        책 풀이

        처음에 이거 생각을 했었는데
        시간복잡도 때문에 아니라고 생각했었음 ㅋㅋ
        근데 지금보니까 내꺼도 만만치 않은듯. ㅋㅋㅋㅋㅋ

        그리고 파이썬으로 큐를 어떻게 구현해야할지 모르겠어서 
        안한게 없잖아 있음..ㅋㅋㅋ

        deque를 사용해서 구현함
    '''

    def __init__(self):
        self.queue = deque()

        return
        

    def push(self, x: int) -> None:
        self.queue.append(x)

        # 데이터를 넣을 때 이전에 넣어뒀던걸
        # 다시 빼서 뒤로 넣어줌
        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())

        return
        

    def pop(self) -> int:
        
        if len(self.queue):
            return self.queue.popleft()

        return None

    def top(self) -> int:
        if len(self.queue):
            return self.queue[0]
        
        return 

    def empty(self) -> bool:

        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()