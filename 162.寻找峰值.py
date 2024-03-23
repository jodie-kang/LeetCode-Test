#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#

# @lc code=start
class Solution:
    # 使用两个指针 left、right 。left 指向数组第一个元素，right 指向数组最后一个元素。
    # 取区间中间节点 mid，并比较 nums[mid] 和 nums[mid + 1] 的值大小。
    # 如果 nums[mid] 小于 nums[mid + 1]，则右侧存在峰值，令 left = mid + 1。
    # 如果 nums[mid] 大于等于 nums[mid + 1]，则左侧存在峰值，令 right = mid。
    # 最后，当 left == right 时，跳出循环，返回 left。
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left
# @lc code=end

