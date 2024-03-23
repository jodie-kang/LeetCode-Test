#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    # 要求使用时间复杂度为 O(log n) 的算法解决问题，那么就需要使用「二分查找算法」了。
    # 进行两次二分查找，第一次尽量向左搜索。第二次尽量向右搜索。
    # 为了在O(log n)的时间复杂度内找到目标值target在数组中的开始位置和结束位置，我们可以使用二分查找算法的变体。
    # 首先，我们需要找到target的第一次出现位置，然后找到它的最后一次出现位置。由于数组是非递减排序的，我们可以确保在第一次出现位置之前的所有位置都不包含target。
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_leftmost(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        def find_rightmost(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right
        
        left_index = find_leftmost(nums, target)
        right_index = find_rightmost(nums, target)
        if left_index <= right_index:
            return [left_index, right_index]
        else:
            return [-1, -1]
# @lc code=end

