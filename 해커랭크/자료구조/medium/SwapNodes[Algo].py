from collections import defaultdict

class TreeNode():
    def __init__(self, index):
        self.index = index
        self.left = None
        self.right = None

def swapNodes(indexes, queries):
    # Write your code here

    answers = []
    root, depth_info = makeTree(indexes)

    answer, depth_info = makeInorderTree(root)
    print(answer)

    for depth in queries:
        swapTree(depth_info[depth])
        answer, depth_info = makeInorderTree(root)

        answers.append(answer)
        print()

    return answers


def makeTree(indexs):

    
    root = TreeNode(1)

    depth_info = defaultdict(list)

    depth_info[1].append(root)
    now_depth = 1
    pre_node_idx = 0

    for i, value in enumerate(indexs):
        node_idx = i + 1

        if value[0] != -1:
            node = TreeNode(value[0])
            depth = int((node_idx*2) ** (1/2)) + 1
            depth_info[depth].append(node)

            if now_depth < depth-1 or len(depth_info[now_depth]) <= pre_node_idx:
                print()
                now_depth = depth - 1
                pre_node_idx = 0

            depth_info[now_depth][pre_node_idx].left = node

        if value[1] != -1:
            node = TreeNode(value[1])
            depth = int((node_idx*2+1) ** (1/2)) + 1
            depth_info[depth].append(node)

            if now_depth < depth-1 or len(depth_info[now_depth]) <= pre_node_idx:
                print()
                now_depth = depth - 1
                pre_node_idx = 0

            depth_info[now_depth][pre_node_idx].right = node

        print(node_idx, now_depth, pre_node_idx)
        print(depth_info[now_depth][pre_node_idx].index)

        pre_node_idx += 1

        
        
    return root, depth_info

def swapTree(swap_nodes):

    for node in swap_nodes:
        node.left, node.right = node.right, node.left

    return


def makeInorderTree(root):

    datas, new_depth_info = checkInorder(root, [], defaultdict(list), 1)

    return datas, new_depth_info

def checkInorder(node, data, depth_info, depth):

    if node == None:
        return data, depth_info

    depth_info[depth].append(node)

    if node.left:
        data, depth_info = checkInorder(node.left, data, depth_info, depth + 1)
    
    data.append(node.index)

    if node.right:
        data, depth_info = checkInorder(node.right, data, depth_info, depth + 1)


    return data, depth_info


#i1 = [[2, 3], [4, -1], [-1, -1], [-1, -1]]
i1 = [[2, 3], [4, 5], [6, -1], [-1, 7], [8, 9], [10, 11], [12, 13], [-1, 14], [-1, -1], [15, -1], [16, 17], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]
#q1 = [1, 1]
q1 = [2, 3]

print(swapNodes(i1, q1))