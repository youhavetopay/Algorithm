class MyHashMap:

    '''
        나의 풀이
        해시 구조를 직접 구현하는 문제

        그냥 배열 인덱스를 key로 하는 방식으로 구현함
        만약 key의 크기가 배열의 크기를 넘어선다면 
        현재 크기의 배로 늘리는 방법으로 구현함

        시간복잡도는 디게 빠른데
        공간복잡도는 좀 높은듯.. 최대 10^6 + 1 ?
    '''

    def __init__(self):
        self.hash = [None]
        return

    def put(self, key: int, value: int) -> None:

        if len(self.hash) <= key:
            while len(self.hash) <= key:
                self.hash += ([None] * len(self.hash))
        
        self.hash[key] = value

        return

    def get(self, key: int) -> int:

        if len(self.hash) <= key or self.hash[key] == None:
            return -1

        return self.hash[key]

    def remove(self, key: int) -> None:

        if len(self.hash) <= key:
            return

        self.hash[key] = None

        return




from collections import defaultdict

class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class FirstSoul:

    '''
        책 풀이
        defaultdict 이랑 연결리스트로 구현함

        해시 테이블 역할을 하는 defaultdict을 사용하고
        해당 테이블에 값으로 연결리스트를 계속 이어가는 방법으로 구현함

        한가지 의문점은 문제에서는 내부 라이브러리를 사용하지 말라고 했는데
        파이썬은 dict형식 자체가 해시로 구현되어 있어서
        만약 dict을 쓴다면 그냥 dict으로 사용하는게 훨씬 간단한데 책은 왜 이렇게 한거지..??

        아마 개별 체이닝 방식으로 구현하려고 일부러 이렇게 한듯??
        
        해시키가 중복 될 경우 해결방법
        - 개별 체이닝 : 연결리스트로 계속 이어가는거
        - 오픈 어드레싱 : 선형탐색으로 다음 비어있는 해시키를 찾아서 넣는 방법

    '''

    def __init__(self):
        # 해시 사이즈는 1000으로 하고 
        # defaultdict으로 초기값을 넣어줌
        self.size = 1000
        self.hash = defaultdict(ListNode)
        return

    def put(self, key: int, value: int) -> None:

        idx = key % self.size

        if self.hash[idx].value == None:
            self.hash[idx] = ListNode(key, value)
            return

        pointer = self.hash[idx]
        while pointer:

            if pointer.key == key:
                pointer.value = value
                return
            
            if pointer.next == None:
                break

            pointer = pointer.next
        
        new_node = ListNode(key, value)
        pointer.next = new_node

        return

    def get(self, key: int) -> int:

        idx = key % self.size

        if self.hash[idx].value == None:
            return -1
        
        pointer = self.hash[idx]
        while pointer:
            if pointer.key == key:
                return pointer.value
            pointer = pointer.next

        return -1

    def remove(self, key: int) -> None:

        idx = key % self.size

        if self.hash[idx].value == None:
            return
        
        pointer = self.hash[idx]
        if pointer.key == key:
            self.hash[idx] = ListNode() if pointer.next == None else pointer.next
        
        prev = pointer
        while pointer:
            if pointer.key == key:
                prev.next = pointer.next
                return
            
            prev, pointer = pointer, pointer.next
                
        return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(1,2)
# param_2 = obj.get(1)
# print(param_2)
# obj.remove(1)