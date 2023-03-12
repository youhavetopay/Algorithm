
import collections

class Solution:

    nums = [0, 1]
    
    def fib(self, n: int) -> int:

        '''
            나의 풀이
            피보나치 수열 구하는 문제

            DP문제의 가장 기본이 되는 문제라서 
            많이 풀어봐서 그런지 디게 쉬웠음
        '''

        if len(self.nums) == n+1:
            return self.nums[n]
        
        else:
            while len(self.nums) < n+1:
                self.nums.append(self.nums[-1] + self.nums[-2])

            return self.nums[n]
        
    '''
        책 풀이는 다음에..
    '''

    def firstSoul(self, n: int) -> int:
        if n <= 1:
            return n
        return self.firstSoul(n-1) + self.firstSoul(n-2)
    

    dp = collections.defaultdict(int)
    def secondSoul(self, n: int) -> int:

        if n <= 1:
            return n
        
        if self.dp[n]:
            return self.dp[n]
        
        self.dp[n] = self.secondSoul(n-1) + self.secondSoul(n-2)

        return self.dp[n]
    
    def thirdSoul(self, n: int) -> int:
        self.dp[0] = 0
        self.dp[1] = 1

        for i in range(2, n+1):
            self.dp[i] = self.dp[i-1] + self.dp[i-2]

        return self.dp[n]
    
    def fouthSoul(self, n: int) -> int:
        x, y = 0, 1

        for i in range(0, n):
            x, y = y, x + y
        
        return x
    
    def fifthSoul(self, n: int) -> int:
        M = np.matrix([[0,1], [1,1]])

        vec = np.array([[0], [1]])

        return np.matmul(M ** n, vec)[0]