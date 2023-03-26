import collections

def solution(nums):

    '''
        나의 풀이
        숫자리스트에서 숫자의 종류를 계산해서
        최대 length // 2 만큼 선택하는데 가장 많은 종류를 계산하는 문제


        defaultdict을 사용해서 카운트?해서 하면됨
        지금보니 그냥 Counter 써도 상관없을듯 ㅋㅋㅋ

        디게 쉬웠음 ㅋㅋ 레벨 1이라서 그런듯??
        예전에도 풀었었는데 그때도 지금이랑 비슷하게 풀었음
        대신 일반 dict을 사용해서 KeyError 처리를 직접했었음 ㅋㅋ
    '''

    phone_ket_info = collections.defaultdict(int)
    for num in nums:
        phone_ket_info[num] += 1

    print(phone_ket_info)
    total_get_count = len(nums) // 2

    phone_ket_type_count = len(phone_ket_info.keys())

    if phone_ket_type_count >= total_get_count:
        return total_get_count

    return phone_ket_type_count

print(solution([3,3,3,2,2,4]))


def firstSoul(nums):

    '''
        다른 사람 풀이
        https://life-of-panda.tistory.com/78

        굳이 카운팅을 할 필요없이 
        중복을 제거하면 쉽게 풀림 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
        이게 훨씬 빠름 ㅋㅋㅋ
    '''

    unique_types = len(set(nums))
    if len(nums) / 2 > unique_types:
        return unique_types
    
    return len(nums) // 2