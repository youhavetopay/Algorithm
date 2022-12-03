from collections import deque

class BinNode():
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

def topView(root):
    #Write your code here

    
    max_left = 0
    max_rigth = 0

    queue = deque([root.info])

    
    queue = findNode(queue, max_left, max_rigth, 0, root)

    print()
    print(' '.join(map(str, queue)))

    return

def findNode(queue, max_left, min_right, now_loc, now_node):

    if now_loc > max_left:
        queue.appendleft(now_node.info)
        max_left = now_loc
    elif now_loc < min_right:
        queue.append(now_node.info)
        min_right = now_loc


    if now_node.left != None:
        print(queue, now_loc, now_node.info, now_node.left.info)
        queue = findNode(queue, max_left, min_right, now_loc + 1, now_node.left)
    
    if now_node.right != None:
        print(queue, now_loc, now_node.info, now_node.right.info, 'right')
        queue = findNode(queue, max_left, min_right, now_loc - 1, now_node.right)


    return queue


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