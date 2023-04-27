import collections

def solution(gems):

    answer = []

    gem_kinds = set(gems)
    if len(gem_kinds) == 1:
        return [1, 1]

    now_gem = collections.defaultdict(int)

    left, right = 0, 1

    now_gem[gems[left]] += 1
    now_gem[gems[right]] += 1

    max_length = float('inf')


    while right < len(gems) and left < right:

        print(left, right, answer, now_gem)

        
        if len(now_gem.keys()) == len(gem_kinds):
            
            while now_gem[gems[left]] > 2:
                now_gem[gems[left]] -= 1
                left += 1

            answer.append([left+1, right+1])

            max_length = min(max_length, right - left + 1)
        
        right += 1
        now_gem[gems[right]] += 1
        
        if max_length < right - left + 1:
            now_gem[gems[left]] -= 1
            if now_gem[gems[left]] == 0:
                del now_gem[gems[left]]
            left += 1
        
    print(answer)
    answer.sort(key=lambda x: (x[1] - x[0], x[0]))

    return answer[0]

print(solution(	["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))