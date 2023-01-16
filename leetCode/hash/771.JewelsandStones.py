import collections

class Solution:

    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        '''
            나의 풀이
            돌 중에 보석이 몇개 있는지 카운팅 하는 문제

            그냥 보석이름을 key로 가지는 dict 만들어서
            해당하는 key가 있으면 카운팅하고
            keyError 뜨면 넘어가는 형식으로 구현함
        '''

        jewels_info = {}

        for jewel in jewels:
            jewels_info[jewel] = True
        

        jewel_count = 0
        for stone in stones:
            try:
                if jewels_info[stone]:
                    jewel_count += 1

            except KeyError:
                continue


        return jewel_count

    def firstSoul(self, jewels: str, stones: str) -> int:
        
        '''
            첫번째 책 풀이
            나머지 풀이는 시간복잡도는 거의 비슷하나 코드를 줄이는 방법
            나랑 반대로 함 ㅋㅋ
        '''

        freqs = {}
        for char in stones:

            # 이렇게 key 있는지 없는지 검사할 수 있음
            # 앞으론 굳이 try except 안해도 될듯 ㅋㅋ
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] += 1
        
        count = 0
        for char in jewels:
            if char in freqs:
                count += freqs[char]
        
        return count
    
    def secondSoul(self, jewels: str, stones: str) -> int:
        
        '''
            두번째 책 풀이
            첫번째 풀이랑 똑같은데
            defaultdict 써서 in 검사하는 코드를 생략함
        '''

        freqs = collections.defaultdict(int)
        for char in stones:
            freqs[char] += 1
        
        count = 0
        for char in jewels:
            count += freqs[char]

        return count

    def thirdSoul(self, jewels: str, stones: str) -> int:
        
        '''
            세번째 책 풀이
            처음에 돌을 세는 부분을 Counter로 함
            Counter에 값을 넣으면 각각 몇개가 있는지 알려줌
        '''
        freqs = collections.Counter(stones)

        count = 0
        for char in jewels:
            count += freqs[char]

        return count
    
    def fourthSoul(self, jewels: str, stones: str) -> int:
        '''
            네번째 책 풀이
            파이썬 다운 풀이라고 함 ㅋㅋ
            [s for s in stones] 하면은 [1, 2, 4, 5, ,6] 이렇게 되는데
            여기서 char in jewels를해서 True, False 이렇게 나옴
            그럼 이걸 sum으로 계산하면 끝..
        '''
        return sum(char in jewels for char in stones)