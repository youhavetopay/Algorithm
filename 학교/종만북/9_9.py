count, p, l = map(int, input().split())
dragon = 'FX'
answer = dragon

for level in range(count):
    i = 0
    while i < len(dragon):
        
        if dragon[i] == 'X':
            dragon = dragon[0:i]+'X+YF'+dragon[i+1:len(dragon)]
            i += 4
            continue
        if dragon[i] == 'Y':
            dragon = dragon[0:i]+'FX-Y'+dragon[i+1:len(dragon)]
            i += 4
            continue
        
        i += 1

print(dragon[p-1:p+l-1])