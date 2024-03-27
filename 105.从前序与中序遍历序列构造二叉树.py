#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 从前序遍历顺序中当前根节点的位置在 postorder[0]。
    # 通过在中序遍历中查找上一步根节点对应的位置 inorder[k]，从而将二叉树的左右子树分隔开，并得到左右子树节点的个数。
    # 从上一步得到的左右子树个数将前序遍历结果中的左右子树分开。
    # 构建当前节点，并递归建立左右子树，在左右子树对应位置继续递归遍历并执行上述三步，直到节点为空。
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 前序：根，左，右
        # 中序：左，根，右
        def createTree(preorder, inorder, n):
            if n == 0:
                return None
            k = 0
            while preorder[0] != inorder[k]:
                k += 1
            node = TreeNode(inorder[k])
            node.left = createTree(preorder[1:k+1], inorder[0:k], k)
            node.right = createTree(preorder[k+1:], inorder[k+1:], n-k-1)
            return node
        return createTree(preorder, inorder, len(inorder))
# @lc code=end

