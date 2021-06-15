T = int(input())

for test_case in range(1,T+1):
    str1 = list(input())
    str2 = list(input())

    answer = 0

    str1 = set(str1)
    
    for word1 in str1:
        count = 0
        
        for word2 in str2:

            if word1 == word2:
                count += 1

                if count > answer:
                    answer = count

    print('#'+str(test_case), answer)