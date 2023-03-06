from typing import List
import heapq

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        '''
            나의 풀이
            주유소에서 충전하면서 다시 돌아올 수 있는 시작 위치를 찾는 문제

            겁나 꾸역꾸역 품 ㅋㅋㅋㅋㅋ 시간복잡도 5%(3980ms) ㅋㅋㅋㅋㅋㅋㅋㅋㅋ
            
            현재 주유소의 기름 양 - 다음 주유소까지의 거리를 heapq에 넣고
            가장 많이 남는 곳을 먼저 체크해서 품

            더 효율적인 풀이가 있을 수도 있지만
            내 머리론 여기까지....ㅋㅋㅋ
        '''

        total_gas = sum(gas)
        total_cost = sum(cost)

        # 기름 총합이 거리의 총합 보다 작으면 어떤 곳에서도 출발 못함
        if total_cost > total_gas:
            return -1
        

        heap = []
        diff_gas = []
        # 해당 위치에서 출발 할 수 있는지 체크
        for idx, (fuel, length) in enumerate(zip(gas, cost)):
            # 기름의 차이 계산해서 넣기
            diff_gas.append(fuel - length)

            # 출발할 수 있으면 heap에 넣기
            if fuel - length >= 0:
                heapq.heappush(heap, (-(fuel - length), idx))
        
        print(heap)
        # heap에 아무것도 남지 않을 때 까지
        while len(heap):
            _, idx = heapq.heappop(heap)

            start_idx = (idx + 1) % len(gas)
            now_fuel = diff_gas[idx]

            # 해당 위치에서 다시 돌아 올때까지
            while start_idx != idx:
                now_fuel += diff_gas[start_idx]

                # 기름 모자라면 끝내기
                if now_fuel < 0:
                    break

                start_idx = (start_idx + 1) % len(gas)
            
            else:
                # 기름이 모자르지 않았다면 정답 -> 정답이 유일하다고 했음
                return idx


        return -1
    
    def firstSoul(self, gas: List[int], cost: List[int]) -> int:
        
        '''
            첫번째 책 풀이(시간초과)
            그냥 처음부터 끝까지 하나씩 다 확인하는 방법
            O(n^2) 이라서 시간초과 뜸

            시간초과 뜬거와는 별개로 코드는 참 깔끔한듯 ㅋㅋ
        '''

        for start in range(len(gas)):

            fuel = 0
            for i in range(start, len(gas) + start):
                index = i % len(gas)

                can_travel = True
                if gas[index] + fuel < cost[index]:
                    can_travel = False
                    break
                else:
                    fuel += gas[index] - cost[index]
                
            if can_travel:
                return start
            
        return -1

    def secondSoul(self, gas: List[int], cost: List[int]) -> int:
        
        '''
            두번째 책 풀이

            시간복잡도 23%인데 1050ms라서 나의 풀이보다 거의 4배 빠름

            정답이 무조건 하나이므로 
            해당 위치에서 출발하지 못하면 앞부분에서도 성립이 안되기 때문에
            뒤로 한칸씩 체크함
            귀류법? 활용해서 앞에서 안되면 뒤에서는 가능하다는 것??

            좀 어려움 ㅋㅋ
        '''

        # 불가능한 경우
        # 이 경우를 제외하면 무조건 답이 있음
        if sum(gas) < sum(cost):
            return -1
        
        start, fuel = 0, 0
        for i in range(len(gas)):
            # 현재 주유소의 기름과 지금까지의 기름합을 더한걸로 다음 위치로 못갈 경우
            # 정답이 아니기 때문에 
            # start위치를 앞으로 한칸 뒤로 밀고
            # 현재 연료 초기화
            if gas[i] + fuel < cost[i]:
                start = i + 1
                fuel = 0
            else:
                # 기름 더하기
                fuel += gas[i] - cost[i]
        
        return start

obj = Solution()
print(obj.canCompleteCircuit([5,8,2,8], [6,5,6,6]))