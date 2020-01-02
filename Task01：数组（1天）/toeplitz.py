class Solution:
    '''
    托普利茨矩阵问题
    '''
    def isToeplitzMatrix(self, matrix) -> bool:
        for i in range(len(matrix)-1):
            for j in range( len(matrix[0])-1) :
                if matrix[i][j]!=matrix[i+1][j+1]:
                    return False
        return True

if __name__ == '__main__':
    matrix = [
        [1, 2, 3, 4],
        [5, 1, 2, 3],
        [9, 5, 1, 2]
    ]
    solution = Solution()
    output = solution.isToeplitzMatrix(matrix)
    print(output)