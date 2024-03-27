#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution:
    # 思路 1：动态规划
    # 这道题跟「0053. 最大子序和」有点相似，不过一个求的是和的最大值，这道题求解的是乘积的最大值。
    # 乘积有个特殊情况，两个正数、两个负数相乘都会得到正数。所以求解的时候需要考虑负数的情况。
    # 若想要最终的乘积最大，则应该使子数组中的正数元素尽可能的大，负数元素尽可能的小。所以我们可以维护一个最大值变量和最小值变量。
    # 1. 划分阶段
    # 按照子数组的结尾位置进行阶段划分。
    # 2. 定义状态
    # 定义状态 dp_max[i] 为：以第 i 个元素结尾的乘积最大子数组的乘积。
    # 定义状态 dp_min[i] 为：以第 i 个元素结尾的乘积最小子数组的乘积。
    # 3. 状态转移方程
    # dp_max[i] = max(dp_max[i - 1] * nums[i], nums[i], dp_min[i - 1] * nums[i])
    # dp_min[i] = min(dp_min[i - 1] * nums[i], nums[i], dp_max[i - 1] * nums[i])
    # 4. 初始条件
    # 以第 0 个元素结尾的乘积最大子数组的乘积为 nums[0]，即 dp_max[0] = nums[0]。
    # 以第 0 个元素结尾的乘积最小子数组的乘积为 nums[0]，即 dp_min[0] = nums[0]。
    # 5. 最终结果
    # 根据状态定义，最终结果为 dp_max 中最大值，即乘积最大子数组的乘积。
    def maxProduct(self, nums: List[int]) -> int:
        size = len(nums)
        dp_max = [0 for _ in range(size)]
        dp_min = [0 for _ in range(size)]
        dp_max[0] = nums[0]
        dp_min[0] = nums[0]
        
        for i in range(1, size):
            dp_max[i] = max(dp_max[i-1] * nums[i], nums[i], dp_min[i-1] * nums[i])
            dp_min[i] = min(dp_min[i-1] * nums[i], nums[i], dp_max[i-1] * nums[i])
        return max(dp_max)

# @lc code=end

