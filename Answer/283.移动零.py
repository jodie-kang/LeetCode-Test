#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    # 思路 2：快慢指针
    # 使用两个指针 slow，fast。slow 指向处理好的非 0 数字数组的尾部，fast 指针指向当前待处理元素。
    # 不断向右移动 fast 指针，每次移动到非零数，则将左右指针对应的数交换，交换同时将 slow 右移。
    # 此时，slow 指针左侧均为处理好的非零数，而从 slow 指针指向的位置开始， fast 指针左边为止都为 0。
    # 遍历结束之后，则所有 0 都移动到了右侧，且保持了非零数的相对位置。
    # 时间复杂度：O(n)，空间复杂度：O(1)
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1

# @lc code=end

