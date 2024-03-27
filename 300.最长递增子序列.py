#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
    # 思路1：动态规划
    # dp[i] 表示为：以 nums[i] 结尾的最长递增子序列长度。那为了计算出最大的最长递增子序列长度，则需要再遍历一遍 dp 数组，求出最大值即为最终结果。
    # 状态转移方程为：dp[i] = max(dp[i], dp[j] + 1)，0 <= j <= i，nums[j] < nums[i]
    # 时间复杂度：O(n^2)
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     dp = [1 for _ in range(len(nums)+1)]
    #     for j in range(len(nums)):
    #         for i in range(j, len(nums)):
    #             if nums[i] > nums[j]:
    #                 dp[i] = max(dp[i], dp[j] + 1)
    #     return max(dp)
    # 思路2：二分查找 + 动态规划
    # 时间复杂度：O(n * log n)
    def lengthOfLIS(self, nums):
        # tails数组，其中tails[i]存储长度为i+1的所有递增子序列的最小尾部元素
        tails = [0] * len(nums)
        # size变量用于跟踪当前已知的最长递增子序列的长度
        size = 0
        for x in nums:  # 遍历给定数组中的每个元素x
            # 使用二分查找法，在tails数组中查找第一个大于等于x的元素的位置
            i, j = 0, size
            while i != j:
                m = (i + j) // 2  # 计算中间位置
                if tails[m] < x:  # 如果中间位置的元素小于x，则在右侧子数组中继续查找
                    i = m + 1
                else:  # 否则，在左侧子数组中继续查找
                    j = m
            tails[i] = x  # 找到位置后，更新或者添加新的元素x到tails数组
            # 如果i等于当前的size，则表示我们在tails的末尾添加了新的元素，因此递增子序列的长度增加了1
            size = max(i + 1, size)
        # 遍历完成后，size即为最长递增子序列的长度
        return size

# @lc code=end

