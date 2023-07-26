
'''
    백준 5639. 이진 검색 트리

    전위 순회 결과가 주어지면 후위 순회를 출력하는 문제
'''

import sys
sys.setrecursionlimit(100_000)
input = sys.stdin.readline


preorder = list(map(int, sys.stdin.readlines()))


def postorder(tree, now):

    if tree[now][0]:
        postorder(tree, tree[now][0])
    
    if tree[now][1]:
        postorder(tree, tree[now][1])

    print(now)

def solution(nums):

    '''
        나의 풀이

        나의 접근법
        걍 숫자 주어지면 트리를 만들어서
        이전 숫자보다 작으면 이전숫자의 왼쪽에 넣어주고
        아니면
        루트부터 탐색해서 알맞는 자리에 넣어줌

        그 후 완성된 트리에서 후위 순회 해줌

        이번 문제는 입력을 희한하게 해서
        좀 이상했음 ㅋㅋ
    '''

    tree = {}

    if nums:
        tree[nums[0]] = [None, None]

    for i in range(1, len(nums)):
        tree[nums[i]] = [None, None]

        now = nums[0]
        num = nums[i]
        while True:

            if now < num:
                if tree[now][1] == None:
                    tree[now][1] = num
                    break
                else:
                    now = tree[now][1]
            else:
                if tree[now][0] == None:
                    tree[now][0] = num
                    break
                else:
                    now = tree[now][0]


    postorder(tree, nums[0])
    
    return

solution(preorder)


def firstSolu():

    '''
        다른 사람 풀이
        https://ku-hug.tistory.com/132

        맨 앞이 루트이고 루트보다 큰 숫자가 나오는 곳 부터가 루트의 오른쪽 서브트리임
        나머지는 왼쪽 서브트리

        이런식으로 계속 이어가면 됨 ㅋㅋ

        그리고 옛날에는 문제 난이도가 실버 1인듯 ㅋㅋ
    '''

    pre = []

    while True:
        try:
            pre.append(int(input()))
        except:
            break

    def post(start, end):
        if  start > end:
            return
        
        mid = end + 1
        for i in range(start + 1, end + 1):
            if pre[i] > pre[start]:
                mid + 1
                break

        post(start + 1, mid - 1)
        post(mid, end)
        print(pre[start])
    
    post(0, len(pre) - 1)