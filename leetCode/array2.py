arr = [1,0,1,2,3,4,5,6]

arrLength = len(arr)

i = 0
while i < arrLength:
    if arr[i] == 0:
        for j in range(arrLength-1, i, -1):
            arr[j] = arr[j-1]
        i += 1
    i += 1

print(arr)