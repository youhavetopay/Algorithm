# 듣보잡

N, M = map(int, input().split())

personListDic = {}

for _ in range(N+M):
    name = input()

    try:
        personListDic[name] += 1
    
    except KeyError:
        personListDic[name] = 1

answers = []

for key, value in personListDic.items():
    if value > 1:
        answers.append(key)

print(len(answers))
for name in sorted(answers):
    print(name)