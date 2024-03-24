#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
class Solution:
    # 思路：哈希表
    # 先将数组存储到集合中进行去重，然后使用 curr_streak 维护当前连续序列长度，使用 ans 维护最长连续序列长度。
    # 遍历集合中的元素，对每个元素进行判断，如果该元素不是序列的开始（即 num - 1 在集合中），则跳过。
    # 如果 num - 1 不在集合中，说明 num 是序列的开始，判断 num + 1 、nums + 2、... 是否在哈希表中，并不断更新当前连续序列长度 curr_streak。并在遍历结束之后更新最长序列的长度。
    # 最后输出最长序列长度。
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        nums_set = set(nums)
        for num in nums_set:
            if num - 1 not in nums_set:
                curr_num = num
                curr_streak = 1
                while curr_num + 1 in nums_set:
                    curr_num += 1
                    curr_streak += 1
                ans = max(ans, curr_streak)
        return ans
# @lc code=end

