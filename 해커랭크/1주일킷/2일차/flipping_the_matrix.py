def flippingMatrix(matrix, n):
    # Write your code here
    
    answer = 0
    
    for i in range(n):
        for j in range(n):
            # 어떻게 해서든 무조건 이 자리에 올수 있어서?? 걍 끝에있는 최대값 구해서 반환
            answer += max(matrix[i][j], matrix[i][n*2-j-1], matrix[n*2-1-i][j], matrix[n*2-1-i][n*2-j-1])
    
    return answer