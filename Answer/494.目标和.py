#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

# @lc code=start
class Solution:
    # 假设数组中所有元素和为 sum，数组中所有符号为 + 的元素为 sum_x，符号为 - 的元素和为 sum_y。则 target = sum_x - sum_y。
    # 而 sum_x + sum_y = sum。根据两个式子可以求出 2 * sum_x = target + sum ，即 sum_x = (target + sum) / 2。
    # 那么这道题就变成了，如何在数组中找到一个集合，使集合中元素和为 (target + sum) / 2。这就变为了求容量为 (target + sum) / 2 的 01 背包问题。
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sum_nums = sum(nums)
        if abs(target) > abs(sum_nums) or (target + sum_nums) % 2 == 1:
            return 0
        size = (target + sum_nums) // 2
        dp = [0 for _ in range(size + 1)]
        dp[0] = 1
        for num in nums:
            for i in range(size, num-1, -1):
                dp[i] = dp[i] + dp[i-num]
        return dp[size]
# @lc code=end

