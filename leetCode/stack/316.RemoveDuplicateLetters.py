import collections

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        '''
            내가 작성한 코드
            틀림..
            아예 접근 방법부터 다름ㅋ
        '''

        answer = ''
        max_length = len(s)

        dup_letters = set()
        for i, word in enumerate(s):
            if word in dup_letters:
                continue

            if i - 1 == max_length:
                answer += word
                break
            
            if word not in set(s[i+1:]):
                answer += word
            else:
                j = i + 1

                flag = False
                while j + 1 < max_length and s[j] in set(s[j+1:]):

                    if ord(s[j]) < ord(word) and word in set(s[j+1:]):
                        flag = True
                        break

                    j += 1

                if flag:
                    continue

                if ord(word) <= ord(s[j]):
                    answer += word
                    dup_letters.add(word)
        
        return answer

    def firstSoul(self, s: str) -> str:

        '''
            첫번째 책 풀이
            재귀를 활용한 풀이

            set으로 중복을 제거한 다음 사전순서대로 정렬

            그 후 해당 문자가 가능한지? 체크하고 
            가능하다면 더하고 해당 문자 제거 하고 새로 진행

            안된다면 넘어가고 다른문자 체크

            이걸 어떻게 생각해ㅋㅋ
        '''

        for word in sorted(set(s)):

            suffix = s[s.index(word):]

            if set(s) == set(suffix):
                return word + self.firstSoul(suffix.replace(word, ''))

        return ''

    def secondSoul(self, s: str) -> str:

        '''
            두번째 책 풀이
            스택을 활용한 풀이
            현재 문자가 더 빠르고 뒤에 더 담을게 있다면 스택에서 빼기
        '''

        counter, seen, stack = collections.Counter(s), set(), []

        for word in s:
            # 남은 문자 갯수 빼기
            counter[word] -= 1

            # 이미 넣은 문자라면 다른거 검색
            if word in seen:
                continue
            
            # 만약에 word가 top보다 빠르면 담았던거 없애기
            # 뒤에 더 담을게 있을 경우만(counter가 0이상일때..)
            while stack and word < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            
            # 스택에 추가
            stack.append(word)

            # 이거 대신에 그냥 stack에서 검색해도 되는데
            # 책에선 최대한 stack을 사용하려고 이걸로 중복검사
            seen.add(word)
        
        return ''.join(stack)