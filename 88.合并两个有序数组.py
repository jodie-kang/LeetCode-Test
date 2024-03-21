#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    # 思路 1：快慢指针
    # 将两个指针 index1、index2 分别指向 nums1、nums2 数组的尾部，再用一个指针 index 指向数组 nums1 的尾部。
    # 从后向前判断当前指针下 nums1[index1] 和 nums[index2] 的值大小，将较大值存入 num1[index] 中，然后继续向前遍历。
    # 最后再将 nums2 中剩余元素赋值到 num1 前面对应位置上。
    # 时间复杂度：O(m+n)，空间复杂度：O(m+n)
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index1, index2 = m-1, n-1
        index = m + n - 1
        while index1 >= 0 and index2 >= 0:
            if nums1[index1] < nums2[index2]:
                nums1[index] = nums2[index2]
                index2 -= 1
            else:
                nums1[index] = nums1[index1]
                index1 -= 1
            index -= 1
        nums1[:index2+1] = nums2[:index2+1]
        
# @lc code=end

