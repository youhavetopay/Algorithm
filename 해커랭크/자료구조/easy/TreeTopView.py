from collections import defaultdict

class BinNode():
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

def topView(root):
    #Write your code here

    
    max_left = 0
    max_rigth = 0

    dict = defaultdict(list)

    
    dict = findNode(dict, max_left, max_rigth, 0, root)

    print(dict)

    data_list = []
    flag = True

    for key in sorted(list(dict.keys()), reverse=True):
        if key < 0:
            if flag:
                data_list.append(root.info)
                flag = False
            data_list.append(sorted(dict[key], reverse=True)[0])
        elif key > 0:
            
            data_list.append(sorted(dict[key])[0])
        


    print(' '.join(map(str, data_list)))

    return

def findNode(dict, max_left, min_right, now_loc, now_node):

    if now_loc > max_left:
        dict[now_loc].append(now_node.info)
        max_left = now_loc
    elif now_loc < min_right:
        dict[now_loc].append(now_node.info)
        min_right = now_loc


    if now_node.left != None:
        dict = findNode(dict, max_left, min_right, now_loc + 1, now_node.left)
    
    if now_node.right != None:
        dict = findNode(dict, max_left, min_right, now_loc - 1, now_node.right)


    return dict


def test():

    a = [14, 3, 7, 4, 5, 15, 6, 13, 10, 11, 2, 12, 8, 9]
    root = BinNode(1)

    for num in a:
        node = root

        while True:
            if node.info < num:

                if node.right:
                    node = node.right
                else:
                    node.right = BinNode(num)
                    break
            elif node.info > num:
                if node.left:
                    node = node.left
                else:
                    node.left = BinNode(num)
                    break


    topView(root)

    return

test()