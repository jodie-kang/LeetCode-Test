#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    # def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     if root is None:
    #         return []
    #     queue = [root]
    #     order = []
    #     flag = True
    #     while queue:
    #         level = deque()
    #         size = len(queue)
    #         for _ in range(size):
    #             cur = queue.pop(0)
    #             if flag:
    #                 level.append(cur.val)
    #             else:
    #                 level.appendleft(cur.val)
    #             if cur.left:
    #                 queue.append(cur.left)
    #             if cur.right:
    #                 queue.append(cur.right)
    #         if level:
    #             order.append(list(level))
    #         flag = not flag
    #     return order

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = [root]
        order = []
        flag = True
        while queue:
            level = []
            size = len(queue)
            for _ in range(size):
                cur = queue.pop(0)
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            if level:
                if flag:
                    order.append(level)
                else:
                    order.append(level[::-1])
            flag = not flag
        return order

# @lc code=end

