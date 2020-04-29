class Solution:
    def maximalSquare(self, matrix) -> int:
        max_square = 0
        if matrix:
            rows, cols = len(matrix), len(matrix[0])
            dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]

            for i in range(rows):
                for j in range(cols):
                    if matrix[i][j] == '1':
                        dp[i+1][j+1] = min(dp[i+1][j], dp[i][j],dp[i][j+1]) + 1
                        max_square = max(max_square, dp[i+1][j+1])
                    else:
                        dp[i+1][j+1] = 0
        
        return max_square * max_square