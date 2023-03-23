def solution(numbers):

    '''
        나의 풀이
        숫자 리스트가 주어졌을 때 조합해서 가장 큰 수를 만드는 문제

        예전에 LeetCode 에서 풀어봄 ㅋㅋ(179. Largest Number)
        차이점은 데이터 크기가 프로그래머스가 훨씬 커서 

        그때 풀이를 사용하면 시간초과가 뜸(여기는 최대 10만개)

        그때는 삽입정렬을 사용했는데
        퀵정렬을 사용해서 풀어봄

        이전에 똑같은 문제를 풀었음에도 불구하고 꽤나 힘들었음 ㅋㅋ
        그때 풀이를 보고 삽입정렬을 했는데 안되길래 
        꾸역꾸역 최적화 해보다가 실패하고 정렬알고리즘을 바꾸니 성공함 ㅋㅋ
    '''

    def check(n1, n2):
        if str(n1) + str(n2) < str(n2) + str(n1):
            return True
        
        return False
    
    def quick_sort(nums):

        if len(nums) <= 2:
            if len(nums) == 2 and check(nums[0], nums[1]):
                nums[0], nums[1] = nums[1], nums[0]
                return nums
            
            return nums

        center = len(nums) // 2
        left = []
        right = []

        for i in range(len(nums)):
            if i == center:
                continue

            if check(nums[i], nums[center]):
                right.append(nums[i])
            else:
                left.append(nums[i])
        
        left = quick_sort(left)
        right = quick_sort(right)
        left.append(nums[center])

        return left + right

    
    return str(int(''.join(map(str, quick_sort(numbers)))))


print(solution([3, 30, 34, 5, 9]))


def firstSoul(numbers):
    '''
        다른 사람 풀이
        https://jokerldg.github.io/algorithm/2021/05/06/most-big-number.html

        이렇게 간단하게 풀다니.. ㅋㅋㅋㅋㅋ

        파이썬에서 문자열 비교는 아스키 값을 기준(사전순?)으로 하는걸 이용해서
        전부 문자로 바꿔 주고
        x0... , x는 x가 먼저 와야하기 때문에 x를 xxx 이렇게 바꿔줘서 정렬함
        ex) "30", "3" 으로 정렬하면 ["30", "3"] 이렇게 되기 때문에
        "303030", "333" 이렇게 만들고 정렬 -> 최대값이 1000이하 라서
        
        
        지금와서 생각해보니 어차피 정렬하는건데
        조건만 잘 설정하면 직접 정렬을 구현하는것보단
        내장 함수를 사용하는게 훨씬 빠르고 간결하니 
        좀더 생각해보는게 좋을듯 함 ㅋㅋ
    '''

    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
