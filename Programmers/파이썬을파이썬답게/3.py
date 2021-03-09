s, n = input().strip().split(' ')
n = int(n)

print(s)
print(' '*(int((n-len(str(s)))/2)) + s)
print(' '*((n-len(str(s)))) + s)


# 이게 답 
print(s.ljust(n))
print(s.center(n))
print(s.rjust(n))