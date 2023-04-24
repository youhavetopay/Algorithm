import heapq

def solution1(stones, k):

    '''
        나의 풀이 (못품..)
        징검다리를 최대 몇명까지 건널수 있는지 체크하는 문제

        나의 접근법 (효율성을 하나도 통과못함.. ㅋㅋㅋ)
        힙에 인덱스랑 돌값을 넣어주고
        최소값이랑 해당 인덱스를 차례대로 빼면서
        인덱스를 따로 모아둠
        
        그리고 인덱스를 정렬해서
        연속된 숫자가 K개 만큼 나오면
        해당 최소값 만큼 건널 수 있으므로 해당 최소값이 정답

        근데 데이터 수가 최대 20만이라서
        시간복잡도가 너무 안좋아서 못품 ㅠㅠ
    '''

    heap = []

    # 힙 만들어주기
    for i, stone in enumerate(stones):
        heapq.heappush(heap, (stone, i))

    # 최소값이랑 인덱스 담아두기
    last_stone, idx = heapq.heappop(heap)
    stone_idxs = [idx]

    while heap:
        
        # 방금뺀 값이랑 지금 최소값이랑 같으면
        # 계속 빼주기 -> 어차피 같은 값이라면 굳이 계속 체크할 필요가 없어서??
        while last_stone == heap[0][0]:
            last_stone, idx = heapq.heappop(heap)
            stone_idxs.append(idx)
        
        # 인덱스들 정렬
        stone_idxs.sort()
        print(stone_idxs)
        
        # 연속된 숫자가 몇개인지 체크하기
        count = 1
        for i in range(1, len(stone_idxs)):
            if stone_idxs[i] - 1 == stone_idxs[i-1]:
                count += 1

                if count >= k:
                    break
            else:
                count = 1

        if count >= k:
            break
            
        last_stone = heap[0][0]
        print()

    return last_stone



def solution2(stones, k):

    '''
        나의 풀이 2
        근데 사실상 풀이법을 보고 한거라서
        그냥 풀이법을 코드로 나타낸거 밖에.. ㅋㅋ

        접근법
        최대값이 2억이므로
        1 ~ 2억까지 이진탐색을 진행하면서
        건널 수 있으면 올리고
        건너지 못하면 내리는 방식으로 하면 된다고 함 ㅋㅋ

        애초에 이진탐색 자체가 시간복잡도가 엄~~~~~~~청 낮기 때문에
        배열 순회 * 이진탐색 횟수를 해도 사실상 O(N) 이라서 
        가능하다고 함

        데이터 수가 너무 많거나 하면
        이진탐색을 고려하는 것도 좋은 방법이라고 함.
    '''

    # 최소값, 최대값
    left = 1
    right = 200_000_000

    # 이진탐색 시작
    while left <= right:

        center = (left + right) // 2
        print(left, right, center)

        # 0보다 작은 숫자의 연속성 체크
        count = 0
        for stone in stones:
            if stone - center <= 0:
                count += 1
                if count == k:
                    break
            else:
                count = 0

        if count >= k:
            right = center - 1
        else:
            left = center + 1


    return left

print(solution2([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))


def firstSolu(stones, k):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이

        똑같이 이진탐색으로 풀이를 하심
        대신 체크하는 부분을 문자열로 변환을 해서
        연속된 못건너는 돌을 체크함
    '''
    
    left = 0
    right = max(stones) + 1

    def compare(mid):
        # 대충 돌의 숫자가 mid보다 크면 T 아니면 F으로 해서
        # T를 기준으로 스플릿 하고 길이를 체크하는 방식으로 체크
        return any(len(i) >= k for i in ''.join(['T' if i > mid else 'F' for i in stones]).split('T'))
    
    while left < right:
        mid = (left + right) // 2
        if compare(mid):
            right = mid
        else:
            left = mid + 1

    return right