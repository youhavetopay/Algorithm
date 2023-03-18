import collections

def solution(cacheSize, cities):
    
    '''
        나의 풀이
        LRU 방식의 캐시를 구현하는 문제

        최신?? 파이썬에는 dict형식이 순서를 보장하기 때문에
        그대로 dict형식을 사용해도 되지만
        혹시 몰라서 순서를 보장해주는 OrderedDict을 사용함

        사용한 도시는 삭제했다가 뒤에 다시 넣어주고
        가득 찼다면 앞에 있는 도시를 지우고 새로운 도시를 뒤에 넣어주는
        방식으로 품

        어렵지 않았음

    '''


    answer = 0

    if cacheSize == 0:
        return len(cities) * 5

    cache = collections.OrderedDict()

    for city in cities:
        
        lower_city = city.lower()

        if lower_city not in cache:
            answer += 5

            if len(cache.keys()) == cacheSize:
                del cache[list(cache.keys())[0]]
            
            
            cache[lower_city] = 1
        
        else:
            answer += 1
            del cache[lower_city]
            cache[lower_city] = 1


    return answer


print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))


def firstSoul(cacheSize, cities):

    '''
        책 풀이
        deque를 활용한 풀이

        나도 처음에 deque를 생각했었지만
        remove하는게 시간초과에 걸릴 것 같아서
        삭제하는데 O(1)인 dict을 사용했는데
        지금보니 캐시의 최대 크기는 30까지라서
        괜찮은듯??

        그러다보니 코드도 디게 깔끔해서 보기 좋은듯함
    '''

    elapsed: int = 0
    cache = collections.deque(maxlen=cacheSize)

    for c in cities:
        c = c.lower()

        if c in cache:
            cache.remove(c)
            cache.append(c)
            elapsed += 1
        else:
            cache.append(c)
            elapsed += 5

    return elapsed