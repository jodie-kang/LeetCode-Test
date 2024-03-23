#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 思路 1：哈希表
        # 遍历数组 nums。
        # 对于当前元素 num，用哈希表统计每个元素 num 出现的次数。
        # 再遍历一遍哈希表，找出元素个数最多的元素即可。
        # 时间复杂度：O(n)，空间复杂度：O(n)
        numDict = dict()
        for num in nums:
            if num in numDict:
                numDict[num] += 1
            else:
                numDict[num] = 1
        max_cnt = 0
        max_num = -1
        for num in numDict:
            if numDict[num] > max_cnt:
                max_cnt = numDict[num]
                max_num = num
        return max_num

# @lc code=end

