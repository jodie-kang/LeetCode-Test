#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
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
    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     res = []
    #     def inorder(root):
    #         if root == None:
    #             return res
    #         inorder(root.left)
    #         res.append(root.val)
    #         inorder(root.right)
    #     inorder(root)
    #     return res
    # 思路 2：模拟栈迭代遍历
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:                # 二叉树为空直接返回
            return []
        
        res = []
        stack = []

        while root or stack:        # 根节点或栈不为空
            while root:
                stack.append(root)  # 将当前树的根节点入栈
                root = root.left    # 找到最左侧节点
            
            node = stack.pop()      # 遍历到最左侧，当前节点无左子树时，将最左侧节点弹出
            res.append(node.val)    # 访问该节点
            root = node.right       # 尝试访问该节点的右子树
        return res

        
# @lc code=end

