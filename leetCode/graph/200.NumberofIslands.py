from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        '''
            나의 풀이
            2차원 배열 1로 이루어진 덩어리 갯수 찾는 문제
            -> 서로 연결된 그래프?? 몇개인지 찾는 문제
            난 재귀 DFS로 품
        '''

        def DFS(stack):
            vecters = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            if not stack:
                return

            for vec in vecters:
                now_loc = stack[-1]
                y, x = now_loc[0] + vec[0], now_loc[1] + vec[1]

                if 0 <= y < len(grid) and 0 <= x < len(grid[y]):
                    if grid[y][x] == '1':
                        stack.append([y,x])
                        grid[y][x] = "2"
                        DFS(stack)

            stack.pop()

        stack = []
        islans_count = 0

        for y in range(len(grid)):
            for x in range(len(grid[y])):

                if grid[y][x] == '1':
                    stack.append([y, x])
                    grid[y][x] = "2"
                    DFS(stack)

                    for temp in grid:
                        print(temp)

                    islans_count += 1



        return islans_count

    def firstSoul(self, grid: List[List[str]]) -> int:

        '''
            책 풀이
            나랑 똑같이 중첩함수에다 재귀 DFS로 구현함
            대신 stack을 사용하는 것이 아닌
            위치 정보를 넘겨서 판별함

            풀이를 stack이 따로 필요가 없는 것 같음
            grid에다가 값을 표기하면 굳이 스택이 필요없을 듯
            이렇게 하니 시간복잡도랑 공간복잡도가 좋아짐
            한 30ms, 0.1mb 정도??
        '''

        def dfs(i, j):
            if i < 0 or i >= len(grid) or \
                j < 0 or j >= len(grid[0]) or \
                    grid[i][j] != '1':
                        return

            grid[i][j] = '0'

            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)

                    count += 1

        return count


obj = Solution()

print(obj.numIslands([["1","1","1","1","1","1","1"]]))