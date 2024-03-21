#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
class Solution:
    # 思路 1：位运算
    # 根据异或运算的性质，对 n 个数不断进行异或操作，最终可得到单次出现的元素。
    # 时间复杂度：O(n)，空间复杂度：O(1)
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        ans = 0
        for i in range(len(nums)):
            ans ^= nums[i]
        return ans
# @lc code=end

