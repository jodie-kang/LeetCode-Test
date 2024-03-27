#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        water = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            water = max(water, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return water

# @lc code=end

