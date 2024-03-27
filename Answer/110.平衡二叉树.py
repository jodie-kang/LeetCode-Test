#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
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
    # 先递归遍历左右子树，判断左右子树是否平衡，再判断以当前节点为根节点的左右子树是否平衡。
    # 如果遍历的子树是平衡的，则返回它的高度，否则返回 -1。
    # 只要出现不平衡的子树，则该二叉树一定不是平衡二叉树。
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if root == None:
                return False
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1
            else:
                return max(leftHeight, rightHeight) + 1
        return height(root) >= 0
# @lc code=end

