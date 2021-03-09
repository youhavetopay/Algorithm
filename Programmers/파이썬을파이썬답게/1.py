a, b = map(int, input().strip().split(' '))
print('%d %d'%(a//b, a%b))


#이게 파이썬 답게 
# 큰 숫자를 다룰땐 이게 좋음
print(*divmod(a,b))