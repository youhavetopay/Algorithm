def solution(k, room_number):

    '''
        나의 풀이(못품..)
        원하는 호텔 방을 지정해주는 문제

        나의 접근법
        (풀이법 보고 한거라서 의미없음 ㅋㅋ)

        해시에 다음에 넣어줄 방 번호를 담아주는 방식으로 품?

        문제 너무 어렵다...
        효율성에서 많이 부족한듯 함
    '''

    hotel = {}

    # 방 요청 번호를 순회
    for number in room_number:
        
        # 아직 방을 할당하지 않았다면
        # 해당 방번호 + 1을 담아줌
        if number not in hotel:
            hotel[number] = number + 1
        else:
            # 만약에 해당 방 번호가 할당되었다면
            # DFS 를 해야함

            # 방문한 방 번호들
            visit = []
            # 현재 방 번호
            now_room = hotel[number]

            # 할당되지 않은 방이 될때까지 탐색하기
            while now_room in hotel:
                visit.append(now_room)
                now_room = hotel[now_room]
            
            # 방문했던 방의 다음 번호를 업데이트 해주기
            for room in visit:
                hotel[room] = now_room + 1
            
            # 방 할당해주기
            hotel[now_room] = now_room + 1
            
                
    print(hotel)

    return list(hotel.keys())

print(solution(10, [1,3,4,1,3,1]))



def firstSolu(k, room_number):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이

        나랑 똑같은..?? 풀이
        훨씬 깔끔한듯??
    '''

    room_dic = {}
    ret = []
    
    for i in room_number:
        n = i
        visit = [n]

        while n in room_dic:
            n = room_dic[n]
            visit.append(n)

        ret.append(n)

        for j in visit:
            room_dic[j] = n + 1
    
    return ret