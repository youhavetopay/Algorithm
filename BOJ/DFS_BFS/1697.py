# 숨바꼭질

myLoc, broLoc = map(int, input().split())

answer = 0

grahp = {}
visit = [0] * 100001
queue = [myLoc]
grahp[broLoc] = None
maxValue = 0
while grahp[broLoc] == None:
    now = queue.pop(0)
    visit[now] = 1
    one = now - 1
    two = now + 1
    three = now * 2

    if maxValue < three:
        maxValue = three
    
    try:
        if now == broLoc:
            grahp[now] = [one, two, three]
        else:
            temp = grahp[now]
    except KeyError:
        grahp[now]=[one, two, three]
        
        
        for i in grahp[now]:
            if visit[i] == 0:
                queue.append(i)
                visit[i] = 1
    
    myLoc = now




print(grahp)

queue = [myLoc]

visit = [0] * maxValue

nowLoc = myLoc

while nowLoc != broLoc:
    nowLoc = queue.pop(0)
    visit[nowLoc] = 1

    flag = 0
    for i in grahp[nowLoc]:
        if visit[i] == 0:
            queue.append(i)
            flag = 1
            if i == broLoc:
                pass
            

