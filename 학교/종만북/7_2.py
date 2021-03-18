

# # c = int(input())



# def divTree(testTree):
#     print(testTree)
#     tempTree = []
#     i = 0
#     checkList = [False for _ in range(len(testTree))]
#     while i < len(testTree):

#         print(i, len(testTree), testTree[i], tempTree)

#         if testTree[i] == 'x' and not checkList[i]:

#             temp2List = divTree(testTree[i+1:])

#             tempTree.append(temp2List)
#             for x in range(i, len(temp2List)):
#                 checkList[i] = True
#             i += len(temp2List)+1

#         elif not checkList[i]:
#             if i > 4:
#                 break
#             tempTree.append(testTree[i])
#             checkList[i] = True
#             i += 1

#         elif checkList[i]:
#             i += 1

#         print(checkList)
    
#     return tempTree

# qTree = input()

# answerTree = divTree(qTree)


# print(answerTree)

testCase = int(input())
tree = ''
count1 = 0

def reverse(count):
    global count1
    head = tree[count]
    
    count1 += 1
    if head == 'w' or head == 'b':
        return head
    
    upperLeft = reverse(count1)
    upperRight = reverse(count1)
    lowLeft = reverse(count1)
    lowRight = reverse(count1)

    return 'x' + lowLeft + lowRight + upperLeft + upperRight
answers = []
while testCase:
    testCase -= 1

    tree = input()
    answers.append(reverse(0))
    count1 = 0

for i in answers:
    print(i)