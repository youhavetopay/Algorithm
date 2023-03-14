import collections

class Solution:
    
    def climbStairs(self, n: int) -> int:
        
        '''
            나의 풀이
            숫자가 주어졌을때 1과 2로 만들 수 있는 경우의 수를
            계산하는 문제

            직접 경우의 수를 계산해보니 피보나치 수열이 나와서
            해보니 풀림.. ㅋㅋ
            easy라서 그런지 어렵지 않았음
        '''

        dp = [0, 1, 2]

        while len(dp) - 1 < n:
            dp.append(dp[-2] + dp[-1])

        return dp[n]
    
    def firstSoul(self, n: int) -> int:

        '''
            첫번째 책 풀이(시간초과)

            경우의수는 피보나치의 수열이기 때문에
            피보나치를 구하는 방법으로 풀면된다고 함

            문제를 바로 봤을 때는 피보나치를 연상하기 어려워서
            조금은 힘들 수도 있다고 함

            모든 경우의 수를 재귀로 찾아가기 때문에
            시간초과가 뜸

        '''

        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        return self.firstSoul(n-1) + self.firstSoul(n-2)
    
    dp = collections.defaultdict(int)

    def secondSoul(self, n: int) -> int:

        '''
            두번째 책 풀이
            그냥 첫번째 풀이에 메모제이션을 추가한 풀이법
            사실상 피보나치 구하는 문제 ㅋㅋ
        '''

        if n <= 2:
            return n
        
        if self.dp[n]:
            return self.dp[n]
        
        self.dp[n] = self.secondSoul[n-1] + self.secondSoul[n-2]

        return self.dp[n]