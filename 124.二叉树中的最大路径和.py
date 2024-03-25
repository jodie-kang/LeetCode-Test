#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 思路：深度优先搜索
    # 如果根节点 root 为空，则返回 0。
    # 递归计算左子树的最大贡献值为 left_max。
    # 递归计算右子树的最大贡献值为 right_max。
    # 更新维护最大路径和变量，即 self.max_sum = max(self.max_sum, root.val + left_max + right_max)。
    # 返回以当前节点为根节点，并且经过该节点的最大贡献值。即返回「当前节点值」+「左右子节点的最大贡献值中较大的一个」。
    # 最终 self.max_sum 即为答案。
    def __init__(self):
        self.max_sum = float('-inf')

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.max_sum
    
    def dfs(self, root):
        if not root:
            return 0
        left_max = max(self.dfs(root.left), 0)
        right_max = max(self.dfs(root.right), 0)
        self.max_sum = max(self.max_sum, root.val + left_max + right_max)
        return root.val + max(left_max, right_max)

# @lc code=end

