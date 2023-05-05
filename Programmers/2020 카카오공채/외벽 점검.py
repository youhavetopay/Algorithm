def getLeftNextDist(now, next, max_length):

    dist = 0

    if now < next:
        dist = max_length - next + now
    else:
        dist = now - next
    
    return dist

def getRightNextDist(now, next, max_length):
    dist = 0

    if now > next:
        dist = max_length - now + next
    else:
        dist = next - now
    
    return dist



def check(dists, friends, max_length):

    def dfs(now_dists, now_friends):
        
        # 모든 곳을 수리했을 때 -> 성공
        if len(now_dists) == 0:
            return True

        # 현재 남은 인원이 없을 때 -> 모든 곳을 수리했으면 성공 아니면 실패
        if len(now_friends) == 0:
            return len(now_dists) == 0
        
        # 가장 이동거리가 높은 친구 
        now_friend = now_friends[-1]

        # 남아있는 망가진 곳
        remain_dists = sorted(list(now_dists))

        # 남아있는 곳에서 전부 체크함
        for start_location in range(len(now_dists)):
            
            # 반시계로 탐색
            left_start_fixed = [remain_dists[start_location]]
            left_moved_dist = 0

            i = start_location

            while True:

                now_location = remain_dists[i]

                i -= 1
                if i == -1:
                    i = len(remain_dists) - 1

                next_location = remain_dists[i]

                dist = getLeftNextDist(now_location, next_location, max_length)

                if left_moved_dist + dist <= now_friend:
                    left_moved_dist += dist
                    left_start_fixed.append(remain_dists[i])
                else:
                    break

                if len(left_start_fixed) >= len(remain_dists):
                    return True
                
            
            # 시계방향으로 탐색
            right_start_fixed = [remain_dists[start_location]]
            right_moved_dist = 0
            i = start_location

            while True:
                now_location = remain_dists[i]

                i = (i + 1) % len(remain_dists)

                next_location = remain_dists[i]

                dist = getRightNextDist(now_location, next_location, max_length)

                if right_moved_dist + dist <= now_friend:
                    right_moved_dist += dist
                    right_start_fixed.append(remain_dists[i])
                else:
                    break

                if len(right_start_fixed) >= len(now_dists):
                    return True


            delete_points = []

            # 이동거리 비교
            if left_moved_dist <= right_moved_dist:
                for point in right_start_fixed:
                    now_dists.remove(point)
                
                delete_points = right_start_fixed
            
            else:
                for point in left_start_fixed:
                    now_dists.remove(point)
                
                delete_points = left_start_fixed
            
            now_friends.pop()

            # 다른 친구 진행
            if dfs(now_dists, now_friends):
                return True
            
            for point in delete_points:
                now_dists.add(point)
            
            now_friends.append(now_friend)

        return False

    return dfs(dists, friends)


def solution(n, weak, dist):

    '''
        나의 풀이 (못품 ㅠㅠㅠ 시간 초과랑 테스트케이스 틀림...)
        원형으로 이루어진 외벽을 수리하는데 필요한 최소 인원을 구하는 문제

        나의 접근법(2개 시간초과 랑 테스트케이스 1번 틀림..)
        일단 움직일 수 있는 거리가 가장 많은 사람을 먼저 뽑아서 체크하는 방식으로 접근함
        애초에 인원만 체크하면 되서..

        이동거리가 가장 많은 사람부터 망가진 부분이 있는 모든 곳에서 
        시계방향이 좋은지, 반시계 방향이 좋은지 체크함 -> 이 부분이 가장 잘못된 부분일듯>??? 아마???
        그렇게 DFS로 모든 경우의 수를 계산하고 해당 인원에서 가능하면 해당 인원이 정답

        열심히 했으나.. 못풀어서 너무 아쉬움.....
        레벨 3이 진~~~~~~~~~~짜 어려운듯...
    '''
    # 이동 거리 순으로 정렬
    friends = sorted(dist)
    
    now_friend_count = 1

    # 가능한 인원 1명부터 체크하기
    while now_friend_count < len(friends)+1:

        if check(set(weak), friends[len(friends) - now_friend_count:], n):
            return now_friend_count
        
        now_friend_count += 1


    return -1

