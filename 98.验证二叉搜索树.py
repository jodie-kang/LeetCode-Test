#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
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
    # 根据题意进行递归遍历即可。前序、中序、后序遍历都可以。
    # 以前序遍历为例，递归函数为：preorderTraversal(root, min_v, max_v)。
    # 前序遍历时，先判断根节点的值是否在 (min_v, max_v) 之间。
    # 如果不在则直接返回 False。
    # 如果在区间内，则继续递归检测左右子树是否满足，都满足才是一棵二叉搜索树。
    # 当递归遍历左子树的时候，要将上界 max_v 改为左子树的根节点值，因为左子树上所有节点的值均小于根节点的值。
    # 当递归遍历右子树的时候，要将下界 min_v 改为右子树的根节点值，因为右子树上所有节点的值均大于根节点。
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def preorderTraverse(root, max_v, min_v):
            if root == None:
                return True
            if root.val >= max_v or root.val <= min_v:
                return False
            return preorderTraverse(root.left, root.val, min_v) and preorderTraverse(root.right, max_v, root.val)
        return preorderTraverse(root, float('inf'), float('-inf'))
# @lc code=end

