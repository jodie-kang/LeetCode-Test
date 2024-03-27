#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
class Solution:
    # 为了在O(log n)的时间复杂度内找到旋转后的升序数组中的最小元素，我们可以使用二分查找算法。
    # 由于数组是旋转的，所以最小元素位于数组的旋转点或其右侧。
    # 我们可以通过比较中间元素与其右侧元素的值来判断最小元素的位置。
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            # 如果中间元素大于其右侧元素，说明最小值在右侧或就是中间元素
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # 否则，最小值在左侧或就是中间元素
                right = mid

        # 当 left 和 right 相遇时，找到了最小值
        return nums[left]
# @lc code=end

