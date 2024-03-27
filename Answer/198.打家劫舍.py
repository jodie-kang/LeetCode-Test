#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    # 1. 划分阶段
    # 按照房屋序号进行阶段划分。
    # 2. 定义状态
    # 定义状态 dp[i] 表示为：前 i 间房屋所能偷窃到的最高金额。
    # 3. 状态转移方程
    # 如果房屋数大于等于 3 间，则偷窃第 i 间房屋的时候，就有两种状态：
    # 偷窃第 i 间房屋，那么第 i - 1 间房屋就不能偷窃了，偷窃的最高金额为：前 i - 2 间房屋的最高总金额 + 第 i 间房屋的金额，即 dp[i] = dp[i - 2] + nums[i]；
    # 不偷窃第 i 间房屋，那么第 i - 1 间房屋可以偷窃，偷窃的最高金额为：前 i - 1 间房屋的最高总金额，即 dp[i] = dp[i - 1]。
    # 然后这两种状态取最大值即可，即状态转移方程为：dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])，i > 2 时。
    # 4. 初始条件
    # 如果只有一间房，则直接偷这间屋子就能偷到最高金额，即 dp[0] = nums[i]。
    # 如果只有两间房，那么就选择金额最大的那间屋进行偷窃，就可以偷到最高金额，即 dp[1] = max(nums[0], nums[1])。
    # 5. 最终结果
    # 根据我们之前定义的状态，dp[i] 表示为：前 i 间房屋所能偷窃到的最高金额。则最终结果为 dp[size - 1]，size 为总的房屋数。
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 1:
            return nums[0]
        # if size == 2:
        #     return max(nums[0], nums[1])
        
        dp = [0 for _ in range(size)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, size):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        
        return dp[size-1]
# @lc code=end

