from typing import List

import collections

class TrieNode:
    def __init__(self) -> None:

        self.palindrome_word_ids = []
        self.word_id = -1
        self.children = collections.defaultdict(TrieNode)

        return

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    @staticmethod
    def is_palindrome(word: str) -> bool:
        return word[::] == word[::-1]

    def insert(self, index, word) -> None:
        node = self.root

        # 문자열을 거꾸로 넣음
        for i, char in enumerate(reversed(word)):

            # 삽입할 때 미리 팰린드롬 여부를 체크해둠
            if self.is_palindrome(word[0:len(word) - i]):
                node.palindrome_word_ids.append(index)
            
            node = node.children[char]
        
        # 맨 마지막 단어, 즉 첫번째 단어에 인덱스 기록
        node.word_id = index
    
    def search(self, index, word) -> List[List[int]]:
        result = []
        node = self.root

        # 탐색 시작
        while word:

            # node.word_id가 있을 때, 즉 삽입된 단어의 끝에 왔을 때
            if node.word_id >= 0:
                
                # 남은 글자가 팰린드롬이면 팰린드롬 
                # 왜냐하면 글자를 거꾸로 넣었기 때문에
                if self.is_palindrome(word):
                    result.append([index, node.word_id])
            
            # 해당하는 글자 없으면 끝내기
            if not word[0] in node.children:
                return result

            # 글자를 처음부터 하나씩 잘라가면서 탐색을 함
            node = node.children[word[0]]
            word = word[1:]
        
        # 주어진 단어 끝에 왔고 자기 자신이 아닐때
        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])
        
        # 미리 체크된 팰린드롬 인덱스가 있다면 이것도 넣어주기
        for palindrome_word_id in node.palindrome_word_ids:
            result.append([index, palindrome_word_id])
        
        return result


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        '''
            나의 풀이
            문자열이 배열로 주어졌을 때 팰린드롬이 되는 조합을 찾는 문제
            팰린드롬은 뒤집어도 똑같은 단어 ex) abba -> abba

            그냥 완전탐색으로 했는데
            역시나 시간초과뜸
            트라이 파트에 있어서 트라이를 생각해봤는데
            도저히 트라이를 사용해서 풀수 있는 방법을 모르겠음...

            너무 어렵다.. 역시 hard...
        '''

        answers = []

        for i, word in enumerate(words):

            for j, word2 in enumerate(words):
                if i == j:
                    continue

                check_word = word + word2

                start, end = 0, len(check_word)-1

                while start <= end:
                    if check_word[start] != check_word[end]:
                        break

                    start += 1
                    end -= 1
                
                else:
                    answers.append([i, j])


        return answers
    

    def firstSoul(self, words: List[str]) -> List[List[int]]:

        '''
            책 풀이
            역시나 트라이를 활용해서 문제를 품
            근데 겁나 어려움 ㅋㅋ
            이걸 어떻게 생각해서 구현해... ㅠㅠㅠ
        '''

        trie = Trie()

        # 문자열 삽입
        for i, word in enumerate(words):
            trie.insert(i, word)
        
        # 팰린드롬 검사
        results = []
        for i, word in enumerate(words):

            # extend는 가장 바깥에 있는 반복가능한 객체??를 합쳐줌
            # ex) [1,2].extend([1,2]) => [1,2,1,2]
            results.extend(trie.search(i, word))
        
        return results


obj = Solution()
print(obj.palindromePairs(["abcd","dcba","lls","s","sssll"]))