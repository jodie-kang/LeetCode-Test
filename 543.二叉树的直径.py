#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
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
    # 这道题的重点是理解直径长度的定义。这里的直径并不是简单的「左子树高度」+「右子树高度」。
    # 而是 当前节点的直径 = max{左子树高度+右子树高度，所有子树中最大直径}。
    # 也就是说当前节点的直径可能来自于 「左子树高度」+「右子树高度」，也可能来自于「子树中的最大直径」。
    # 这就需要在递归求解子树高度的时候维护一个 maxDiameter 变量。每次递归都要去判断 当前「左子树高度」+「右子树的高度」是否大于 self.maxDiameter，如果大于，则更新最大值。
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0
        def height(root):
            nonlocal maxDiameter  # 声明maxDiameter为外部作用域的变量
            if root == None:
                return 0
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            maxDiameter = max(leftHeight + rightHeight, maxDiameter)
            return max(leftHeight, rightHeight) + 1
        height(root)
        return maxDiameter

# @lc code=end

