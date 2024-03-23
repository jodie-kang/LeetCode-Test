#
# @lc app=leetcode.cn id=718 lang=python3
#
# [718] 最长重复子数组
#

# @lc code=start
class Solution:
    # 思路1：滑动窗口
    # 我们可以将两个数组分别看做是两把直尺。然后将数组 nums1 固定， 让 nums2 的尾部与 nums1 的头部对齐
    # 然后逐渐向右移动直尺 nums2，比较 nums1 与 nums2 重叠部分中的公共子数组的长度，直到直尺 nums2 的头部移动到 nums1 的尾部。
    # 时间复杂度：O(n^2)，其中 n 是数组 nums1 和 nums2 的长度。这是因为我们需要对 nums1 和 nums2 进行两次遍历，每次遍历的时间复杂度为 O(n)
    # def findLength(self, nums1: List[int], nums2: List[int]) -> int:
    #     # 辅助函数，计算从nums1的第i个位置和nums2的第j个位置开始的最长公共子序列的长度
    #     def findMaxLength(nums1, nums2, i, j):
    #         size1, size2 = len(nums1), len(nums2)
    #         max_len = 0  # 初始化最长公共子序列的最大长度为0
    #         cur_len = 0  # 初始化当前位置的公共子序列长度为0
    #         # 遍历两个数组，寻找最长公共子序列
    #         while i < size1 and j < size2:
    #             if nums1[i] == nums2[j]:  # 如果当前元素相同
    #                 cur_len += 1  # 增加当前公共子序列长度
    #                 max_len = max(max_len, cur_len)  # 更新最大公共子序列长度
    #             else:
    #                 cur_len = 0  # 如果当前元素不同，重置公共子序列长度
    #             i += 1  # 移动nums1的指针
    #             j += 1  # 移动nums2的指针
    #         return max_len
    #     size1, size2 = len(nums1), len(nums2)
    #     res = 0
    #     # 遍历nums1，对于每个位置i，计算以i为起点的最长公共子序列长度，并更新结果
    #     for i in range(size1):
    #         res = max(res, findMaxLength(nums1, nums2, i, 0))
    #     # 遍历nums2，对于每个位置i，计算以i为起点的最长公共子序列长度，并更新结果
    #     for i in range(size2):
    #         res = max(res, findMaxLength(nums1, nums2, 0, i))
    #     return res
    # 思路2：动态规划
    # 这段代码的时间复杂度是 O(m * n)，其中 m 和 n 分别是 nums1 和 nums2 的长度。空间复杂度也是 O(m * n)，因为我们需要一个二维数组来存储所有的中间结果。
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # 初始化 DP 表
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        # 记录最长公共子数组的长度
        max_length = 0

        # 填充 DP 表
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                # 如果当前元素相同，更新 dp 表
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_length = max(max_length, dp[i][j])
                else:
                    # 如果当前元素不同，重置 dp[i][j]
                    dp[i][j] = 0
        return max_length
# @lc code=end

