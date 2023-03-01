import collections

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        '''
            나의 풀이(못품)

            문자열에서 k개 만큼 바꿔서 연속된 같은 문자의 최대길이를 구하는 문제

            너무 어려움...ㅜㅜ
            슬라이딩 윈도우 문제는 너무 어려운듯..

            내 접근법은
            정답의 범위가 k+1 부터 s의 길이 까지라서
            윈도우 크기를 k+1 부터 늘려가면서 탐색하는 방법으로 접근함

            시간초과도 뜨고 풀이도 올바르지 못함
        '''

        window_size = k + 1

        while window_size <= len(s):
            
            # s를 윈도우 크기만큼 짜르면서 탐색
            for i in range(len(s)-window_size+1):
                now_s = s[i: i+window_size]

                # 빈도수 체크
                counter = collections.Counter(now_s)

                # 한 단어 밖에 없는경우 -> 모두 같은 문자
                if len(counter.keys()) == 1:
                    break
                
                sorted_counter = sorted(list(counter.items()), key=lambda x: -x[1])

                # 빈도순으로 정렬해서 가장 많이 나온 문자의 수와 k를 합쳤을 때
                # 현재 윈도우의 크기를 넘어가면 모두 같은 문자로 만들 수 있음
                if sorted_counter[0][1] + k >= len(now_s):
                    break
                
                # 이 외에는 어떻게 해야할 지 모르겠음 ㅠㅠ
                

            else:
                window_size -= 1
                break

            window_size += 1
            
        if window_size > len(s):
            return len(s)
        
        return window_size
    
    def firstSoul(self, s: str, k: int) -> int:

        '''
            책 풀이
            투포인터, Counter를 활용한 풀이

            right를 하나씩 증가시키면서 Counter에 빈도수를 저장
            가장 많이 나오는 빈도수를 가져와서
            현재 윈도우의 길이 - 최대 빈도수 <= k를 만족하는 left와 right를 구함
            만약 만족하지 않는다면 left를 당기면서 윈도우 길이를 줄여나가면서
            최대 길이를 찾는 방법

            나랑 접근법이 비슷했는데
            내가 투포인터를 사용하지 않고 고정된 윈도우 크기를 계속 반복 비교해서 그런지
            더 비효율적인것 같음
            그리고 most_common이라는 걸 사용하면 쉽게 최다 빈도수를 가져올 수 있음
        '''

        left = right = 0
        counts = collections.Counter()
        for right in range(1, len(s) + 1):
            counts[s[right - 1]] += 1

            max_char_n = counts.most_common(1)[0][1]

            if right - left - max_char_n > k:
                counts[s[left]] -= 1
                left += 1
    
        return right - left

obj = Solution()
print(obj.characterReplacement("ABAB", 2))