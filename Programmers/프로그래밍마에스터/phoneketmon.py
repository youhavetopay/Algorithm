
def makeMonsterDict(nums):
    monsterDict = {}

    for num in nums:
        try:
            monsterDict[num] += 1
        except KeyError:
            monsterDict[num] = 1

    return monsterDict

def solution(nums):
    answer = 0

    selectCout = len(nums)//2

    monsterDict = makeMonsterDict(nums)

    monsterCount = len(monsterDict.keys())

    if selectCout < monsterCount:
        answer = selectCout
    else:
        answer = monsterCount

    return answer