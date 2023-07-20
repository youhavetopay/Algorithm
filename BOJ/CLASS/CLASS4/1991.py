
'''
    백준 1991. 트리 순회

    트리 연결정보가 주어지면
    전위, 중위, 후위 순회의 결과를 출력하는 문제
'''

import sys
input = sys.stdin.readline

N = int(input())

tree_nodes = [ list(input().rstrip().split()) for _ in range(N)]

def solution(n, tree_nodes):

    '''
        나의 풀이

        나의 접근법
        dict 자료형으로 트리 만들고
        재귀로 구현함

        솔직히 어떤게 루트인지 말 안해줬으면
        좀 더 귀찮았을듯.. ㅋㅋㅋ
    '''

    tree = {}

    for parent, left_child, right_child in tree_nodes:
        tree[parent] = [None, None]
        if left_child != '.':
            tree[parent][0] = left_child
        if right_child != '.':
            tree[parent][1] = right_child


    preorder_result = ['']
    def preorder(now):

        preorder_result[0] += now

        if tree[now][0]:
            preorder(tree[now][0])

        if tree[now][1]:
            preorder(tree[now][1])
    
    inorder_result = ['']
    def inorder(now):

        if tree[now][0]:
            inorder(tree[now][0])

        inorder_result[0] += now

        if tree[now][1]:
            inorder(tree[now][1])

    postorder_result = ['']
    def postorder(now):

        if tree[now][0]:
            postorder(tree[now][0])

        if tree[now][1]:
            postorder(tree[now][1])

        postorder_result[0] += now

    preorder('A')
    inorder('A')
    postorder('A')

    print(preorder_result[0])
    print(inorder_result[0])
    print(postorder_result[0])

    return

solution(N, tree_nodes)




def firstSolu():

    '''
        다른 사람 풀이
        https://jm-codingmemo.tistory.com/22

        나랑 똑같은 풀이

        굳이 나처럼 문자열에 담지 말고
        바로바로 출력하는게 훨씬 좋은 듯 함 ㅋㅋ
    '''

    N = int(sys.stdin.readline().strip())
    tree = {}

    for n in range(N):
        root, left, right = sys.stdin.readline().strip().split()
        tree[root] = [left, right]
    

    def preorder(root):
        if root != '.':
            print(root, end='')
            preorder(tree[root][0])
            preorder[tree[root][1]]
    
    def inorder(root):
        if root != '.':
            inorder(tree[root][0])
            print(root, end='')
            inorder[tree[root][1]]
    
    def postorder(root):
        if root != '.':
            postorder(tree[root][0])
            postorder[tree[root][1]]
            print(root, end='')
    
    preorder('A')
    print()
    inorder('A')
    print()
    postorder('A')