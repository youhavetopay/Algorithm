import heapq

def convertTimeToMinute(time):
    h, m = map(int, time.split(':'))

    m += h * 60

    return m

def solution(book_time):


    '''
        나의 풀이
        호텔 입실시간과 퇴실시간이 주어질때
        최소 몇개의 방이 있어야 하는지 계산하는 문제

        나의 접근법
        입실시간을 기준으로 정렬을하고
        퇴실시간을 기준으로 heap에 넣으면서
        heap 의 길이를 체크하면서 품

        집중이 잘 안되서 생각보다 오래걸림 ㅋㅋㅋㅋ

    '''

    answer = 0

    heap = []

    convert_book_time = []

    for start, end in book_time:
        start_m, end_m = convertTimeToMinute(start), convertTimeToMinute(end)
        convert_book_time.append([start_m, end_m])

    convert_book_time.sort(key=lambda x:(x[0], x[1]))

    heapq.heappush(heap, (convert_book_time[0][1], convert_book_time[0][0]))

    print(convert_book_time)
    
    i = 1
    while heap:

        while i < len(convert_book_time) and heap[0][0] + 10 > convert_book_time[i][0]:
            heapq.heappush(heap, (convert_book_time[i][1], convert_book_time[i][0]))
            i += 1
        
        print(heap, i)
        answer = max(len(heap), answer)

        if i < len(convert_book_time):
            while heap and convert_book_time[i][0] >= heap[0][0] + 10:
                heapq.heappop(heap)
        else:
            break



    return answer

print(solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]))


def firstSolu(book_time):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이

        뜨하... ㅋㅋㅋ
        시간을 배열로 표현해서
        해당 시간대에 1을 더해줌
        겹치는 시간대를 찾아서 최대값을 넘겨주면 됨 ㅋㅋㅋㅋㅋ
        heap 도 필요가 없네 ㅋㅋㅋㅋㅋㅋ
    '''

    time_table = [0 for _ in range(60 * 24)]

    for start, end in book_time:
        start_minutes = 60 * int(start[:2]) + int(start[3:])
        end_minutes = 60 * int(end[:2]) + int(end[3:]) + 10

        if end_minutes > 60 * 24 - 1:
            end_minutes = 60 * 24 - 1
        
        for i in range(start_minutes, end_minutes):
            time_table[i] += 1

    return max(time_table)