#print(solution(12, [10, 0], [1, 2]))

#print(solution(16, [1,2,3,4,5,7,8,10,11,12,14,15], [4,2,1,1]))


#print(solution(50, [1], [6]))

#print(solution(200, [0,50, 100], [1,1]))
#print(solution(200, [0, 10, 50, 80, 120, 160], [1, 10, 5, 40, 30]))
#print(solution(12, [1, 5, 6, 8, 9, 10, 11], [3, 4]))
# print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))

from itertools import permutations

def checkAllFixed(weak, dist):

    print(dist)

    weak_length = len(weak) // 2

    dist_permutations = list(map(list, permutations(dist, len(dist))))

    for now_dists in dist_permutations:
        for i in range(len(weak) - weak_length + 1):

            now_friend = 0

            check_weak = weak[i:i+weak_length]
            print(check_weak)

            max_dist = check_weak[0] + now_dists[now_friend]

            for point in check_weak:

                if max_dist < point:
                    now_friend += 1
                    if now_friend == len(now_dists):
                        break
                    max_dist = point + now_dists[now_friend]
                    
            else:
                return True
        
        
    
    return False


def solutionSecond(n, weak, dist):

    '''
        나의 두번째 풀이
        밑에 다른 사람 풀이 보고 조금..??? 더 효율적으로 풀 수 있을 것 같아서
        해당 풀이를 바탕으로 다시 풀어봄

        엄청~~~크게 줄인건 아니지만
        이동 거리가 높은 친구들을 우선으로 뽑아서 수리보내는 방식으로 품
        이런 풀이로 한다면 무조건 순열을 사용해야 할듯..
        이동거리가 높은 친구를 우선으로 뽑는다 하더라도
        결국 수리 보내는 순서에 따라 정답이 달라짐..
    '''

    dist = sorted(dist, reverse=True)

    new_weak = weak[:]

    for point in weak:
        new_weak.append(point + n)
    
    for now_friend_count in range(1, len(dist) + 1):
        if checkAllFixed(new_weak, dist[:now_friend_count]):
            return now_friend_count
    
    return -1


print(solutionSecond(200, [0, 10, 50, 80, 120, 160], [1, 10, 5, 40, 30]))




def firstSolu(n, weak, dist):

    '''
        다른 사람 풀이
        https://ysyblog.tistory.com/128

        순열을 이용한 풀이법
        길이가 담긴 weak에 * 2를 해서 진행 방향을 신경쓰지 않아도 되게끔 구현함
        ex) 4 -> 9를 갈때 4 -> 9 시계는 9 -> 4갈때 반시계 이고 4 -> 9의 반시계는 9 -> 4의 시계 방향임
        이걸 활용하면 정말 쉽게 풀수 있는듯

        나는 일일히 방향에 따른 위치 계산하느라 고생했는디... ㅋㅋ
    '''

    answer = len(dist) + 1
    weak_length = len(weak)

    for i in range(weak_length):
        weak.append(weak[i] + n)
    
    dist_combi = list(map(list, permutations(dist, len(dist))))

    for i in range(weak_length):
        start = [weak[j] for j in range(i, i + weak_length)]

        for dist_p in dist_combi:
            result = 1
            dist_distance = 0
            check_len = start[0] + dist_p[0]

            for k in range(weak_length):
                if start[k] > check_len:
                    result += 1

                    if result > len(dist_p):
                        break
                    dist_distance += 1
                    check_len = start[k] + dist_p[dist_distance]
            
            answer = min(answer, result)
    
    if answer > len(dist):
        return -1
    
    return answer