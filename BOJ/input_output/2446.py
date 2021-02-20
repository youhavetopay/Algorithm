value = int(input())

for i in range(value):
    print(' '*i + '*'*((2*value)-(i*2)-1))

for i in range(value-2, -1, -1):
    print(' '*i + '*'*((2*value)-(i*2)-1))

# for n in range(-num+1,num):
# 	print(' '*(num-abs(n)-1) + '*'*(2*abs(n)+1))
# 절대값으로 줄어들었다 커지기 ㄷ ㄷ