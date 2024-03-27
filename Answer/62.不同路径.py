#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    # 定义状态 dp[i][j] 为：从左上角到达 (i, j) 位置的路径数量。
    # 因为我们每次只能向右、或者向下移动一步，因此想要走到 (i, j)，只能从 (i - 1, j) 向下走一步走过来；或者从 (i, j - 1) 向右走一步走过来。所以可以写出状态转移方程为：dp[i][j] = dp[i - 1][j] + dp[i][j - 1]，此时 i > 0，j > 0。
    # 4. 初始条件
    # 从左上角走到 (0, 0) 只有一种方法，即 dp[0][0] = 1。
    # 第一行元素只有一条路径（即只能通过前一个元素向右走得到），所以 dp[0][j] = 1。
    # 同理，第一列元素只有一条路径（即只能通过前一个元素向下走得到），所以 dp[i][0] = 1。
    # 5. 最终结果
    # 根据状态定义，最终结果为 dp[m - 1][n - 1]，即从左上角到达右下角 (m - 1, n - 1) 位置的路径数量为 dp[m - 1][n - 1]。
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
        
# @lc code=end

