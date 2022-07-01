def countLenCableOfLength(cables, length):
    count = 0
    for cable in cables:
        count += cable // length
    
    return count

K, N = map(int, input().split(' '))

len_cables = []

for i in range(K):
    len_cables.append(int(input()))

start = 1
end = max(len_cables)
mid = (start + end) // 2

max_length = []

while start <= end:
    count = countLenCableOfLength(len_cables, mid)
    if count < N:
        end = mid - 1
    elif count >= N:
        start = mid + 1
        max_length.append(mid)
    
    mid = (start + end) // 2

print(max(max_length))