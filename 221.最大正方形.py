#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#

# @lc code=start
class Solution:
    # 思路 1：动态规划
    # 1. 划分阶段：按照正方形的右下角坐标进行阶段划分。
    # 2. 定义状态 dp[i][j] 表示为：以矩阵第 [i, j] 位置为右下角，且值包含 1 的正方形的最大边长。
    # 3. 状态转移方程：
    # 如果矩阵第 [i, j] 位置为 0 ，则 dp[i][j] = 0。
    # 如果矩阵第 [i, j] 位置为 1，则 dp[i][j] 的值该位置上方、左侧、左上方三者共同约束的，为三者中最小值加 1。即：dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1。
    # 4. 初始条件：凑成总金额为 0 的最少硬币数量为 0，即 dp[0] = 0。
    # 5. 最终结果：根据我们之前定义的状态，dp[i][j] 表示为：以矩阵第 [i, j] 位置为右下角，且值包含 1 的正方形的最大边长。则最终结果为所有 dp[i][j] 中的最大值。
    # 时间复杂度：O(m*n)，其中 m、n 分别为二维矩阵 matrix 的行数和列数。
    # 空间复杂度：O(m*n)
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
        max_size = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                    max_size = max(max_size, dp[i][j])
        return max_size * max_size
                
# @lc code=end

