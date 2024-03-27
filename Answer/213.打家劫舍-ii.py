#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#


# @lc code=start
class Solution:
    # 这道题可以看做是「198. 打家劫舍」的升级版。
    # 如果房屋数大于等于 3 间，偷窃了第 1 间房屋，则不能偷窃最后一间房屋。同样偷窃了最后一间房屋则不能偷窃第 1  间房屋。
    # 假设总共房屋数量为 size ，这种情况可以转换为分别求解 [0, size-2] 和 [1, size-1] 范围下首尾不相连的房屋所能偷窃的最高金额，然后再取这两种情况下的最大值。
    # 而求解 [0, size-2] 和 [1, size-1] 范围下首尾不相连的房屋所能偷窃的最高金额问题就跟「198. 打家劫舍」所求问题一致了。
    def helper(self, nums):
        size = len(nums)
        dp = [0 for _ in range(size)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, size):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[size - 1]

    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 1:
            return nums[0]
        if size == 2:
            return max(nums[0], nums[1])
        return max(self.helper(nums[: size - 1]), self.helper(nums[1:]))

# @lc code=end
