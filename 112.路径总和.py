#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 思路 1：递归遍历
    # 定义一个递归函数，递归函数传入当前根节点 root，目标节点和 targetSum，以及新增变量 currSum（表示为从根节点到当前节点的路径上所有节点值之和）。
    # 递归遍历左右子树，同时更新维护 currSum 值。
    # 如果当前节点为叶子节点时，判断 currSum 是否与 targetSum 相等。
    # 如果 currSum 与 targetSum 相等，则返回 True。
    # 如果 currSum 不与 targetSum 相等，则返回 False。
    # 如果当前节点不为叶子节点，则继续递归遍历左右子树。
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def preorder(root, targetSum, curSum):
            if root == None:
                return False
            curSum += root.val
            if root.left == None and root.right == None:
                return curSum == targetSum
            else:
                return preorder(root.left, targetSum, curSum) or preorder(root.right, targetSum, curSum)
        return preorder(root, targetSum, 0)
            
# @lc code=end

