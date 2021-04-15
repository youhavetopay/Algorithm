count = int(input())

answers = []
for i in range(count):
    n, m = map(int, input().split())

    if n == m:
        answers.append(-1)

    else:
        minValue = 0
        maxValue = 2000000000

        half = int((minValue+maxValue) / 2)

        nowWin = m/n*100
        onePer = nowWin + 1

        while True:
            half = int((minValue+maxValue) / 2)
            nowWin = (m+half)/(n+half)*100
            print(onePer, nowWin, minValue, maxValue, half)
            if nowWin > onePer:
                if maxValue == half:
                    half -= 1
                    break
                maxValue = half
        
            elif nowWin < onePer:
                if minValue == half:
                    half += 1
                    break
                minValue = half
        
            elif nowWin == onePer:
                break
        
        answers.append(half)

for temp in answers:
    print(temp)