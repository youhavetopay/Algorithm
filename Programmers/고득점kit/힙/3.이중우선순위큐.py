import heapq

def solution(operations):

    '''
        나의 풀이
        최소값과 최대값을 삭제할 수 있는 우선순위 큐를 만드는 문제

        최대 힙, 최소 힙 이렇게 두개 만들어서 풀었음
        삭제한 리스트를 만들어서 힙의 루트 값이 삭제한 리스트에 들어있다면
        없애주는 방식으로 품

        힙을 두개 만들어서 푸는 접근까지는 디게 빨랐는데
        이를 구현하는데 생각보다 오래걸림 ㅋㅋ

        입력값이 100만이라서 효율성 걱정했는데 효율성 테스트는 없어서 좀 의야했음 ㅋㅋㅋ
    '''

    # 삭제한 값들
    # 검색 시간복잡도 때문에 set()으로 함
    delete_set = set()

    # 최소, 최대 힙
    min_heap, max_heap = [], []

    for operation in operations:
        oper, num = operation.split(' ')
        num = int(num)

        # 삽입 시
        # 최소, 최대 힙에 같이 넣어 줌
        if oper == 'I':
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
        else:
            
            # 최대 값 삭제 시
            if num == 1:

                # 최대 힙이 있고 루트값이 삭제 한 값이 아닐때
                # 삭제하고 삭제 리스트에 추가
                if max_heap and -max_heap[0] not in delete_set:
                    delete_set.add(-heapq.heappop(max_heap))
            
            # 최소 값 삭제 시
            else:
                if min_heap and min_heap[0] not in delete_set:
                    delete_set.add(heapq.heappop(min_heap))
        
        # 현재 루트 값이 삭제 리스트에 있을때
        # 즉 이미 삭제한 값일 때 전부 삭제
        while max_heap and -max_heap[0] in delete_set:
            heapq.heappop(max_heap)
        while min_heap and min_heap[0] in delete_set:
            heapq.heappop(min_heap)

        print(operation)
        print(min_heap)
        print(max_heap)
        print(delete_set)
        print()


    min_num, max_num = 0, 0
    if min_heap:
        min_num = min_heap[0]
    if max_heap:
        max_num = -max_heap[0]

    return [max_num, min_num]

# print(solution(["I 3", "I 2", "I 1", "D 1", "D 1", "I 3", "D -1"]	))


def firstSoul(operations):

    '''
        다른 사람 풀이
        https://velog.io/@younge/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%9D%B4%EC%A4%91%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84%ED%81%90-%ED%9E%99

        나랑 비슷하게 heap 두개를 사용해서 품
        대신 중복값을 제거하는데 set을 사용한게 아니라
        그냥 remove로 삭제함..

        이거 시간복잡도가 걸릴것 같은디..??
        operations 길이가 100만인데 아마 데이터는 얼마 없고 연산만 잔뜩 있는듯 ㅋㅋㅋㅋ
    '''

    heap = []
    max_heap = []

    for o in operations:
        current = o.split()

        if current[0] == 'I':
            num = int(current[1])
            heapq.heappush(heap, num)
            heapq.heappush(max_heap, (num*-1, num))
        
        else:

            if len(heap) == 0:
                pass
            elif current[1] == '1':
                max_value = heapq.heappop(max_heap)[1]
                heap.remove(max_value)
            elif current[1] == '-1':
                min_value = heapq.heappop(heap)
                max_heap.remove((min_value*-1, min_value))
    
    if heap:
        return [heapq.heappop(max_heap)[1], heapq.heappop(heap)]

    else:
        return [0, 0]
    
print(firstSoul(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))



def secondSoul(operations):


    '''
        다른 사람 풀이 2
        https://velog.io/@norighthere/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Python-%EC%9D%B4%EC%A4%91%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84%ED%81%90

        신기하게 heap을 하나만 사용해서 품
        heapq.nlargest()를 사용해서 list에서 가장 큰 수를 찾아 낼 수 있음
        반대로 heapq.nsmallest()를 사용해서 가장 작은 수도 찾아 낼 수 있음 ㅋㅋ

        파이썬에선 참 다양한 메소드를 제공하는 듯 함 ㅋㅋㅋ

        코드 형태가 위에 사람이랑 조금..비슷한듯..??? ㅋㅋㅋㅋ
    '''


    answer = []
    heap = []

    for data in operations:

        if data[0] == 'I':
            heapq.heappush(heap, int(data[2:]))

        else:
            if len(heap) == 0:
                pass
            elif data[2] == '-':
                heapq.heappop(heap)
            else:
                heap = heapq.nlargest(len(heap), heap)[1:]
                heapq.heapify(heap)
    
    if heap:
        answer.append(max(heap))
        answer.append(min(heap))
    
    else:
        answer.append(0)
        answer.append(0)
    
    return answer