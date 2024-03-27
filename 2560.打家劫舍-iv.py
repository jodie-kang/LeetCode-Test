#
# @lc app=leetcode.cn id=2560 lang=python3
#
# [2560] 打家劫舍 IV
#

# @lc code=start
class Solution:
    # 思路 1：使用三维动态规划
    # 这个方法的核心是维护一个三维DP数组，其时间复杂度和空间复杂度可能相对较高。
    # def minCapability(self, nums: List[int], k: int) -> int:
    #     n = len(nums)
    #     # 初始化三维DP数组，dp[i][j][l] 表示前i个房间，是否偷第i个房间，偷了l个房间时的最大金额
    #     dp = [[[0 for _ in range(k+1)] for _ in range(2)] for _ in range(n+1)]
        
    #     # 初始化，至少偷k间房屋的情况
    #     for l in range(1, k+1):
    #         dp[0][0][l] = float('-inf')  # 如果没有房间可偷，但是要求偷l间，则设置为无穷小
        
    #     for i in range(1, n+1):
    #         for l in range(1, k+1):
    #             dp[i][0][l] = max(dp[i-1][0][l], dp[i-1][1][l])  # 不偷当前房间
    #             dp[i][1][l] = nums[i-1] + dp[i-1][0][l-1]  # 偷当前房间
                
    #     # 最后返回偷和不偷第n个房间，且至少偷了k间房屋的最大金额
    #     return max(dp[n][0][k], dp[n][1][k])

    # 时间复杂度：O(n*k)
    # 空间复杂度：O(n*k*2)

    # 思路 2：修改的滑动窗口 + 打家劫舍动态规划
    # 这个方法在每个窗口内部使用标准的打家劫舍动态规划算法，并确保每个窗口至少包含 k 个房子。
    def rob(self, nums):
        # 标准打家劫舍动态规划解法
        # 标准的打家劫舍动态规划算法
        if not nums:
            return 0
        n = len(nums)
        if n <= 2:
            return max(nums)

        dp = [0] * n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        return dp[-1]

    def minCapability(self, nums: List[int], k: int) -> int:
        min_ability = float('inf')

        # 窃取连续的k间房屋，并计算这种情况下的总金额
        for i in range(len(nums) - k + 1):
            # 计算窃取连续k间房屋的金额
            stolen_amount = sum(nums[i:i+k])
            # 计算窃取这k间房屋前后的其他房屋的最大金额
            max_amount_before = self.rob(nums[:i-1]) if i >= 2 else 0  # 确保不窃取相邻的房屋
            max_amount_after = self.rob(nums[i+k+1:]) if i + k < len(nums) else 0  # 确保不窃取相邻的房屋
            # 更新最小窃取能力
            min_ability = min(min_ability, stolen_amount + max_amount_before + max_amount_after)

        return min_ability

    # # 时间复杂度：O(n^2) 对于每个窗口都需要进行一次动态规划计算
    # # 空间复杂度：O(n) 用于存储动态规划数组

# @lc code=end

