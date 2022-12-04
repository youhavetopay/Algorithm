from collections import defaultdict


def levelOrder(root):
    #Write your code here

    level_dict = defaultdict(list)
    now_level = 0
    
    level_dict = findNode(root, now_level, level_dict)

    datas = []

    for key in sorted(level_dict.keys()):
        for data in level_dict[key]:
            datas.append(data)

    print(' '.join(map(str, datas)))

    return


def findNode(now_node, now_level, level_dict):

    level_dict[now_level].append(now_node.info)

    if now_node.left:
        level_dict = findNode(now_node.left, now_level + 1, level_dict)
    
    if now_node.right:
        level_dict = findNode(now_node.right, now_level + 1, level_dict)

    return level_dict

