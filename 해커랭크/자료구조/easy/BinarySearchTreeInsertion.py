def insert(self, val):
        #Enter you code here.
    root = self.root

    if not root:
        self.root = Node(val)
        return

    now_node = root
    new_node = Node(val)
    while True:
        if now_node.info <= val:
            if now_node.right:
                now_node = now_node.right
            else:
                now_node.right = new_node
                return
        elif now_node.info > val:
            if now_node.left:
                now_node = now_node.left
            else:
                now_node.left = new_node
                return