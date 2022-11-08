def dynamicArray(n, queries):
    # Write your code here

    array = [ [] for _ in range(n) ]
    last_answer = 0

    answers = []
    for querie in queries:
        if querie[0] == 1:
            x, y = querie[1], querie[2] 
            idx = (x ^ last_answer) % n

            array[idx].append(y)

        else:
            x, y = querie[1], querie[2]
            idx = (x ^ last_answer) % n
            last_answer = array[idx][y % len(array[idx])]
            answers.append(last_answer)

    return answers

n1 = 2
q1 = [
    [1,0,5], [1,1,7], [1,0,3],
    [2,1,0], [2,1,1]

]

print(dynamicArray(n1, q1))