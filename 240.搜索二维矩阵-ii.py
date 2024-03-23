#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False

        for i in range(len(matrix)):
            if binarySearch(matrix[i], target):
                return True
        return False
        
# @lc code=end

