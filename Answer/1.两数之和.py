#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    # 使用哈希表来存储数组中每个元素的值和它的下标。然后，我们可以遍历数组，对于每个元素，我们检查目标值减去当前元素值是否在哈希表中。如果在，我们就找到了一对和为 target 的整数，并返回它们的下标。这种方法的时间复杂度是 O(N)，因为我们只需要遍历一次数组。
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 创建一个哈希表来存储元素的值和下标
        num_map = {}
        # 遍历数组
        for i, num in enumerate(nums):
            # 计算另一个数
            complement = target - num
            # 检查 complement 是否在哈希表中
            if complement in num_map:
                # 如果在，返回对应的下标
                return [num_map[complement], i]
            # 否则，将当前元素的下标添加到哈希表中
            num_map[num] = i

# @lc code=end

