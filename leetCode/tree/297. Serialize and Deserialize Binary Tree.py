# Definition for a binary tree node.

import collections

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        '''
            나의 풀이
            
            이진트리를 문자열로 만들었다가 다시 이진트리로 만드는 문제

            내 풀이로는 시간초과 남 ㅠㅠ

            Queue를 이용해서 직렬화 하고 다시 Queue를 이용해서 했는데
            너무 복잡하게 한듯..
            뭐지..
            
        '''

        serial_tree = [None]

        if root is None:
            return ''

        queue = collections.deque([[root, 0]])


        while queue:

            node, idx = queue.popleft()

            while len(serial_tree) <= idx:
                serial_tree.append('None')
            
            serial_tree[idx] = str(node.val)

            if node.left:
                queue.append([node.left, idx*2+1])
            
            if node.right:
                queue.append([node.right, (idx+1)*2])

        return ','.join(serial_tree)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        if not data:
            return None


        data = 'None,'+ data

        datas = list(data.split(','))
        datas_length = len(datas)

        root = TreeNode(datas[1])
        queue = collections.deque([[root, 1]])

        while queue:

            node, idx = queue.popleft()

            if idx * 2 < datas_length and datas[idx*2] != 'None':
                left_node = TreeNode(int(datas[idx*2]))
                node.left = left_node
                
                queue.append([left_node, idx*2])
            
            if idx * 2 + 1 < datas_length and datas[idx*2+1] != 'None':
                right_node = TreeNode(int(datas[idx*2+1]))
                node.right = right_node
                
                queue.append([right_node, idx*2+1])


        return root

    
    def firstSoul1(self, root):

        '''
            책 풀이
            나랑 유사한 방식으로 풀이함 똑같이 Queue를 사용함

            굳이 차이점이라고 하면 index 계산을 안한거..?
            이게 그렇게 차이가 크나..????

            암튼 코드도 디게 깔끔하고 보기 좋은듯 함
            내가 너무 불필요한 연산?? 을 너무 많이 한듯..??
        '''

        queue = collections.deque([root])

        result = ['#']

        while queue:

            node = queue.popleft()

            if node:
                queue.append(node.left)
                queue.append(node.right)

                result.append(str(node.val))
            else:
                
                result.append('#')
        
        return ' '.join(result)
    
    def firstSoul2(self, data):

        if data == '# #':
            return None
        
        nodes = data.split()

        root = TreeNode(int(nodes[1]))
        queue = collections.deque([root])

        index = 2

        while queue:
            node = queue.popleft()
            if nodes[index] is not '#':
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            
            index += 1

            if nodes[index] is not '#':
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)

            index += 1
        
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))