
'''
    프로그래머스 행렬의 곱셈
    2차원 행렬 두개가 주어지면 행렬 곱셈의 결과를 반환하는 문제
'''

def solution(arr1, arr2):

    '''
        나의 풀이

        나의 접근법
        곱할 수 있는 행렬만 주어진다고 해서
        예외처리 할것도 없었음 ㅋㅋㅋ

        그냥 행렬의 곱셈을 그대로 구현함
    '''

    answer = []

    for k in range(len(arr1)):
        row = []
        for j in range(len(arr2[0])):
            
            num = 0
            for i in range(len(arr1[0])):
                num += (arr1[k][i] * arr2[i][j])
            
            row.append(num)
        
        answer.append(row)

    return answer

print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))