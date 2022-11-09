def rotateLeft(d, arr):
    # Write your code here

    rotated_arr = []
    idx = d

    arr_length = len(arr)

    while len(rotated_arr) < arr_length:

        rotated_arr.append(arr[idx])

        idx += 1

        if idx == arr_length:
            idx = 0


    return rotated_arr


d1 = 4
arr1 = [1,2,3,4,5]
print(rotateLeft(d1, arr1))