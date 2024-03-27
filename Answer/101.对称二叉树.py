#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
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
    # 如果一棵二叉树是对称的，那么其左子树和右子树的外侧节点的节点值应当是相等的，并且其左子树和右子树的内侧节点的节点值也应当是相等的。
    # 那么我们可以通过递归方式，检查其左子树与右子树外侧节点和内测节点是否相等。即递归检查左子树的左子节点值与右子树的右子节点值是否相等（外侧节点值是否相等），递归检查左子树的右子节点值与右子树的左子节点值是否相等（内测节点值是否相等）。
    # 具体步骤如下：
    # 如果当前根节点为 None，则直接返回 True。
    # 如果当前根节点不为 None，则调用 check(left, right) 方法递归检查其左右子树是否对称。
    # 如果左子树节点为 None，并且右子树节点也为 None，则直接返回 True。
    # 如果左子树节点为 None，并且右子树节点不为 None，则直接返回 False。
    # 如果左子树节点不为 None，并且右子树节点为 None，则直接返回 False。
    # 如果左子树节点值不等于右子树节点值，则直接返回 False。
    # 如果左子树节点不为 None，并且右子树节点不为 None，并且左子树节点值等于右子树节点值，则：
    # 递归检测左右子树的外侧节点是否相等。
    # 递归检测左右子树的内测节点是否相等。
    # 如果左右子树的外侧节点、内测节点值相等，则返回 True
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.check(root.left, root.right)
    
    def check(self, left, right):
        if left == None and right == None:
            return True
        elif left == None and right != None:
            return False
        elif left != None and right == None:
            return False
        elif left.val != right.val:
            return False
        return self.check(left.left, right.right) and self.check(left.right, right.left)
        
# @lc code=end

