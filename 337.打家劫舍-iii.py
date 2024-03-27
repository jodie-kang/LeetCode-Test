#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 这个问题可以通过动态规划的方法来解决，关键是要在树结构上应用动态规划。对于树中的每个节点，小偷有两个选择：要么盗取这个节点的房子，要么不盗取。如果小偷决定盗取当前节点的房子，那么就不能盗取其子节点的房子；如果小偷决定不盗取当前节点的房子，那么可以选择盗取或不盗取其子节点的房子。
    # 因此，对于每个节点，我们可以维护两个值：
    # robbed：如果盗取当前节点的房子，从当前节点开始所能获得的最大金额。
    # notRobbed：如果不盗取当前节点的房子，从当前节点开始所能获得的最大金额。
    # 对于树的叶节点，如果盗取这个节点的房子，那么 robbed 就是节点的值；如果不盗取这个节点的房子，那么 notRobbed 就是0。对于非叶节点，我们可以递归地计算其子节点的 robbed 和 notRobbed 值，然后根据这些值来确定当前节点的最优选择。
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0, 0)  # (盗取当前节点，不盗取当前节点)

            left = dfs(node.left)
            right = dfs(node.right)

            # 如果盗取当前节点，那么不能盗取其子节点
            robbed = node.val + left[1] + right[1]
            # 如果不盗取当前节点，可以选择盗取或不盗取其子节点，选择其中的最大值
            notRobbed = max(left) + max(right)

            return (robbed, notRobbed)

        return max(dfs(root))
# @lc code=end

