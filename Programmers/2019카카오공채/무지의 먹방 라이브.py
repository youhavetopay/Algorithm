def solution(food_times, k):

    '''
        나의 풀이(못품 ㅠㅠ)
        음식을 차례대로 먹을때 N초되면 다음 먹어야하는 음식을 찾는 문제

        나의 접근법
        음식 양을 기준으로 정렬을 한다음
        인덱스를 차례대로 뽑아서 계속 빼주는 방식으로 했는데
        효율성 하나 빼고 다 실패.. ㅠㅠ

        다 먹은 음식을 삭제해줄려고 dict에다 했지만
        애초에 음식 하나씩 빼는게 아닌듯함..
        정렬 혹은 힙을 하는건 맞는것 같은데
        그 이후를 모르겠음 ㅠㅠ
    '''

    answer = 0

    if sum(food_times) <= k:
        return -1
    
    length = len(food_times)
    if length > k:
        return k + 1
    
    temp = []
    food_idx_by_time = {}
    for idx, time in enumerate(food_times):
        temp.append([time, idx+1])
        food_idx_by_time[idx+1] = time

    temp.sort(reverse=True)
    now_k = k

    while temp:
        
        min_time_idx = temp.pop()[1]
        while min_time_idx not in food_idx_by_time:
            min_time_idx = temp.pop()[1]
        
        span_time = food_idx_by_time[min_time_idx]
        idx_keys = list(food_idx_by_time.keys())
        idx_length = len(idx_keys)
        
        if now_k < span_time * idx_length:
            span_time = int(now_k / idx_length)
                
        if span_time == 0:
            break

        for key in idx_keys:
            food_idx_by_time[key] -= span_time
            if food_idx_by_time[key] == 0:
                del food_idx_by_time[key]

        now_k -= span_time * idx_length
            
    

    print(food_idx_by_time, now_k)
    idx_keys = list(food_idx_by_time.keys())

    answer = idx_keys[now_k]

    return answer

print(solution([3,4,1], 5))

import heapq

def firstSolu(food_times, k):

    '''
        다른 사람 풀이
        https://mjmjmj98.tistory.com/149

        역시.. 힙을 사용하는게 맞았었음...ㅠㅠ

        너무 간단해서 놀람 ㅋㅋㅋㅋ
    '''
    
    answer = -1
    h = []

    # 힙에다가 넣어주기
    for i in range(len(food_times)):
        heapq.heappush(h, (food_times[i], i+1))
    
    # 음식 개수
    food_num = len(food_times)

    # 이전에 제거한 음식의 시간
    previous = 0

    while h:

        # 현재 양이 가장 적게 남은 음식을 먹는 시간
        # 단, 이전에 시간을 빼주기(이미 먹으면서 지나갔을 테니)
        t = (h[0][0] - previous) * food_num

        # 해당 음식을 먹을 수 있을 때
        if k >= t:

            # 해당 시간 빼주고
            k -= t
            # 다음 음식 가져오기
            previous, _ = heapq.heappop(h)
            # 하나먹었으니까 빼주기
            food_num -= 1

        else:
            # 해당 음식을 다 못 먹을 때
            # 남은 음식중 먹어야 하는 음식 찾기
            idx = k % food_num

            # 음식 번호를 기준으로 정렬
            h.sort(key=lambda x: x[1])
            answer = h[idx][1]
            break

    return answer