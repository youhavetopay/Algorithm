from collections import defaultdict

class BinNode():
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

from collections import defaultdict


def topView(root):
    max_left = 0
    max_rigth = 0
    dict_list = defaultdict(list)
    
    dict_list = findNode(dict_list, max_left, max_rigth, 0, root)

    data_list = []
    flag = True

    # 키를 기준으로 정렬하기 
    for key in sorted(list(dict_list.keys()), reverse=True):
        if key < 0:
            if flag: # root 노드 넣어주기
                data_list.append(root.info)
                flag = False
            data_list.append(dict_list[key][-1]) # 오른쪽 노드 넣어주기
        elif key > 0:
            data_list.append(dict_list[key][0]) # 왼쪽 노드 넣어주기
        

    print(' '.join(map(str, data_list)))

    return

def findNode(dict_list, max_left, min_right, now_loc, now_node):
    if now_loc > max_left: # 현재 위치가 가장 왼쪽 일때
        dict_list[now_loc].append(now_node.info)
        max_left = now_loc
    elif now_loc < min_right: # 현재 위치가 가장 오른쪽 일때
        dict_list[now_loc].append(now_node.info)
        min_right = now_loc


    if now_node.left != None: # 왼쪽 자식 노드가 있다면 들어가기
        dict_list = findNode(dict_list, max_left, min_right, now_loc + 1, now_node.left)
    
    if now_node.right != None: # 오른쪽 자식 노드가 있다면 들어가기
        dict_list = findNode(dict_list, max_left, min_right, now_loc - 1, now_node.right)


    return dict_list


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