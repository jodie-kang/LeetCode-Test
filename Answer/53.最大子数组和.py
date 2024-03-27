#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
class Solution:
    # 思路 1：动态规划
    # 定义状态 dp[i] 为：以第 i 个数结尾的连续子数组的最大和。
    # 则最终结果应为所有 dp[i] 的最大值，即 max(dp)。
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [float('-inf') for _ in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if dp[i-1] > 0:
                dp[i] = dp[i-1] + nums[i]
            else:
                dp[i] = nums[i]
        return max(dp)
    # 思路 2：动态规划 + 滚动优化
    # 因为 dp[i] 只和 dp[i - 1] 和当前元素 nums[i] 相关，我们也可以使用一个变量 sub_max 来表示以第 i 个数结尾的连续子数组的最大和。然后使用 ans_max 来保存全局中最大值。
    # def maxSubArray(self, nums: List[int]) -> int:
    #     size = len(nums)
    #     sub_max = nums[0]
    #     ans_max = nums[0]

    #     for i in range(1, size):
    #         if sub_max < 0:
    #             sub_max = nums[i]
    #         else:
    #             sub_max += nums[i]
    #         ans_max = max(ans_max, sub_max)
    #     return ans_max
# @lc code=end

