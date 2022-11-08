def reverseArray(a):
    # Write your code here

    reversed_a = []

    for i in range(len(a)-1, -1, -1):
        reversed_a.append(a)


    return reversed_a


a1 = [1,2,3,4,5]
print(reverseArray(a1))