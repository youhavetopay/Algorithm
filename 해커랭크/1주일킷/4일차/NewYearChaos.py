def minimumBribes(q):
    # Write your code here

    answer = 0
    copy_q = []
    for idx, number in enumerate(q):
        copy_q.append(number)
        if number - (idx + 1) > 2:
            print('Too chaotic')
            return 

    i = 0
    q_length = len(q)
    while i < q_length:
        if i + 1 < copy_q[i]:
            
            for j in range(i + 1, q_length):
                copy_q[i], copy_q[j] = copy_q[j], copy_q[i]
                
                answer += 1
                if copy_q[i] == i + 1:
                    break
           

        i += 1
    print(answer)
    return

q1 = [2,1,5,3,4]
q2 = [1, 2, 5, 3, 7, 8, 6, 4]

print(minimumBribes(q2))