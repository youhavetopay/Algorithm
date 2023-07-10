def solution(number, k):
    
    '''
        나의 풀이(못품 ㅠㅠ)

        문자열로 이루어진 숫자가 있을때
        K개를 지우고 만들수 있는 최대의 수를 구하는 문제
        (숫자들의 기존 순서는 유지)

        나의 접근법
        탐욕법이라고 해서 비교적 쉬울 줄 알았는데
        진짜 답도 없음...
        도대체 뭐가 최적의 해인지 1도 모르겠음..

        처음엔 최대 길이가 100만이길래 heap으로 해볼려고 했는데 
        아니였음(입출력 예제 3번에 걸림)

        그래서 이것 저것 시도해보다가 결국
        밑에 답이 최선...(1번 틀리고 10번 시간초과..)
        으아...탐욕문제가 수학 문제 다음으로 제일 싫음..ㅋ
    '''

    remove_count = 0

    numbers = list(map(int, number))
    
    # 앞에서 최대 값을 찾음
    # 단 앞에서 다 못뺄 경우 뒤에 것도 남겨둔 상태까지만
    max_idx = 0
    i = 1
    while i < len(numbers) - remove_count - 1:

        if numbers[max_idx] < numbers[i]:
            max_idx = i

            remove_count = i
            if remove_count == k: # 앞에서 다 뺀경우
                return number[i:]

        i += 1
    
    # 앞에거 잘라내기
    numbers = numbers[max_idx:]

    # 다시 끝까지 탐색
    # 중간에 빼면서 -> 중간에서 다 뺐으면 끝내기
    i = 1
    right = i + 1
    while remove_count < k and right < len(numbers):
        
        # 나의 오른쪽 값이 더 클때
        if numbers[i] < numbers[right]:
            # 나를 빼기
            numbers.pop(i)
            remove_count += 1
            i -= 1
            
        else:
            i += 1

        right = i + 1

    
    # 중간에서도 다 못뺀 경우
    # 뒤에서 부터 빼기
    while remove_count < k:
        if numbers[-1] < numbers[-2]:
            numbers.pop()
        else:
            numbers.pop(len(numbers) - 2)

        remove_count += 1


    return ''.join(map(str, numbers))

print(solution("10001", 3))


def firstSolu(number, k):

    '''
        다른 사람 풀이
        https://chiefcoder.tistory.com/37

        뭔가 간단할 것 같았음..
        역시나.. ㅋㅋㅋ

        그냥 이거 스택문제였음...
        문제 유형에 탐욕법 없었으면 풀 수 있었을지도..

        내가 넣을 값보다 top값이 낮으면 top이 더 높을때까지 pop()해주고

        마지막에 아직 뺄 수가 남았다면 
        끝에서 제거해주기 
    '''

    answer = []

    for i in number:
        while k > 0 and answer and answer[-1] < i:
            answer.pop()
            k -= 1
        
        answer.append(i)
    
    return ''.join(answer[:len(answer) - k])