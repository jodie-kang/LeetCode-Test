#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#


# @lc code=start
class Solution:
    # 思路：动态规划
    # 一天结束时，可能有持股、可能未持股、可能卖出过1次、可能卖出过2次、也可能未卖出过
    # 所以定义状态转移数组dp[天数][当前是否持股][卖出的次数]
    # 具体一天结束时的6种状态：
    # 未持股，未卖出过股票：说明从未进行过买卖，利润为0
    # dp[i][0][0]=0
    # 未持股，卖出过1次股票：可能是今天卖出，也可能是之前卖的（昨天也未持股且卖出过）
    # dp[i][0][1]=max(dp[i-1][1][0]+prices[i],dp[i-1][0][1])
    # 未持股，卖出过2次股票:可能是今天卖出，也可能是之前卖的（昨天也未持股且卖出过）
    # dp[i][0][2]=max(dp[i-1][1][1]+prices[i],dp[i-1][0][2])
    # 持股，未卖出过股票：可能是今天买的，也可能是之前买的（昨天也持股）
    # dp[i][1][0]=max(dp[i-1][0][0]-prices[i],dp[i-1][1][0])
    # 持股，卖出过1次股票：可能是今天买的，也可能是之前买的（昨天也持股）
    # dp[i][1][1]=max(dp[i-1][0][1]-prices[i],dp[i-1][1][1])
    # 持股，卖出过2次股票：最多交易2次，这种情况不存在
    # dp[i][1][2]=float('-inf')
    # 作者：MarcusXu
    # 链接：https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/solutions/71209/tong-su-yi-dong-de-dong-tai-gui-hua-jie-fa-by-marc/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []:
            return 0
        length = len(prices)
        # 结束时的最高利润=[天数][是否持有股票][卖出次数]
        dp = [[[0, 0, 0], [0, 0, 0]] for i in range(0, length)]
        # 第一天休息
        dp[0][0][0] = 0
        # 第一天买入
        dp[0][1][0] = -prices[0]
        # 第一天不可能已经有卖出
        dp[0][0][1] = float("-inf")
        dp[0][0][2] = float("-inf")
        # 第一天不可能已经卖出
        dp[0][1][1] = float("-inf")
        dp[0][1][2] = float("-inf")
        for i in range(1, length):
            # 未持股，未卖出过，说明从未进行过买卖
            dp[i][0][0] = 0
            # 未持股，卖出过1次，可能是今天卖的，可能是之前卖的
            dp[i][0][1] = max(dp[i - 1][1][0] + prices[i], dp[i - 1][0][1])
            # 未持股，卖出过2次，可能是今天卖的，可能是之前卖的
            dp[i][0][2] = max(dp[i - 1][1][1] + prices[i], dp[i - 1][0][2])
            # 持股，未卖出过，可能是今天买的，可能是之前买的
            dp[i][1][0] = max(dp[i - 1][0][0] - prices[i], dp[i - 1][1][0])
            # 持股，卖出过1次，可能是今天买的，可能是之前买的
            dp[i][1][1] = max(dp[i - 1][0][1] - prices[i], dp[i - 1][1][1])
            # 持股，卖出过2次，不可能
            dp[i][1][2] = float("-inf")
        return max(dp[length - 1][0][1], dp[length - 1][0][2], 0)

# @lc code=end
