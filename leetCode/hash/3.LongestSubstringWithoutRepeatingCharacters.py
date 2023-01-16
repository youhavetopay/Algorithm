import collections

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        '''
            나의 풀이
            중복되지 않으면서 연속된 가장 긴 문자열의 길이를 찾는 문제

            일단 문자열을 순회하면서
            중복되지 않은 문자는 dict에 index를 담아둠
            만약 중복된 문자가 나왔다면 
            이전에 담아둔 문자의 다음부터 다시 시작 -> dict는 비우고

        '''

        max_length = 0
        word_info = {}

        idx = 0
        length = len(s)

        while idx < length:

            if s[idx] not in word_info:
                word_info[s[idx]] = idx
            else:
                max_length = max(max_length, len(word_info))

                idx = word_info[s[idx]]
                word_info = {}
            idx += 1

        max_length = max(max_length, len(word_info))

        return max_length

    def mySecondSoul(self, s: str) -> int:
        '''
            나의 두번째 풀이
            책에 풀이로 투포인터를 활용하였길래
            좀 다시 생각해봤는데 queue로도 구현이 가능한 것 같아서 구현해봄

            set()자료형이 in 연산이 O(1) 이라서 이걸로 중복검사를 진행함
            계속 queue랑 set()에 넣다가
            중복이 생기면
            queue에 중복된 글자가 없을 때 까지 빼고 
            다시넣기

            이렇게 하니까 시간복잡도가 많이 줄어듬
            위에껀 400ms 정도이고 이거는 50ms 정도
        '''

        word_set = set()
        deque = collections.deque()

        max_length = 0
        for word in s:

            if word in word_set:
                max_length = max(max_length, len(deque))

                while word in word_set:
                    word_set.remove(deque.popleft())
    
            deque.append(word)
            word_set.add(word)

        max_length = max(max_length, len(deque))
        return max_length

    def firstSoul(self, s: str) -> int:

        '''
            책 풀이
            나의 첫번째 풀이랑 유사함

            똑같이 dict에 index를 넣지만
            거기부터 다시 탐색을 하는게 아니라
            그냥 위치만 갱신시키고 다음꺼로 넘어감

            이게 좀더 맞는듯
            찾은 문자열을 넘겨주는게 아니라 단순히 길이만 필요한거니까..
            index를 통해 길이 계산이 가능하기 때문에
        '''

        used = {}
        max_length = start = 0
        for index, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_length = max(max_length, index - start + 1)

            used[char] = index
        
        return max_length
    

obj = Solution()

print(obj.lengthOfLongestSubstring("dvdf"))
