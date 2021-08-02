class BinNode(): # <-- 이진트리

   def __init__(self, value) -> None:
       self.value = value
       self.left = None
       self.right = None

root = BinNode(1)


def addNode(value):
    global root
   
    point = None
    preNode = root

    if value < root.value:
        point = root.left
    else:
        point = root.right

    while point != None:
        preNode = point

        if value < point.value:
            point = point.left
        else:
            point = point.right
    
    if value < preNode.value:
        preNode.left = BinNode(value)
    else:
        preNode.right = BinNode(value)








