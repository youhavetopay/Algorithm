def inOrder(root):
    #Write your code here
    data_list = appendData(root, [])
    
    print(' '.join(map(str, data_list)))

def appendData(node, data_list):

    if node.left != None:
        data_list = appendData(node.left, data_list)

    data_list.append(node.info)
    
    if node.right != None:
        data_list = appendData(node.right, data_list)

    return data_list