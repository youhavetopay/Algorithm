def getTargetNodePath(node, arr, target):

    if not node:
        return arr

    if node.info == target:
        arr.append(node)
        return arr
    
    if node.info < target:
        arr.append(node)
        arr = getTargetNodePath(node.right, arr, target)

    else:
        arr.append(node)
        arr = getTargetNodePath(node.left, arr, target)
    
    return arr

def lca(root, v1, v2):
  #Enter your code here
  
  v1_path = getTargetNodePath(root, [], v1)
  v2_path = getTargetNodePath(root, [], v2)

  sum_path = list(set(v1_path) & set(v2_path))

  data_list = []
  for node in sum_path:
    data_list.append([node.info, node])
  
    
  answer = sorted(data_list, key=lambda x: x[0])
  
  if v1 <= root.info and v2 <= root.info:
    return answer[0][1]
  elif v1 >= root.info and v2 >= root.info:
    return answer[-1][1]

  return answer[0][1]
