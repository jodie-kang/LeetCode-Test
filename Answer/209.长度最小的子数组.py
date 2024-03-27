#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#


# @lc code=start
class Solution:
    # 思路：不定长度的 滑动窗口
    # 用滑动窗口来记录连续子数组的和，设定两个指针：left、right，分别指向滑动窗口的左右边界，保证窗口中的和刚好大于等于 target。
    # 一开始，left、right 都指向 0。
    # 向右移动 right，将最右侧元素加入当前窗口和 window_sum 中。
    # 如果 window_sum >= target，则不断右移 left，缩小滑动窗口长度，并更新窗口和的最小值，直到 window_sum < target。
    # 然后继续右移 right，直到 right >= len(nums) 结束。
    # 输出窗口和的最小值作为答案。
    # 时间复杂度：O(n)，空间复杂度：O(1)
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        size = len(nums)
        left, right = 0, 0
        window_sum = 0
        ans = size + 1
        while right < size:
            window_sum += nums[right]
            while window_sum >= target:
                ans = min(ans, right - left + 1)
                window_sum -= nums[left]
                left += 1
            right += 1
        return ans if ans != size + 1 else 0

# @lc code=end
