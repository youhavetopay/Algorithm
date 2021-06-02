# 전기 버스

import sys

input = sys.stdin.readline

def gotoBus(canGo, dst, chargeCount, chargLocs):
    busLoc = 0
    count = 0
    answer = 0
    while True:
        busLoc = busLoc + canGo
        
        if busLoc >= dst:
            return answer

        for index, value in enumerate(chargLocs):
            if value <= busLoc:
                count = index
            else:
                break
        
        busLoc = chargLocs[count]
        
        answer += 1

        if answer > chargeCount:
            return 0


testCount = int(input().strip())

for test_case in range(1, testCount + 1):
    
    canGo, dst, chargeCount = map(int, input().strip().split())

    chargeLocations = list(map(int, input().strip().split()))

    print('#'+str(test_case),gotoBus(canGo, dst, chargeCount, chargeLocations))