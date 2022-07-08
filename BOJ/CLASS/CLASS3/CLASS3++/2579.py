import sys
input = sys.stdin.readline

step_count = int(input())

step = []
for _ in range(step_count):
    step.append(int(input()))


# step_count = 6
# step = [
#     10,
#     20,
#     15,
#     25,
#     10,
#     20
# ]

def findMaxStepValue():

    dp = [0] * (step_count)

    dp[0] = step[0]
    
    if step_count >= 2:
        dp[1] = dp[0] + step[1]
        if step_count >= 3:
            dp[2] = max(dp[0] + step[2], step[1] + step[2])

            for i in range(3, step_count):
                dp[i] = max(dp[i-3] + step[i-1] + step[i], dp[i-2] + step[i])
        
    print(dp[step_count-1])
    return

findMaxStepValue()