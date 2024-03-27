#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 思路 1：回溯
    # 在回溯的同时，记录下当前路径。同时维护 targetSum，每遍历到一个节点，就减去该节点值。如果遇到叶子节点，并且 targetSum == 0 时，将当前路径加入答案数组中。然后递归遍历左右子树，并回退当前节点，继续遍历。
    # 具体步骤如下：
    # 使用列表 res 存储所有路径，使用列表 path 存储当前路径。
    # 如果根节点为空，则直接返回。
    # 将当前节点值添加到当前路径 path 中。
    # targetSum 减去当前节点值。
    # 如果遇到叶子节点，并且 targetSum == 0 时，将当前路径加入答案数组中。
    # 递归遍历左子树。
    # 递归遍历右子树。
    # 回退当前节点，继续递归遍历。
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        path = []
        def dfs(root, targetSum):
            if root is None:
                return 
            path.append(root.val)
            targetSum -= root.val
            if not root.left and not root.right and targetSum == 0:
                res.append(path[:])
            dfs(root.left, targetSum)
            dfs(root.right, targetSum)
            path.pop()
        dfs(root, targetSum)
        return res
# @lc code=end

