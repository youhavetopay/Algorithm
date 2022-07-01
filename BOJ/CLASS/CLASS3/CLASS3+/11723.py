import sys
input = sys.stdin.readline

set_list = set([])

order_count = int(input())

while order_count > 0:
    order = list(map(str, input().split(' ')))
    
    if len(order) > 1:
        order[1] = int(order[1][0])
    else:
        order[0] = order[0][:-1]
        
    if order[0] == 'add':
        set_list.add(order[1])
    elif order[0] == 'remove':
        if order[1] in set_list:
            set_list.remove(order[1])
    elif order[0] == 'check':
        if order[1] in set_list:
            print(1)
        else:
            print(0)
    elif order[0] == 'toggle':
        if order[1] in set_list:
            set_list.remove(order[1])
        else:
            set_list.add(order[1])
    elif order[0] == 'all':
        set_list = set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    elif order[0] == 'empty':
        set_list = set([])

    order_count -= 1