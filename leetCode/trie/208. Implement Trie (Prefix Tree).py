import collections


class Trie:

    def __init__(self):

        '''
            나의 풀이
            트라이를 구현하는 문제
            트라이는 문자 하나하나를 트리로 저장하는 구조

            파이썬 dict 자료구조를 사용함
            중첩 dict을 사용해서 쉽게..?? 구현함

            시간, 공간 나쁘지 않은듯??
            시간은 96% 이고 공간도 88% 라서 괜찮은듯??>
        '''

        # 초기값 선언
        self.word_dict = {}

        return

    # 문자 추가
    def insert(self, word: str) -> None:

        node = self.word_dict

        # 문자 하나하나 찾아가면서 내려감
        for s in word:

            # 문자에 해당하는 key가 없다면 빈 dict 만들어주기
            if s not in node:
                node[s] = {}
            
            # 자식?? 으로 내려가기
            node = node[s]
        
        # 이 문자가 저장되었다고 판단하기 위해
        # 마지막 문자에 'end' 라는 key를 넣어줌
        node['end'] = True

        return
        
    # 문자 찾기
    # 문자 자체를 넣지 않았다면 단어는 있다고 해서 True를 반환하면 안됨
    def search(self, word: str) -> bool:

        node = self.word_dict
        for s in word:
            if s not in node: # 문자 없으면 False
                return False

            node = node[s]

        # 끝까지 왔을 때 'end' key가 있어야 문자 자체를 넣은 거임
        if 'end' in node:
            return True

        # 'end' key 없으면 문자를 넣은 것이 아님
        return False
        
    # 접두사 찾기
    def startsWith(self, prefix: str) -> bool:

        node = self.word_dict
        for s in prefix:
            if s not in node: # 문자 없으면 False
                return False
            
            node = node[s]

        # 접두사만 찾는거라서 잘 왔으면 True
        return True



class TrieNode:
    def __init__(self) -> None:
        self.word = False
        self.children = collections.defaultdict(TrieNode)

class FirstSoul:
    def __init__(self):

        '''
            책 풀이
            나랑 똑같이 dict 자료형 써서 구현함

            대신 TrieNode라는 클래스를 만들어서
            단순 dict을 사용하는 것이 아닌 객체를 만들어서 했음

            그래서 그런지 코드도 디게 깔끔한듯??
            대신 시간, 공간 복잡도가 나보다 쪼~~금 안좋음 캬캬캬 ㅋㅋ

            푼 방법이 나랑 거의 동일해서 신기함.. ㅋㅋ
            그래도 코드는 엄청 보기 좋은 듯 함
        '''

        self.root = TrieNode()
        return

    def insert(self, word: str) -> None:
        node = self.root
        
        for char in word:
            node = node.children[char]
        
        node.word = True

        return
        
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            
            node = node.children[char]

        return node.word
        
    def startsWith(self, prefix: str) -> bool:

        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            
            node = node.children[char]

        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('word')
obj.insert('worh')
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)