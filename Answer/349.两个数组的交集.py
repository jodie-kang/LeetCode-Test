#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        left1, left2 = 0, 0
        res = []
        while left1 < len(nums1) and left2 < len(nums2):
            if nums1[left1] == nums2[left2]:
                if nums1[left1] not in res:
                    res.append(nums1[left1])
                left1 += 1
                left2 += 1
            elif nums1[left1] < nums2[left2]:
                left1 += 1
            elif nums1[left1] > nums2[left2]:
                left2 += 1
        return res
# @lc code=end

