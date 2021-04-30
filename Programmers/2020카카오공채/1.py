# 문자열 압축 ㄷㄷ

def solution(s):
    answer = 0
    dp = [0] * len(s)
    for i in range(1,int(len(s)/2)):
        for j in range(len(s)-i):
            tempStr = s[j:i+j]
            print(tempStr)
            dp[i] += s.count(tempStr)
    print(dp)
    return answer

print(solution("ababcdcdababcdcd"))