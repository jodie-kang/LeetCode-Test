#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    # 我们使用两个指针 left 和 right 来表示当前搜索范围的边界。在每次迭代中，我们首先检查 nums[mid] 是否等于 target。如果等于，我们找到了目标值并返回它的下标。如果不等于，我们需要确定 target 位于有序的左半部分还是右半部分。我们通过比较 nums[left] 和 nums[mid] 来判断左半部分是否有序。如果是有序的，并且 target 位于 nums[left] 和 nums[mid] 之间，我们将搜索范围移动到左半部分；否则，我们移动到右半部分。如果右半部分是有序的，我们对 target 进行类似的检查，但针对右半部分。如果 target 不在数组中，搜索范围最终会相交，循环结束，我们返回 -1 表示未找到目标值。
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # 判断左半部分是否有序
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # 右半部分有序
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
# @lc code=end

