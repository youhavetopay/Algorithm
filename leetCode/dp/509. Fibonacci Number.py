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