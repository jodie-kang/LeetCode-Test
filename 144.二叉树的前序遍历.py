#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
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
    # 二叉树的前序遍历递归实现步骤为：
    # 判断二叉树是否为空，为空则直接返回。
    # 先访问根节点。
    # 然后递归遍历左子树。
    # 最后递归遍历右子树。
    # def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     res = []
    #     def preorder(root):
    #         if not root:
    #             return
    #         res.append(root.val)
    #         preorder(root.left)
    #         preorder(root.right)
    #     preorder(root)
    #     return res
    # 思路 2：模拟栈迭代遍历
    # 判断二叉树是否为空，为空则直接返回。
    # 初始化维护一个栈，将根节点入栈。
    # 当栈不为空时：
    # 弹出栈顶元素 node，并访问该元素。
    # 如果 node 的右子树不为空，则将 node 的右子树入栈。
    # 如果 node 的左子树不为空，则将 node 的左子树入栈。
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:                        # 二叉树为空直接返回
            return []
            
        res = []
        stack = [root]

        while stack:                        # 栈不为空
            node = stack.pop()              # 弹出根节点
            res.append(node.val)            # 访问根节点
            if node.right:
                stack.append(node.right)    # 右子树入栈
            if node.left:
                stack.append(node.left)     # 左子树入栈

        return res
# @lc code=end

