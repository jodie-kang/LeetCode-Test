#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#


# @lc code=start
class Solution:
    # 动态规划：
    # 定义状态 dp[i][j] 为：从左上角到达 (i, j) 位置的最小路径和。
    # 当前位置 (i, j) 只能从左侧位置 (i, j - 1) 或者上方位置 (i - 1, j) 到达。为了使得从左上角到达 (i, j) 位置的最小路径和最小，应从 (i, j - 1) 位置和 (i - 1, j) 位置选择路径和最小的位置达到 (i, j)。
    # 即状态转移方程 dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]。
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]

        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]
        return dp[m - 1][n - 1]


# @lc code=end
