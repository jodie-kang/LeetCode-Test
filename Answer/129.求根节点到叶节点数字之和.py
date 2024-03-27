#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根节点到叶节点数字之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 思路 1：深度优先搜索
    # 记录下路径上所有节点构成的数字，使用变量 pre_total 保存下当前路径上构成的数字。
    # 如果遇到叶节点，则直接返回当前数字。
    # 如果没有遇到叶节点，则递归遍历左右子树，并累加对应结果。
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, pre_total):
            if root is None:
                return 0
            total = pre_total * 10 + root.val
            if not root.left and not root.right:
                return total
            return dfs(root.left, total) + dfs(root.right, total)
        
        return dfs(root, 0)
# @lc code=end

