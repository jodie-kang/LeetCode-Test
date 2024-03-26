#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    # 思路 1：递推
    # 设置两个变量 minprice（用来记录买入的最小值）、maxprofit（用来记录可获取的最大利润）。
    # 从左到右进行遍历数组 prices。
    # 如果遇到当前价格比 minprice 还要小的，就更新 minprice。
    # 如果遇到当前价格大于或者等于 minprice，则判断一下以当前价格卖出的话能卖多少，如果比 maxprofit 还要大，就更新 maxprofit。
    # 最后输出 maxprofit。
    # 时间复杂度：O(n)，其中 n 是数组 prices 的元素个数。
    # 空间复杂度：O(1)
    def maxProfit(self, prices: List[int]) -> int:
        minprice = 10010
        maxprofit = 0
        for p in prices:
            if p < minprice:
                minprice = p
            elif p - minprice > maxprofit:
                maxprofit = p - minprice
        return maxprofit
# @lc code=end

