#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    # 思路 2：完全背包问题
    # 可以转换为有 n 枚不同的硬币，每种硬币可以无限次使用。凑成总金额为 amount 的背包，最少需要多少硬币。
    # 1. 划分阶段
    # 按照子串的起始位置进行阶段划分。

    # 2. 定义状态
    # 定义状态 dp[i] 表示为：凑成总金额为 i 的最少硬币数量。

    # 3. 状态转移方程
    # dp[i] 来源于两部分：
    # 不使用当前硬币，只使用之前硬币凑成金额 i 的最少硬币数量。
    # 凑成金额 i - num 的最少硬币数量，再加上当前硬币。
    # 上述两者的较小值即为 dp[i]。

    # 4. 初始条件
    # 凑成总金额为 0 的最少硬币数量为 0，即 dp[0] = 0。
    # 5. 最终结果
    # 根据我们之前定义的状态，dp[i] 表示为：凑成总金额为 i 的最少硬币数量。则最终结果为 dp[amount]。
    # 时间复杂度：O(amount * size)。其中 amount 表示总金额，size 表示硬币的种类数。
    # 空间复杂度： O(amount)。
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[amount] != float('inf'):
            return dp[amount]
        else:
            return -1

# @lc code=end

