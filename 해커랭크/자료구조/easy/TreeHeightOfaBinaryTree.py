def height(root):

    height = findHeight(root, 0)

    return height
   

def findHeight(node, height):

    now_height = height

    if node.left != None:
        now_height = findHeight(node.left, height + 1)
    
    if node.right != None:
        now_height = findHeight(node.right, height + 1)
    
    return max(now_height, height)