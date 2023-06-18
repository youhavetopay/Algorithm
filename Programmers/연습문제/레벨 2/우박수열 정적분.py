def solution(k, ranges):

    '''
        나의 풀이(접근법 보고 품 ㅠㅠ)
        콜라츠의 추측의 결과값을 좌표평면에 나타내고
        그려지는 그래프를 통해 일정 구간의 정적분을 구하는 문제
        
        정적분이란?
        대충 일정구간의 x축에서 함수값까지의 도형 넓이? 정도?

        나의 접근법
        콜라츠 추측 값을 일단 구하고
        정적분에 대해 알아봤는데
        정적분을 하려면 함수 f(x)를 적분해서 F(b) - F(a) 를 하면 된다고 했는데
        함수를 몰라서 고민좀 하다가 이것저것 알아보다가 
        결국 질문하기를 통해서 접근법을 알게 됨

        아직 콜라츠 추측은 함수로 표현을 못하기에 정적분을 못한다고 함
        그래도 넓이는 구할 수 있다고 해서 보니 
        n, n-1 의 구간의 도형은 삼각형과 사각형으로 이루어져 있어서
        삼각형의 넓이와 사각형의 넓이를 더해주는 방식으로 풀게됨

        처음에 문제 이해가 안되서 한참 걸림 ㅋㅋㅋ
        정적분이 어떤것인지 알고 구간이 삼각형과 사각형으로 이루졌다는 것만 
        알면 쉽게 풀 수 있을 듯??

    '''

    answer = []

    collatzs = [k]
    def make_collatz(now):

        if now % 2 == 0:
            now = now // 2
        else:
            now = now * 3 + 1
        
        if now >= 1:
            collatzs.append(now)
            if now > 1:
                make_collatz(now)
    
    make_collatz(k)
    print(collatzs)

    for start, end in ranges:
        end = len(collatzs) + end - 1
        if start == end:
            answer.append(0)
        elif start > end:
            answer.append(-1)
        else:
            total_area = 0
            if start == 0 and k % 2 != 0:
                total_area = 2 * (collatzs[1] - k) * (1/2) * (1/2)
                total_area += k

                for i in range(2, end+1):
                    total_area += (2 * (collatzs[i-1] - collatzs[i]) * (1/2) * (1/2))
                    total_area += collatzs[i]
            
            else:
                for i in range(start+1, end+1):
                    total_area += (2 * (collatzs[i-1] - collatzs[i]) * (1/2) * (1/2))
                    total_area += collatzs[i]

            answer.append(total_area)



    return answer

print(solution(	5, [[0, 0], [0, -1], [2, -3], [3, -3]]))


def firstSolu(k, ranges):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/134239/solution_groups?language=python3

        구간합으로 미리 구간들의 넓이를 만들어주는듯?
        나는 해당 구간의 넓이를 계속 새로 구해서
        조금 비효율적인듯 함

        구간합 대박 ㅋㅋㅋ
    '''

    answer = []
    arr = [k]
    while k > 1:
        if not k % 2:
            k //= 2
        else:
            k = k * 3 + 1
        
        arr.append(k)
    
    area = [0]
    for i in range(len(arr)-1):
        arr.append(area[-1] + (arr[i] + arr[i+1]) / 2)
    
    for a, b in ranges:
        if a >= len(area) or b - 1 < -len(area):
            answer.append(-1)
        elif area[b-1] - area[a] < 0:
            answer.append(-1)
        else:
            answer.append(area[b-1] - area[a])

    return answer