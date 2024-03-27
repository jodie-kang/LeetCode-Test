#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#

# @lc code=start
import functools
class Solution:
    # 思路 1：排序
    # 本质上是给数组进行排序。假设 x、y 是数组 nums 中的两个元素。
    # 如果拼接字符串 x + y < y + x，则 y > x 。y 应该排在 x 前面。反之，则 y < x。
    # 按照上述规则，对原数组进行排序即可。这里我们使用了 functools.cmp_to_key 自定义排序函数。
    # 时间复杂度：O(n^2)，空间复杂度：O(n)
    def largestNumber(self, nums: List[int]) -> str:
        ans = ""
        def cmp(a, b):
            if a + b == b + a:
                return 0
            elif a + b > b + a:
                return 1
            else:
                return -1
        nums_s = list(map(str, nums))
        nums_s.sort(key=functools.cmp_to_key(cmp), reverse=True)
        return str(int(''.join(nums_s)))

# @lc code=end

