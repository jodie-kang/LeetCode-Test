#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    # 通过交换数组，确保在较短的数组上进行二分查找。
    # 使用二分查找确定较短数组的分割位置，使得两个数组的左半部分和右半部分元素个数相等或左半部分多一个。
    # 根据两个数组的总元素个数是奇数还是偶数，计算中位数。
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2) 
        if n1 > n2:  # 如果 nums1 较长，交换两个数组
            return self.findMedianSortedArrays(nums2, nums1)

        # 计算中位数的索引
        k = (n1 + n2 + 1) // 2
        left = 0  # 定义 nums1 的左边界
        right = n1  # 定义 nums1 的右边界

        # 二分查找 nums1 中的分割位置
        while left < right:
            m1 = left + (right - left) // 2  # 在 nums1 中取前 m1 个元素的索引
            m2 = k - m1  # 在 nums2 中取前 m2 个元素的索引

            # 检查 nums1 中的 m1 元素是否应该与 nums2 中的 m2 元素配对
            if nums1[m1] < nums2[m2 - 1]:
                left = m1 + 1  # 如果 nums1 中的元素不够多，更新左边界
            else:
                right = m1  # 否则，更新右边界

        # 确定 nums1 的分割位置
        m1 = left
        # 确定 nums2 的分割位置
        m2 = k - m1

        # 计算中位数的左侧边界值
        c1 = max(float('-inf') if m1 <= 0 else nums1[m1 - 1],
                    float('-inf') if m2 <= 0 else nums2[m2 - 1])

        # 如果总元素个数是奇数，中位数是左侧边界值
        if (n1 + n2) % 2 == 1:
            return c1

        # 计算中位数的右侧边界值
        c2 = min(float('inf') if m1 >= n1 else nums1[m1],
                    float('inf') if m2 >= n2 else nums2[m2])

        # 如果总元素个数是偶数，中位数是两个边界值的平均
        return (c1 + c2) / 2

# @lc code=end

