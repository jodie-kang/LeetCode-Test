#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#

# @lc code=start
class Solution:
    # 思路：原地哈希
    # 我们可以将当前数组视为哈希表。一个长度为 n 的数组，对应存储的元素值应该为 [1, n + 1] 之间，其中还包含一个缺失的元素。
    # 我们可以遍历一遍数组，将当前元素放到其对应位置上（比如元素值为 1 的元素放到数组第 0 个位置上、元素值为 2 的元素放到数组第 1 个位置上，等等）。
    # 然后再次遍历一遍数组。遇到第一个元素值不等于下标 + 1 的元素，就是答案要求的缺失的第一个正数。
    # 如果遍历完没有在数组中找到缺失的第一个正数，则缺失的第一个正数是 n + 1。
    # 最后返回我们找到的缺失的第一个正数。
    def firstMissingPositive(self, nums: List[int]) -> int:
        size = len(nums)
        for i in range(size):
            # 当 nums[i] 在范围内(1 到 size)，并且 nums[i] 不是 nums[nums[i] - 1] 时
            while 1 <= nums[i] <= size and nums[i] != nums[nums[i] - 1]:
                index1 = i  # 当前元素的索引
                index2 = nums[i] - 1  # nums[i] 所指向的元素的索引
                # 交换 nums[i] 和 nums[nums[i] - 1] 的值
                nums[index1], nums[index2] = nums[index2], nums[index1]
        # 再次遍历数组，找到第一个不符合 nums[i] == i + 1 的情况
        for i in range(size):
            if nums[i] != i + 1:
                # 返回第一个缺失的正整数的索引加 1
                return i + 1
        # 如果所有正整数都存在，则返回 size + 1 作为第一个缺失的正整数
        return size + 1

# @lc code=end

