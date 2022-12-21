def check_binary_search_tree_(root):

    datas = search_tree(root, [])

    answer = True
    for idx, num in enumerate(datas):
        if idx == 0:
            continue

        if datas[idx-1] >= num:
            answer = False
            break

    return answer

def search_tree(node, datas):

    if node.left:
        datas = search_tree(node.left, datas)

    datas.append(node.data)   
    
    if node.right:
        datas = search_tree(node.right, datas)
    
    return datas