#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    # 思路 1：贪心算法
    # 股票买卖获取利润主要是看差价，必然是低点买入，高点卖出才会赚钱。而要想获取最大利润，就要在跌入谷底的时候买入，在涨到波峰的时候卖出利益才会最大化。所以我们购买股票的策略变为了：
    # 连续跌的时候不买。
    # 跌到最低点买入。
    # 涨到最高点卖出。
    # 在这种策略下，只要计算波峰和谷底的差值即可。而波峰和谷底的差值可以通过两两相减所得的差值来累加计算。
    # 时间复杂度：O(n)，其中 n 是数组 prices 的元素个数。
    # 空间复杂度：O(1)
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(1, len(prices)):
            ans += max(0, prices[i] - prices[i-1])
        return ans

# @lc code=end

